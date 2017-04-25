import numpy as np
from bitstring import BitArray
from population import Population


def foo():
    print 'foo function called'

def bar():
    print 'bar function called'

dispatch = {
    'foo':[foo,2,[(-3,3),(2,2)]],
    'bar':[bar,[(3,3)]]
}

if __name__ =='__main__':
    x=2