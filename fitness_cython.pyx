import math
from math import pi
import numpy as np
#todo-me rewrite fitness functions in cython

def rastrigin(double [:] params):
    cdef int i
    cdef int param_len = len(params)

    cdef double fitness = 10.0 * param_len
    for i in xrange(param_len):
        fitness += (params[i] ** 2) - (10.0 * math.cos(2.0 * pi * params[i]))
    return fitness


def rosenbrock(params):
    fitness = 0
    for curr, next in zip(params, params[1:]):
        fitness += (100.0 * (next - curr ** 2) ** 2 + (1 - curr) ** 2)

    return fitness


def griewangk(params):
    fitness = sum((parameter ** 2) / 4000.0 for parameter in params)
    return fitness - np.prod([math.cos(parameter / math.sqrt(i + 1))
                              for i, parameter in list(enumerate(params))])


def SHCB(params):
    a, b = params
    return (4 - 2.1 * (a * a) + (a * a * a * a) / 3.0) * (a * a) + a * b + (-4 + 4 * (b * b)) * (b * b)


def test(x):
    if (type(x) == list):
        return 3.0 + (x[0] ** 2) - 3.0 * math.cos((2.0 * math.pi) * x[0])
    else:
        return 3.0 + (x ** 2) - 3.0 * math.cos((2.0 * math.pi) * x)


dispatcher = {
    'rastrigin': {
        'function': rastrigin,
        'LIMITS': [{'min': -5.12, 'max': 5.12}]
    },
    'rosenbrock': {
        'function': rosenbrock,
        'LIMITS': [{'min': -2.048, 'max': 2.048}]
    },
    'griewangk': {
        'function': griewangk,
        'LIMITS': [{'min': -600, 'max': 600}]
    },
    'SHCB': {
        'function': SHCB,
        'LIMITS': [{'min': -3, 'max': 3}, {'min': -2, 'max': 2}]
    },
    'test': {
        'function': test,
        'LIMITS': [{'min': -5, 'max': 5}]
    }
}
