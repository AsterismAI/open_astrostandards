import os
import glob
import sys
import struct

# the actual reformatter
from include_reformatter import funcline

def get32or64(): return struct.calcsize("P") * 8

def reformatLines( lines ): return [funcline(L) for L in lines]
def reformatFile( FN ):
    with open(FN,'r') as F: lines = F.readlines()
    return lines, reformatLines( lines )

def starts_with_new( fn ):
    base = os.path.basename(fn)
    return base[0:4] == 'new_'

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////////////////
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    print('-'*100)
    print("!!!! NOTE: this will create the rewritten headers *and* the Python files in the same directory as the includes")
    print('-> there are all sorts of circular dependencies, so do NOT try and change this.')
    print('-> just create those python headers, and move the files when you are done')
    print()
    print('-> the PY files should contain explicit constants.')
    print('-> if they do not, check the .err files')
    print('-'*100)
    parser.add_argument('--headers', type=str, required=True,help='directory with AstroStandards .h files' )
    parser.add_argument('--libraries', type=str, required=True, help="directory containing DLL's or .so's")
    args = parser.parse_args()
    # set the parameters
    if os.path.isdir( args.headers ): dothdir = args.headers
    if os.path.isdir( args.libraries): libdir = args.libraries
    else: 
        print('Libraries entry does not seem to be a directory') 
        sys.exit(1)

    # =============================================================================================
    # guess the library extension
    if os.name == 'nt': 
        print('Detected WINDOWS, setting library extension to dll')
        libext = '.dll'
    else:
        print('Detected LINUX, setting library extension to so')
        libext = '.so'

    print('HINT: I detected your Python is {} bit'.format( get32or64() ) )
    print()
    print()

    # =============================================================================================
    # Step 1: build new header files that we could use for ctypesgen
    print('*'*100)
    print('Step 1: reformatting the .h files so that ctypesgen can eat em')
    print('*'*100)
    doth =  glob.glob( os.path.join( dothdir, '*.h' ) ) 
    doth = list(filter(lambda F: not starts_with_new(F), doth ) )
    headerdict = {}
    for fn in doth:
        print('\tWorking {}    '.format( fn ), end='' )
        oldlines, newlines = reformatFile( fn )
        print('{} original lines, {} new lines'.format( len(oldlines),len(newlines) ) )
        justfile = os.path.basename( fn )
        #justdir  = os.path.abspath( os.path.dirname(fn) )
        justdir  = os.path.dirname( fn )
        newfile  = os.path.join( justdir, "new_" + justfile )
        headerdict[ justfile ] = newfile
        print('\t ...  exporting new file to {}'.format( newfile ) )
        with open( newfile,'w' ) as F: F.write( "\n".join( newlines)  )

    # =============================================================================================
    # Step 2: find the DLL's that match the header file name
    lib  = glob.glob( os.path.join( libdir, '*' + libext ) )
    # make a dictionary of the libraries we found
    libdict = {}
    for l in lib:
        ln = os.path.basename(l)
        ld = os.path.dirname(l) 
        #ld = os.path.abspath( os.path.dirname(l) )
        noext = ln.replace(libext,'')
        if libext == '.so': noext = noext.replace('lib','')
        libdict[noext] = os.path.join( ld, ln )

    print('*'*100)
    print('Step 2: finding Dlls')
    print('\t looking in {}'.format( os.path.join( libdir, '*' + libext ) ) )
    print('\t Found : {}'.format( list(libdict.keys() ) )) 
    print('*'*100)
 
    print()
    print('*'*100)
    print('Step 3: generate cytpesgen commands... you should run these!')
    print('\t writing all these to runme.sh, either run that or copy commands')
    print('*'*100)

    print()
    print('*'*100)
    print('Step 4: use the inject_dll script to re-set the DLL search path to the environment var')
    print('\t this works best in a FOR loop')
    print('\t for F in *.py do python builder/inject_dll_environment_path.py $F')
    print('*'*100)

    # keep track of the library directories so we can set environment
    libpath    = []
    pythonpath = []
    with open('runme.sh','w') as F:
        for k in headerdict.keys():
            newfile = headerdict[k]
            noext   = k.replace('.h','')
            newdir  = os.path.dirname( newfile ) 
            #newdir  = os.path.abspath( os.path.dirname( newfile ) )
            newpy   = os.path.join( newdir, noext + '.py' )
            libentry = list(filter( lambda l: l.lower() in k.lower(), libdict.keys() ) )
            libentry = sorted( libentry, key=lambda X: len(X),reverse=True)
            pythonpath.append( newdir )
            if len(libentry) > 0:
                # if we find a corresponding library, encode that
                libfile = os.path.basename( libdict[libentry[0]] )
                libdir  = os.path.abspath(os.path.dirname(libfile))
                libpath.append( libdir) # we'll keep this list
                outs = 'ctypesgen -I {incdir} --compile-libdir={libdir} -l {libfile} {modname} -o {outname} 2>{modname}.err'.format(
                        libfile = repr(libfile),
                        incdir  = repr(newdir),
                        libdir  = repr(ld),
                        modname = repr(newfile),
                        outname = repr(newpy)  ) 

            else:
                # just encode the library directory and build the harness
                outs = 'ctypesgen -I {incdir} {modname} -o {outname} 2>{modname}.err'.format(
                        incdir  = repr(newdir),
                        modname =newfile, 
                        outname = repr(newpy)  ) 
            #F.write('echo "{}"\n'.format( outs ))
            F.write("echo '{}'\n".format( outs ) )
            F.write( outs  + '\n' )

        libpath    = list( set(libpath) )
        pythonpath = list( set(pythonpath) )
        ldpath_S = 'export LD_LIBRARY_PATH={}'.format( ":".join(libpath) )
        pypath_S = 'export PYTHONPATH={}'.format( ":".join(pythonpath) ) 
        F.write('\n\n')
        F.write( '{}\n'.format( ldpath_S ) )
        F.write( '{}\n'.format( pypath_S ) )
        print( ldpath_S )
        print( pypath_S )
        print('\n\n')

