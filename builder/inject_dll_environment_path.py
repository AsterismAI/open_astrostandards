# -----------------------------------------------------------------------------------------------------
# Kerry N. Wood
# March 14, 2023
# This script is a helper to inject some new path data into the reformatted wrapper code:
# -----------------------------------------------------------------------------------------------------
import os
import sys
import re

def check_os_import( lines ):
    def import_check(L):
        re.search(r'import *os ',L)
    return any( [ import_check(L) for L in lines ] )


def inject_os_import( lines ):
    rv = []
    for L in lines:
        L = re.sub('import *sys','import sys\nimport os\n',L)
        rv.append(L)
    return rv


def inject_library_searchdir( lines ):
    rv = []
    for L in lines:
        if re.search('^add_library_search_dirs', L):
            rv.append( "add_library_search_dirs([ os.environ['ASTROSTANDARDS_LIBDIR'] ] )\n" )
        else: 
            rv.append(L)
    return rv


# =====================================================================================================
# main
# =====================================================================================================
if __name__ == '__main__':
    try: 
        with open( sys.argv[1], 'r') as F: lines = F.readlines()
    except: sys.exit()
    print('Injecting DLL search path / environment var in {}'.format( sys.argv[1] ) )

    if check_os_import( lines ): 
        pass
    else: 
        lines = inject_os_import( lines )

    lines = inject_library_searchdir( lines )
    with open( sys.argv[1], 'w') as F: F.write( ''.join(lines) )
