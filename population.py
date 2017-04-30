from chromosome import Chromosome
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fitness import *

import numpy as np


class Population(object):
    # class to represent the population
    def __init__(self, pop_size, LIMITS, param_no, precision, fitness):
        """
        
        :param pop_size: number of chromosomes in population
        :param LIMITS: limits of chromosome's parameters
        :param param_no: number of parameters for a chromosome
        :param precision: precision of parameters' float values
        """

        self.MEMBERS = [Chromosome(param_no, LIMITS, precision) for _ in xrange(pop_size)]
        for member in self.MEMBERS:
            member.fitness = (round(fitness(member.params_float), precision))
        self.__fitness = fitness
        self.__precision = precision
        self.__LIMITS = LIMITS

    def sort(self):
        # function to sort the population by fitness
        self.MEMBERS = sorted(self.MEMBERS, key=lambda member: member.fitness, reverse=False)

    def randomly_mutate(self):
        random_el = random.choice(self.MEMBERS)
        random_el.mutate()
        random_el.fitness = round(self.__fitness(random_el.params_float), self.__precision)

    def visualise(self,iterative=False):
        x = np.array([member.params_float[0] for member in self.MEMBERS])
        y = np.array([member.params_float[1] for member in self.MEMBERS])
        z = [member.fitness for member in self.MEMBERS]

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        s = ax.scatter(x, y, z, c="r")
        s.set_edgecolors = s.set_facecolors = lambda *args: None

        ax.legend()

        if(len(self.__LIMITS)==1):
            ax.set_xlim3d(tuple(self.__LIMITS[0].values()))
            ax.set_ylim3d(tuple(self.__LIMITS[0].values()))
            ax.set_zlim3d(min([member.fitness for member in self.MEMBERS])-3,
                          max([member.fitness for member in self.MEMBERS])+3)
        else:
            if(len(self.__LIMITS)==2):
                ax.set_xlim3d(tuple(self.__LIMITS[0].values()))
                ax.set_ylim3d(tuple(self.__LIMITS[1].values()))
                ax.set_zlim3d(min([member.fitness for member in self.MEMBERS])-3,
                              max([member.fitness for member in self.MEMBERS])+3)

        ax.set_xlabel('first argument')
        ax.set_ylabel('second argument')
        ax.set_zlabel('fitness')

        plt.show()

