'''
Kerry N. Wood

This will take the ctypesgen output'd files and inject new paths for the libraries.  It assumes the mapping of files below,
including the weird <name>Dll.py format of the python harness
'''


import sys
import re
import os

mappings = '''AstroFuncDll.py,libastrofunc.so,AstroFunc.dll
AofDll.py,libaof.so,Aof.dll
BatchDCDll.py,libbatchdc.so,BatchDC.dll
BamDll.py,libbam.so,Bam.dll
ComboDll.py,libcombo.so,Combo.dll
DllMainDll.py,libdllmain.so,DllMain.dll
ElCompDll.py,libelcomp.so, ElComp.dll
ElOpsDll.py,libelops.so,ElOps.dll
EnvConstDll.py,libenvconst.so,EnvConst.dll
ExtEphemDll.py,libextephem.so,ExtEphem.dll
FovDll.py,libfov.so,Fov.dll
ObsDll.py,libobs.so,Obs.dll
ObsOpsDll.py,libobsops.so,ObsOps.dll
RotasDll.py,librotas.so,Rotas.dll
LamodDll.py,liblamod.so,Lamod.dll
SatStateDll.py,libsatstate.so,SatState.dll
SaasDll.py,libsaas.so,Saas.dll
SensorDll.py,libsensor.so,Sensor.dll
Sgp4PropDll.py,libsgp4prop.so,Sgp4Prop.dll
SpPropDll.py,libspprop.so,SpProp.dll
SpVecDll.py,libspvec.so,SpVec.dll
TimeFuncDll.py,libtimefunc.so,TimeFunc.dll
TleDll.py,libtle.so,Tle.dll
VcmDll.py,libvcm.so,Vcm.dll'''

mapdict = {}
for m in mappings.split('\n'):
    py,so,dll = m.strip().split(',')
    mapdict[py] = {}
    mapdict[py]['win']   = dll
    mapdict[py]['linux'] = so

if len(sys.argv) < 3: 
    print( '{} <input> <output>'.format( sys.argv[0] ) ) 
    sys.exit(1)

# check that the input file exists
assert os.path.isfile( sys.argv[1] )

inp = sys.argv[1]
out = sys.argv[2]

filename = os.path.basename( inp )

# get the mapping 
assert filename in mapdict
this_map = mapdict[ filename ]

print()
print('-' * 100 )
print('Found {} in the mapdict'.format( filename ) )
print('-' * 100 )

# load the file
with open( inp, 'r' ) as F: original = F.readlines()

newl = [ line.replace( this_map['linux'], this_map['win'] ) for line in original ]

with open( out, 'w') as F: 
    for l in newl : F.write(l)

