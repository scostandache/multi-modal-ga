import numpy as np
import itertools
from bitstring import BitArray
import copy


class Parameter(object):
    # class to represent a parameter in a chromosome's fitness function


    def __init__(self, limit, precision):
        """The class constructor
        
        :param limit:  a dictionary containing the 'min' and the 'max' values that a float value can have
        :param precision: precision of the float value for an object
        
        """
        # calculate number of subintervals - depends on the precision we need
        N = (limit['max'] - limit['min']) * (10 ** precision)

        # number of needed bits for representing a parameter
        bitrepr_len = int(np.ceil(np.log2(N)))

        # generate an array of randomly generated 0's and 1's
        bitarr = np.array(np.random.randint(0, 2, bitrepr_len))

        # concatenate into a string
        bit_repr = ''.join(str(x) for x in bitarr)

        # get a decimal aproximation of our bitstring
        decimal_aprox = BitArray(bin=bit_repr).uint * 1.0

        # get the float representation
        float_repr = round(limit['min'] +
                           (decimal_aprox * (limit['max'] - limit['min']))
                           / (2.0 ** bitrepr_len - 1), precision)

        self.__bit_repr = bit_repr
        self.__float_repr = float_repr
        self.__bitarr = bitarr
        self.__bitrepr_len = bitrepr_len
        self.__limit = limit
        self.__precision = precision

    @property
    def float_repr(self):
        # get the float representation of the parameter
        return self.__float_repr

    @property
    def bit_repr(self):
        # get the bitstring representation of the parameter
        return self.__bit_repr

    @property
    def bitarr(self):
        # get the parameter representation as an array of bits
        return self.__bitarr

    @property
    def bit_len(self):
        # get the length of bit representation
        return self.__bitrepr_len

    @float_repr.setter
    def float_repr(self, f_number):
        # set the new float value of the parameter
        self.__float_repr = f_number

    @bitarr.setter
    def bitarr(self, new_bitarr):
        # set the new bitarray representation of the parameter
        self.__bitarr = copy.deepcopy(new_bitarr)

    def recalculate(self):
        # will recalculate the value of the parameter after a genetic operation;
        # we'll use the same operations as in the initial float calculation

        self.__bit_repr = ''.join(str(x) for x in self.__bitarr)
        # get a decimal aproximation of our bitstring
        decimal_aprox = BitArray(bin=self.__bit_repr).uint * 1.0

        # recalculate the float value
        self.__float_repr = round(self.__limit['min'] +
                                  (decimal_aprox * (self.__limit['max'] - self.__limit['min'])) /
                                  (2.0 ** self.__bitrepr_len - 1), self.__precision)

    def mutate(self):
        # perform a mutation on a random bit
        mut_idx = np.random.random_integers(0, self.bit_len - 1)

        # negate a bit at a random position, in the bit array
        self.__bitarr[mut_idx] = int(not self.__bitarr[mut_idx])

        self.recalculate()


class Chromosome(object):
    # class to represent a chromosome in population

    def __init__(self, param_no, LIMITS, precision):

        """The class constructor
        
        :param param_no: number of parameters in a chromosome
        :param LIMITS: a dictionary, or an array of dictionaries 
        containing limits, in format {'min':value,'max':value}.
        In some cases a function needs a limit for each parameter,
        while in others all of them have the same limit.
        In those cases the array will contain only one element.
        :param precision: precision for float values of the parameters
        """

        # if we have a case when each function parameter has it's own limit
        if param_no == len(LIMITS):
            # we create a parameter for each limit
            self.PARAMS = [Parameter(limit, precision) for limit in LIMITS]
        else:
            # all of the parameters will be within the same limit
            self.PARAMS = [Parameter(LIMITS[0], precision) for _ in xrange(param_no)]
        # *** an alternative would be to verify if the LIMITS is an array or a dictionary.
        # if it's an array -> case 1, else case 2, without using LIMITS[0]

        self.__param_no = param_no
        self.__bitarr = np.array(list(itertools.chain(*[p.bitarr for p in self.PARAMS])))
        self.__precision = precision

    @property
    def params_raw(self):
        # return the array of parameter objects
        return self.PARAMS

    @property
    def params_bitstring(self):
        # get the array of parameters in bitstring form
        return [param.bit_repr for param in self.PARAMS]

    @property
    def params_float(self):
        # get the array of parameters in float form
        return [param.float_repr for param in self.PARAMS]

    @property
    def bitstring(self):
        # return a string consisting of the contatenated bitstring parameters
        return ''.join([param.bit_repr for param in self.PARAMS])

    @property
    def bitarr(self):
        # return the bitarray
        return self.__bitarr
        # return list(itertools.chain(*[p.bitarr for p in self.PARAMS]))

    @bitarr.setter
    def bitarr(self, new_bitarr):
        # set a new bit array
        self.__bitarr = copy.deepcopy(new_bitarr)

    @property
    def fitness(self):
        # return the fitness of the chromosome
        return self.__fitness

    @fitness.setter
    def fitness(self, new_fitness):
        # set the fitness
        self.__fitness = new_fitness

    def calc_fitness(self, fitness_function):
        self.__fitness = round(1.0/fitness_function(self.params_float),self.__precision)

    def distance(self, chromosome):
        # measure the Hamming distance between the object and other chromosome
        assert len(self.bitarr) == len(chromosome.bitarr)
        return np.count_nonzero(self.bitarr != chromosome.bitarr)
        # return sum(operator.__xor__(a,b) for a,b in zip(self.bitarr,chromosome.bitarr))

    def mutate(self):
        # mutate a randomly chosen parameter
        mut_idx = np.random.random_integers(0, self.__param_no - 1)
        self.PARAMS[mut_idx].mutate()
        self.PARAMS[mut_idx].recalculate()

    def crossover(self, second_parent):
        # create copies of the parents
        first_desc = copy.deepcopy(self)
        second_desc = copy.deepcopy(second_parent)

        # generate a random cut point
        cut_point = np.random.random_integers(0, len(first_desc.bitarr) - 1)

        # interchange bits in the bit arrays
        first_desc.bitarr[0:cut_point] = second_parent.bitarr[0:cut_point]
        second_desc.bitarr[0:cut_point] = self.bitarr[0:cut_point]

        # we start recomposing the bitarrays of the parameters,
        # according to their initial length

        uppr_idx = 0

        for p_first, p_second in zip(first_desc.PARAMS, second_desc.PARAMS):
            lwr_idx = uppr_idx
            uppr_idx = lwr_idx + p_first.bit_len

            p_first.bitarr = first_desc.bitarr[lwr_idx:uppr_idx]
            p_second.bitarr = second_desc.bitarr[lwr_idx:uppr_idx]

            # recalculate the float values for each parameters,
            # according to their new bitstrings
            p_first.recalculate()
            p_second.recalculate()

        return first_desc, second_desc