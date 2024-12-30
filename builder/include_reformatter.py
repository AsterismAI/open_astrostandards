import sys
import re

funcptr = re.compile('.* (\(STDCALL.*? \*fnPtr.*?\))')

def funcline( S ):
    '''
    take a line like:
        typedef int (STDCALL *fnPtrOpenLogFile)(char fileName[512]);
    and make it:
        int OpenLogFile(char fileName);

    this allows ctypesgen to build the right prototype (as opposed to seeing the function as a variable because of the typedef)
    '''

    s = S.strip()

    if s.lstrip().rstrip().split(" ") == ['static', 'const', 'int'] : return '' 

    if '=' in s and s.lstrip()[0] != '/': 
        ''' replace the constant int's with #defines that ctypesgen can handle'''
        news = s.replace('=',' ').replace(',','').replace(';','')
        #return 'const int {}'.format(news)
        return '#define {}'.format(news)

    # reformat the functions
    if 'fnPtr' in s:
        '''reformat the function pointers to ctypesgen-capable formats'''
        try :  
            mtch = funcptr.search( s )
            tspan   = mtch.span()
        except: 
            return '// {} // (commented out pointer)'.format(s)
        pointer = s[ tspan[0] : tspan[-1] ]
        rest    = s[ tspan[-1] : ]
        newptr = pointer.replace('(','').replace('STDCALL','').replace(')','').replace('fnPtr','').replace('typedef','').replace('*','').lstrip().rstrip()
        rv = "{}{}".format(newptr,rest)
        return rv

    return s

if __name__ == "__main__":
    try: 
        with open(sys.argv[1], 'r' ) as F: lines = F.readlines()
    except:
        print()
        print("=" * 100)
        print('{} <include file>'.format(sys.argv[0]))
        print("=" * 100)
        print()
        sys.exit(1)

    for l in lines: 
        print(funcline(l))
