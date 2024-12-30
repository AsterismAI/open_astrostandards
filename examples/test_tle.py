# import the load_utils helper
import load_utils
import helpers

# init the astrostandards
print('\nInitializing the astrostandards\n')
ptr = load_utils.init_all( logfile='test.log' ) 

# test TLE
L1 = '1 25544U 98067A   24365.67842578  .00026430  00000-0  46140-3 0  9990'
L2 = '2 25544  51.6404  61.8250 0005853  25.4579 117.0387 15.50482079489028'

# load the TLE
tleid = load_utils.TleDll.TleAddSatFrLines( 
    load_utils.Cstr( L1, 512 ),
    load_utils.Cstr( L2, 512 )
    )
print('TLE id inside astrostandards is {}'.format( tleid ) )
assert tleid > 0

# -----------------------------------------------------------------------------------------------------
# use the '...ToArray..' methods to see the internals of the TLE

#672 // Retrieves TLE data and stored it in the passing parameters
#673 // satKey             The satellite's unique key (in-Long)
#674 // xa_tle             Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (out-Double[64])
#675 // xs_tle             Output string that contains all TLE's text fields, see XS_TLE_? for column arrangement (out-Character[512])
#676 // returns 0 if all values are retrieved successfully, non-0 if there is an error
#677 typedef int (STDCALL *fnPtrTleDataToArray)(__int64 satKey, double xa_tle[64], char xs_tle[512]);

# get a holder for the XA_TLE_ fields.  These will be pulled from the headers and put into a holder
XA_TLE = helpers.astrostd_named_fields( load_utils.TleDll, prefix='XA_TLE_')
UNUSED = load_utils.Cstr('',512)  

# pass this data pointer into the AstroStandards function (the class will let you parse / modify afterwards)
assert 0 == load_utils.TleDll.TleDataToArray( tleid, XA_TLE.data, UNUSED )

# you can now see this as a dict
print( XA_TLE.toDict() )

# or you can modify like a dict (if you wanted to re-inject these data)
XA_TLE['XA_TLE_SATNUM'] = 99999
print( XA_TLE.toDict() )
