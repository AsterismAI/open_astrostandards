from public_astrostandards import public_astrostandards as PA

# init the astrostandards
print('\nInitializing the astrostandards\n')
ptr = PA.init_all( logfile='test.log' ) 

# test TLE
L1 = '1 25544U 98067A   24365.67842578  .00026430  00000-0  46140-3 0  9990'
L2 = '2 25544  51.6404  61.8250 0005853  25.4579 117.0387 15.50482079489028'

# load the TLE
tleid = PA.TleDll.TleAddSatFrLines( 
    PA.Cstr( L1, 512 ),
    PA.Cstr( L2, 512 )
    )
print('TLE id inside astrostandards is {}'.format( tleid ) )
assert tleid > 0

# init the SGP4 prop
# you need the license file to be readable (easiest is in current directory) for this to work
sgp4 = PA.Sgp4PropDll.Sgp4InitSat( tleid )
print('SGP4 init returned : {}'.format( sgp4 ) )
assert sgp4 == 0

# now lets propagate using the "minutes since epoch" function
# look at the C headers to get good documentation on available functions (e.g.Sgp4PropDll.h)

# data holders for OUTPUT
ds50 = PA.ctypes.c_double() 
pos  = (PA.ctypes.c_double * 3)()
vel  = (PA.ctypes.c_double * 3)()
llh  = (PA.ctypes.c_double * 3)()
date = PA.Cstr('',19)       # < -- C-string, length 19, initially blank

# loop over minutes to propagate (from epoch)
minutes = range( 0, 1440, 10 )
for M in minutes:
    PA.Sgp4PropDll.Sgp4PropMse( 
        tleid,      # <-- input: tleid
        M,          # <-- input: minutes from epoch
        ds50,       # <-- output : days since 1950 of this point (auto-calced from epoch and minutes)
        pos,        # <-- output : position (TEME)
        vel,        # <-- output : velocity (TEME)
        llh)        # <-- output : lat/long/alt

    # convert that 1950 date to a more readable format using astrostandards
    PA.TimeFuncDll.UTCToDTG19( ds50, date )   # <-- pass in the date string holder
    print('{}'.format( date.value.decode('utf-8') ) )
    print('POS : {}'.format( list(pos) ) )
    print('VEL : {}'.format( list(vel) ) )
    print('LLH : {}'.format( list(llh) ) )
    print()
