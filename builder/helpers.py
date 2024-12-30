class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2

def build_lookup( dll, prefix='XA_SPVEC' ):
    '''
    helper routine to look inside a DLL for specific constant headers
    the DLL's use fixed width fields for a lot of data, and this pulls it out

    Ex:
       lookupdict = build_lookup( SpVecDll, prefix='XA_SPVEC')l
    '''
    ids = list( filter( lambda X: prefix in X , dir(dll) ) )
    prs = sorted( [ (getattr(dll,X),X) for X in ids ] )
    rv = TwoWayDict()
    for P in prs: rv[P[0]] = P[1]
    return rv

def apply_lookup_to_array( lookup, array, maxv=512 ):
    '''
    given a lookup dictionary and a pulled array, make a dictionary
    '''
    rv = {}
    for i in range( maxv ):
        if i in lookup: rv[ lookup[i] ] = array[i]
    return rv
