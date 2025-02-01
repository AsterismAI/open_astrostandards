# #############################################################################
# AstroStandards coordinate transforms
#
# Kerry N. Wood (kerry.wood@asterism.ai)
#
# January 2015
# assume that the AstroStandards are loaded outside this library and passed in
# this allows us to be more creative with loading / unloading
#
# you could absolutely do all this with AstroPy, but this implementation uses
# the openly available AstroFuncDll code as an example (and as a check)
# #############################################################################

import numpy as np
import pandas as pd
import ctypes
import helpers

# -----------------------------------------------------------------------------
def temej2k( pos, vel, date : float, func : callable ):
    topos  = (ctypes.c_double*3)()
    tovel  = (ctypes.c_double*3)()    
    func(  1, 
           106, 
           date, 
           (ctypes.c_double * 3)(*pos), 
           (ctypes.c_double * 3)(*vel), 
           topos, 
           tovel )  
    return np.array( topos ), np.array( tovel )

# -----------------------------------------------------------------------------
def j2k_to_teme( pos, vel, date, AstroFuncDll ):
    return temej2k( pos, vel, date, AstroFuncDll.RotJ2KToDate )

# -----------------------------------------------------------------------------
def teme_to_j2k( pos, vel, date, AstroFuncDll ):
    return temej2k( pos, vel, date, AstroFuncDll.RotDateToJ2K )

# -----------------------------------------------------------------------------
def teme_to_efg(  pos, vel, date, AstroFuncDll ):
    topos  = (ctypes.c_double*3)()
    tovel  = (ctypes.c_double*3)()                   
    AstroFuncDll.ECIToEFGTime( date, 
                               (ctypes.c_double * 3)(*pos), 
                               (ctypes.c_double * 3)(*vel), 
                               topos, 
                               tovel )
    return np.array( topos ), np.array( tovel )

# -----------------------------------------------------------------------------
def efg_to_teme(  pos, vel, date, AstroFuncDll ):
    topos  = (ctypes.c_double*3)()
    tovel  = (ctypes.c_double*3)()                   
    AstroFuncDll.EFGToECITime( date, 
                               (ctypes.c_double * 3)(*pos), 
                               (ctypes.c_double * 3)(*vel), 
                               topos, 
                               tovel )
    return np.array( topos ), np.array( tovel )

# -----------------------------------------------------------------------------
def teme_to_llh( pos, vel, date, AstroFuncDll ):
    llh  = (ctypes.c_double*3)()
    AstroFuncDll.XYZToLLHTime( date, 
                               (ctypes.c_double * 3)(*pos), 
                               llh )
    return np.array( llh )

# -----------------------------------------------------------------------------
def llh_to_teme( llh, date, AstroFuncDll ):
    pos  = (ctypes.c_double*3)()
    AstroFuncDll.LLHToXYZ( date, 
                               (ctypes.c_double * 3)(*llh), 
                               pos )
    return np.array( pos )

# =============================================================================
# from here on out, we use pandas to organize a bunch of potential conversions
# this is mostly setup to do sensor checks or geometry calcs, so you'll be 
# converting times a lot, and re-using them
# =============================================================================
def setup_times( ds50_utc : list[ float ], TimeFuncDll) :    # date in astrostandards epoch 
    '''
    this will convert a set of astrostandard formatted times in UTC
    to other time formats needed for conversion later
    this is often the first function run
    '''
    def convert_from_utc( d50u ) :
        d50et = TimeFuncDll.UTCToET( d50u )
        d50ut = TimeFuncDll.UTCToUT1( d50u )
        theta = TimeFuncDll.ThetaGrnwchFK5( d50ut )
            
        return {'ds50_utc' : d50u,
                'ds50_et'  : d50et,
                'ds50_ut1' : d50ut,
                'sidereal' : theta}
    return pd.DataFrame( [ convert_from_utc(D) for D in ds50_utc ] )

# -----------------------------------------------------------------------------
def times_to_llhsensor( times : pd.DataFrame,     # from setup_times
                     lat : float,              # latitude (degrees)
                     lon : float,              # longitude (degrees)
                     alt : float,              # altitude (above WGS84; km)
                     AstroFuncDll,
                     TimeFuncDll ):
    '''
    times must have the ds50_utc entry filled
    '''
    # constant longitude
    utc_dates      = times['ds50_utc']
    sensor_lon_rad = np.radians(lon)
    sen_eci_p      = (ctypes.c_double * 3)()
    sen_eci_v      = (ctypes.c_double * 3)()
    sen_efg        = (ctypes.c_double * 3)()
    _vel           = (ctypes.c_double * 3)(0,0,0)
    llh            = (ctypes.c_double * 3)( lat, lon, alt )
    AstroFuncDll.LLHToEFGPos( llh, sen_efg )
    def llhtoxyz( d50_utc ):
        theta = TimeFuncDll.ThetaGrnwchFK5( d50_utc )
        lst   = sensor_lon_rad + theta
        # AstroFuncDll.LLHToXYZTime( d50_utc, llh, sen_eci )
        AstroFuncDll.EFGToECI( theta, sen_efg, _vel, sen_eci_p, sen_eci_v )
        return {'lat' : float(llh[0]), 'lon' : float(llh[1]), 'alt' : float(llh[2]), 
                'theta'  : theta, 'lst' : lst,
                'teme_p' : list( sen_eci_p ),
                'teme_v' : list( sen_eci_v ) }
    return pd.concat( (times, pd.DataFrame( [llhtoxyz(D) for D in utc_dates ])), axis=1)

# -----------------------------------------------------------------------------
def topographic_calcs( observer_df : pd.DataFrame,      # must have times and teme locations filled in
                       target_df   : pd.DataFrame,      # must have tmies and teme locations filled in
                       AstroFuncDll ):  
    '''
    you must have local sidereal time (lst) in this frame (so even for space based,
    you need this value
    '''
    TOPO = helpers.astrostd_named_fields( AstroFuncDll, prefix='XA_TOPO_' )
    def getTopo( S, T ):
        AstroFuncDll.ECIToTopoComps( S['lst'], 
                                     S['lat'], 
                                     (ctypes.c_double * 3)(*S['teme_p']), 
                                     (ctypes.c_double * 3)(*T['teme_p']), 
                                     (ctypes.c_double * 3)(*T['teme_v']), TOPO.data )
        return TOPO.toDict()

    topo = pd.DataFrame( [getTopo(A,B) for A,B in zip( observer_df.to_dict('records'), target_df.to_dict('records')) ] )
    return pd.concat( (observer_df.add_suffix('_sensor'), target_df.add_suffix('_target'), topo ), axis=1 )

# -----------------------------------------------------------------------------
def get_celest( times : pd.DataFrame,      # from setup_times
                fcn   : callable ):       
    '''
    times must have the ds50_et entry filled
    '''
    sun_v  = (ctypes.c_double * 3)()
    sun_m  = ctypes.c_double()
    def getpos( D ): 
        fcn( D, sun_v, sun_m )
        return {'teme_p' : float(sun_m.value) * np.array(sun_v), 
               'teme_v' : np.zeros(3)}
    return pd.DataFrame( [getpos(X) for X in times['ds50_et'] ] )

# -----------------------------------------------------------------------------
def get_sun(   times: pd.DataFrame ):
    return get_celest( times, AstroFuncDll.CompSunPos )

# -----------------------------------------------------------------------------
def get_moon(   times: pd.DataFrame ):
    return get_celest( times, AstroFuncDll.CompMoonPos )

# -----------------------------------------------------------------------------
def annotate_teme_llh( teme_df : pd.DataFrame,
                       AstroFuncDll,
                       TimeFuncDll):
    dates = teme_df['ds50_utc']
    teme  = teme_df['teme_p'].tolist()
    _vel  = (ctypes.c_double * 3)()
    llh   = [teme_to_llh( P,_vel, D, AstroFuncDll) for P,D in zip( teme, dates ) ]
    teme_df['lat'] = [ X[0] for X in llh ]
    teme_df['lon'] = [ X[1] for X in llh ]
    teme_df['alt'] = [ X[2] for X in llh ]
    theta = [ TimeFuncDll.ThetaGrnwchFK5( D ) for D in dates ]
    teme_df['lst']   = [ A + B for A,B in zip( theta, teme_df['lon'] ) ]
    return teme_df

# =============================================================================
if __name__ == '__main__':
    from datetime import datetime, timedelta
    from load_utils import *
    import helpers
    init_all()

    NOW = datetime.utcnow()
    NOWDS50 = helpers.datetime_to_ds50( NOW , TimeFuncDll )
    
    print( teme_to_j2k( [7000,0,0], [0,6,0], NOWDS50, AstroFuncDll ) ) 
    print( j2k_to_teme( [7000,0,0], [0,6,0], NOWDS50, AstroFuncDll ) ) 
    print( teme_to_efg( [7000,0,0], [0,6,0], NOWDS50, AstroFuncDll ) ) 
    print( efg_to_teme( [7000,0,0], [0,6,0], NOWDS50, AstroFuncDll ) ) 
    print( teme_to_llh( [7000,0,0], [0,6,0], NOWDS50, AstroFuncDll ) ) 
    print( llh_to_teme( [0,0,0], NOWDS50, AstroFuncDll ) ) 

    # series of dates
    DATES       = [ NOW + timedelta(minutes=X) for X in range(0,1440,1) ]
    DATES_DS50  = [ helpers.datetime_to_ds50( X , TimeFuncDll ) for X in DATES ]

    # setup a dataframe with all the times we need
    times       = setup_times( DATES_DS50, TimeFuncDll )
    # annotate that frame with the sensor ECI position at the times
    sen         = times_to_llhsensor( times, 0, 0, 0, AstroFuncDll, TimeFuncDll)
    # make a fake target frame (we can use times_to_llhsensor for this too
    # as long as the sensor and target have teme_p, teme_v, lst, and lat filled out, this should work
    target      = times_to_llhsensor( times, 0, 0, 40000, AstroFuncDll, TimeFuncDll)
    # now calculate the look vectors
    look        = topographic_calcs( sen, target )
    print(look)
    print(look.iloc[0].to_dict())

    # a more realistic case: let's look at the sun from 0,0,0
    # now get the sun using the same times we calculated before
    sun         = get_sun( times )
    look        = topographic_calcs( sen, sun )
    print(look)

    # an example of looking from a space-based observer to another
    # for this one, we need to manually fill in the teme_p and teme_v values
    fake_eci   = times.copy()
    fake_eci['teme_p'] = [ np.array([7000,0,0]) for _ in range( len(fake_eci) )]
    fake_eci['teme_v'] = [ np.array([0,7,0]) for _ in range( len(fake_eci) )]
    fake_eci           = annotate_teme_llh( fake_eci, AstroFuncDll, TimeFuncDll )
    look               = topographic_calcs( fake_eci, sun )
    print(look)
    print(look.iloc[0].to_dict())
    
