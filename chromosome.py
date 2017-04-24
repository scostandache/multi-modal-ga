import numpy as np
import itertools
from bitstring import BitArray
import copy

class Parameter(object):
    #class to represent a parameter in a chromosome's fitness function


    def __init__(self,limit,precision):

        """The class constructor
        
        Args:
            limit: a dictionary containing the 'min' and the 'max' values that a float value can have
            precision: precision of the float value for an object
        
        """
        N = (limit['max'] - limit['min']) * (10 ** precision)  # number of subintervals - depends on the precision we need
        bitarr_len = int(np.ceil(np.log2(N))) #number of needed bits for representing a parameter

        BITS = np.random.randint(0,2,bitarr_len) #generate an array of randomly generated 0's and 1's
        bit_repr = ''.join(str(x) for x in BITS) #concatenate into a string

        decimal_aprox = BitArray(bin=bit_repr).uint * 1.0 #get a decimal aproximation of our bitstring
        float_repr = round(limit['min'] + (decimal_aprox*(limit['max']-limit['min']))/(2.0**bitarr_len-1),precision) #get the float number

        self.__bit_repr = bit_repr
        self.__float_repr = float_repr
        self.__BITS = BITS
        self.__bitarr_len = bitarr_len
        self.__limit = limit
        self.__precision = precision

    @property
    def float_repr(self):
        #get the float representation of the parameter
        return self.__float_repr

    @property
    def bit_repr(self):
        #get the bitstring representation of the parameter
        return self.__bit_repr

    @property
    def bitarr(self):
        #get the parameter representation under an array of bits
        return self.__BITS

    @property
    def bit_len(self):
        #get the length of bit representation
        return self.__bitarr_len

    def recalculate(self):
        #will recalculate the value of the parameter after a genetic operation; we'll use the same operations as in the initial float calculation
        self.__bit_repr = ''.join(str(x) for x in self.__BITS)
        decimal_aprox = BitArray(bin=self.__bit_repr).uint * 1.0 #get a decimal aproximation of our bitstring
        self.__float_repr = round(self.__limit['min'] + (decimal_aprox*(self.__limit['max']-self.__limit['min']))/(2.0**self.__bitarr_len-1),self.__precision)

    def mutate(self):
        #perform a mutation on a random bit
        mut_idx = np.random.random_integers(0, self.bit_len - 1)
        self.__BITS[mut_idx] = int(not self.__BITS[mut_idx]) #negate a bit at a random position, in the bit array
        self.recalculate()
        print 'parameter mutation'


class Chromosome(object):
    #class to represent a chromosome in population

    def __init__(self,param_no,LIMITS,precision):

        """The class constructor

        Args:
            LIMITS = an array of limit dictionaries. In some cases a function needs a limit for each parameter, wether in others all of them have the same limit. 
                    In this case the array will contain only one element.
            precision: precision for float values of the parameters

        """

        if(param_no == len(LIMITS)): #we have a case when each function parameter has it's own limit
            self.PARAMS = [Parameter(limit,precision) for limit in LIMITS] #we create a parameter for each limit
        else:
            self.PARAMS = [Parameter(LIMITS[0], precision) for _ in xrange(param_no)] #all of the parameters will be within the same limit (LIMITS[0])
        #*** an alternative would be to verify if the LIMITS is an array or a dictionary. if it's an array -> case 1, else case 2, without using LIMITS[0]

        self.__param_no = param_no

    @property
    def params_raw(self):
        #return the array of parameter objects
        return self.PARAMS

    @property
    def params_bitstring(self):
        #get the array of parameters in bitstring form
        return [param.bit_repr for param in self.PARAMS]

    @property
    def params_float(self):
        #get the array of parameters in float form
        return [param.float_repr for param in self.PARAMS]

    @property
    def bitstring(self):
        #return a string consisting of the contatenated bitstring parameters
        return ''.join([param.bit_repr for param in self.PARAMS])

    @property
    def bitarr(self):
        #return an array consisting of the concatenated parameters, under arrays of bits
        return list(itertools.chain(*[p.bitarr for p in self.PARAMS]))

    def mutate(self):
        #mutate a randomly chosen parameter
        mut_idx = np.random.random_integers(0, self.__param_no - 1)
        self.PARAMS[mut_idx].mutate()

    def crossover(self,parent):
        first_desc = copy.deepcopy(self)
        second_desc = copy.deepcopy(parent)
        cut_point = np.random.random_integers(0,len(self.PARAMS))
        print cut_point

        for i in range(cut_point):
            first_desc.PARAMS[i],second_desc.PARAMS[i] = second_desc.PARAMS[i],first_desc.PARAMS[i]
        return first_desc,second_desc


if __name__ == '__main__':

    # POPULATION =[]

    c1 = Chromosome(param_no=5,LIMITS=[{'min':-3,'max':3}],precision=5)
    c2 = Chromosome(param_no=5, LIMITS=[{'min': -3, 'max': 3}], precision=5)
    # mut_idx = np.random.random_integers(0,len(c_bitarr)-1)

    # c_bitarr[mut_idx] = int(not c_bitarr[mut_idx])
    #
    # print c_bitarr
    # c_bitstr = c.bitstring
    #
    # chosen_param = c.PARAMS[0]
    #
    # print chosen_param.bitarr
    # print chosen_param.float_repr
    #
    # chosen_param.bitarr[5] = int(not chosen_param.bitarr[5])

    # params = c.params_raw
    #
    # print c.params_float
    #
    # for p in params:
    #      p.bitarr[5] = int(not p.bitarr[5])
    #     # p.recalculate()
    #     #p.mutate()
    #
    #
    #
    # c.mutate()

    print c1.params_float
    print c2.params_float
    print ""

    c1.crossover(c2)


    print c1.params_float
    print c2.params_float



