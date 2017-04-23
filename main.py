import numpy as np
from bitstring import BitArray

def foo():
    print 'foo function called'

def bar():
    print 'bar function called'

dispatch = {
    'foo':[foo,2,[(-3,3),(2,2)]],
    'bar':[bar,[(3,3)]]
}

if __name__ =='__main__':

    #print len(dispatch['bar'][1])
    # s='0101010101'
    # for i in range(0,5):
    #     print s[i*2:(i+1)*2]
    min = -2
    max = 2
    precision = 5
    SUBINTERVALS = (max-min)*(10**precision)

    str_len = int(np.ceil(np.log2(SUBINTERVALS)))
    print str_len

    bit = np.random.randint(0,2,str_len)
    print bit
    bitstr = ''.join(str(x) for x in bit)
    b = BitArray(bin=bitstr)
    print round(min + (b.uint*1.0*(max-min))/(2.0**str_len-1),precision)


