import math
import numpy as np

def rastrigin(params):

    fitness = 10*len(params)
    for param in params:
        fitness += param**2 - (10*math.cos(2*math.pi*param))
    return fitness


def rosenbrock(params):

    fitness = 0
    for curr, next in zip(params, params[1:]):
        fitness += 100.0*(curr - next**2)**2 + (1-curr)**2

    return fitness


def griewangk(params):

    fitness = sum((parameter**2)/4000.0 for parameter in params)
    return fitness - np.prod([math.cos(parameter/math.sqrt(i+1))
                              for i, parameter in list(enumerate(params))])


def SHCB(params):

    a, b = params
    return (4.0-2.1*(a*a)+((a*a*a*a)/3)) + a*b + (-4.0+4.0*(b*b))*b*b


dispatcher = {
    'rastrigin': {
        'function': rastrigin,
        'LIMITS': [{'min':-5.12, 'max':5.12}]
    },
    'rosenbrock': {
        'function': rosenbrock,
        'LIMITS': [{'min': -2.048, 'max': 2.048}]
    },
    'griewangk': {
        'function': griewangk,
        'LIMITS': [{'min': -600, 'max': 600}]
    },
    'SHCB':{
        'function': SHCB,
        'LIMITS': [{'min': -3, 'max': 3},{'min': -2, 'max': 2}]
    }
}