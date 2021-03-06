

#   This is useful for accurate memory profiling because getsizeof doesn't peer into nested objects

import sys
def show_sizeof(x,level=0):
    "Prints type, byte size, and original value"
    print "\t"*level,x.__class__, sys.getsizeof(x), x
    if hasattr(x,'__iter__'):
        if hasattr(x,'items'):
            for xx in x.items():
                show_sizeof(xx,level+1)
        else:
            for xx in x:
                show_sizeof(xx,level+1)

