'''
Kerry N. Wood

This will take the ctypesgen output'd files and inject new paths for the libraries.  It assumes the mapping of files below,
including the weird <name>Dll.py format of the python harness
'''


import sys
import re
import os

mappings = '''AstroFuncDll.py,libastrofunc.so,AstroFunc.dll
BatchDCDll.py,libbatchdc.so,BatchDC.dll
DllMainDll.py,libdllmain.so,DllMain.dll
ElCompDll.py,libelcomp.so, ElComp.dll
EnvConstDll.py,libenvconst.so,EnvConst.dll
ExtEphemDll.py,libextephem.so,ExtEphem.dll
ObsDll.py,libobs.so,Obs.dll
ObsOpsDll.py,libobsops.so,ObsOps.dll
RotasDll.py,librotas.so,Rotas.dll
LamodDll.py,liblamod.so,Lamod.dll
SatStateDll.py,libsatstate.so,SatState.dll
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


'''
the lines we need to replace are:
_libdirs = ['/hostmount/JHUAPL/SOFTWARE/asctypes/Lib']
# End loader
add_library_search_dirs(['/hostmount/JHUAPL/SOFTWARE/asctypes/Lib'])
# Begin libraries
_libs["/hostmount/JHUAPL/SOFTWARE/asctypes/Lib/libastrofunc.so"] = load_library("/hostmount/JHUAPL/SOFTWARE/asctypes/Lib/libastrofunc.so")
'''

# libdir search
l1 = re.compile('\_libdirs.*=')
# libs line
l2 = re.compile('\_libs.*\[.*load_library')
# add_library_search...
l3 = re.compile('add_library_search_dirs.*')

if __name__ == "__main__":
    # check for the dll / library directory
    if len(sys.argv) < 3 or not os.path.isdir( sys.argv[1] ):
        print('{} <new library directory> <Python harness file>'.format( sys.argv[0] ) )
        sys.exit(1)
    else: newpath = os.path.abspath( sys.argv[1]  )
    print(newpath)
    
    # read in the Python harness file (e.g. AstroFuncDll.py)
    try: 
        with open(sys.argv[2], 'r' ) as F: lines = F.readlines()
    except:
        print('could not read {}'.format( sys.argv[2] ))
        sys.exit()
        
    # get the type of system (for DLL vs so files)
    if os.name == 'nt' : mytype = 'win'
    else: mytype = 'linux'
        
    # this file
    thisfn = os.path.basename( sys.argv[2] )
    try: libmap = mapdict[ thisfn ][mytype] 
    except Exception as e:
        print('Could not find the library mapping for {} // exception: {}'.format( sys.argv[2], str(e)) )
        sys.exit(1)
    
    # fix the lines we want to fix
    outS = ''
    for l in lines:
        if l1.search(l): 
            outS += "# OLD {}\n".format(l.strip() )
            outS += "_libdirs = [{}]\n".format( repr(newpath) )
            continue
        if l2.search(l):
            outS += "# OLD {}\n".format(l.strip())  
            outS += '_libs[{}] = load_library({})\n'.format( repr(libmap),
                                                        repr(os.path.join(newpath, libmap) ) ) 
            continue
        if l3.search(l): 
            continue
        outS +=  l
            
    with open( sys.argv[2],'w') as F: F.write(outS)
