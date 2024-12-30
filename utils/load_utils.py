import ctypes
import sys
import DllMainDll
import TimeFuncDll
import EnvConstDll
import AstroFuncDll
import TleDll
import SpVecDll
import VcmDll
import ExtEphemDll
import Sgp4PropDll
#import SatStateDll # <- included in distro, but needs SpProp to work
import SensorDll
import ObsDll
import ElOpsDll
import RotasDll
import BatchDCDll

def get_last_errmsg( ):
    stbuf = ctypes.create_string_buffer( 128 )
    DllMainDll.GetLastErrMsg( stbuf )
    return stbuf.value.decode('utf-8')

def Cstr( S, slen=128 ):
    stbuf = ctypes.create_string_buffer( slen )
    stbuf.value = S.encode()
    return stbuf

# in the order that they should be loaded
INIT_LIST = [ 
    ('EnvConstDll', EnvConstDll.EnvInit),
    ('TimeFuncDll', TimeFuncDll.TimeFuncInit),
    ('AstroFuncDll', AstroFuncDll.AstroFuncInit),
    ('TleDll', TleDll.TleInit),
    ('SpVecDll', SpVecDll.SpVecInit),
    ('VcmDll', VcmDll.VcmInit),
    ('ExtEphemDll', ExtEphemDll.ExtEphInit),
    ('Sgp4PropDll', Sgp4PropDll.Sgp4Init),
    ('ElOpsDll', ElOpsDll.ElOpsInit),
    #('SatStateDll', SatStateDll.SatStateInit),
    ('SensorDll', SensorDll.SensorInit),
    ('ObsDll',ObsDll.ObsInit)
    ]

def init_wrapper( name, fcn, ptr, verbose=True ):
    rv = fcn(ptr) 
    if verbose : print( '{:20} : {}'.format( name, rv ) )

# DEPRECATED
#def get_loaded( ):
#    stbuf = ctypes.create_string_buffer( 512 )
#    DllMainDll.GetInitDllNames( stbuf )
#    return stbuf.value.rstrip() 

def init_all( logfile='aslog.txt', verbose=True ):
    # the first DllMain must be init'd separetely
    ptr = DllMainDll.DllMainInit()
    if verbose: print('{:20} : {}'.format( 'DllMainInit', ptr ))

    # do we want a logfile?
    if logfile: DllMainDll.OpenLogFile( Cstr( logfile, 512) )

    # load all the libraries
    for nm, fcn in INIT_LIST: init_wrapper( nm, fcn, ptr, verbose )

    # DEPRECATED
    #print('Loaded: {}'.format( get_loaded() ) )
    return ptr

# WARNING
def time_warning():
    sys.stderr.write('*'*100 +'\n')
    sys.stderr.write('Remember when converting dates/times that you should use Julian dates to avoid leap second issues\n')
    sys.stderr.write('   helpers.DS50EPOCH + <days_since_50_float> * u.day ---> WRONG\n')
    sys.stderr.write("   astropy.time.Time( helpers.DS50EPOCH.jd + <days_since_50_float> , format='jd') ---> CORRECT\n")
    sys.stderr.write('*'*100 + '\n')

# =====================================================================================================
if __name__ == "__main__":
    # get a version string from the libraries
    s128 = Cstr('' , 128 )
    Sgp4PropDll.Sgp4GetInfo( s128 )
    print('\n----------------------------------------- VERSION -----------------------------------------')
    print(s128.value)
    print('----------------------------------------- VERSION -----------------------------------------\n')

    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    # some dates checks
    #   use the Astrostandards to get a 1950 epoch date
    #   manually calculate it as a Python datetime difference
    #   see how different they are
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    from datetime import datetime, timedelta
    ptr = init_all()
    now = datetime.utcnow()
    ds = now.strftime('%y%j%H%M%S.%f')[:-3]

    x = TimeFuncDll.DTGToUTC(  Cstr( ds,20 ) )
    epoch = datetime.strptime( '1949-12-31T00:00:00', "%Y-%m-%dT%H:%M:%S")

    def get_days_between(datePast, dateFuture):
        difference = dateFuture - datePast
        return difference.total_seconds() / 86400.
        #return difference.total_seconds() / timedelta(days=1).total_seconds()

    print('Now               : {}'.format(now.isoformat()) )
    print('Test date string  : {}'.format(ds) )
    print('AstroStd answer   : {}'.format(x) )

    print('Python answer     : {}'.format( get_days_between( epoch, now ) ) )
    print('Difference in sec : {}'.format(  86400. * (x - get_days_between( epoch, now ) ) ) )
