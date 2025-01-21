from datetime import datetime,  timedelta

# epochs to help us convert from and to Julian... (rather than a library)
_J2K_dt = datetime(year=2000, month=1, day=1, hour=12)
_J2K_jd = 2451545.0
# --------------------------------------------------------------------------------------------------------
def dt2julian( DT : datetime ):
    del_d = ( DT - _J2K_dt ).total_seconds() / 86400
    return _J2K_jd + del_d

# --------------------------------------------------------------------------------------------------------
def julian2dt( jd : float ):
    return _J2K_dt + timedelta( days= jd - _J2K_jd )