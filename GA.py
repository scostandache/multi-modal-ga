from population import Population
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fitness import *

import numpy as np
class GA(object):

    def solve(self,
              gen_no,
              niche_method,
              pop_size,
              LIMITS,
              param_no,
              precision,
              fitness):

        population = Population(pop_size, LIMITS, param_no, precision, fitness)

        for i in xrange(gen_no):
            niche_method(population, fitness)
            if(i%10 == 0):
                print "."

        for member in population.MEMBERS:
            print member.fitness, member.params_float
        #
        # fitnesses = [member.fitness for member in population.MEMBERS]
        # floats = [member.params_float[0] for member in population.MEMBERS]
        #
        # x= np.linspace(-5,5,300)
        # y = [test(item) for item in x]
        #
        # pylab.plot(x,y)
        # pylab.plot(floats,fitnesses,'co')
        # pylab.show()

        # fig = plt.figure()
        # ax = fig.gca(projection='3d')
        #
        # x = np.array([member.params_float[0] for member in population.MEMBERS])
        # y = np.array([member.params_float[1] for member in population.MEMBERS])
        # z = [member.fitness in population.MEMBERS]
        #
        # x,y = np.meshgrid(x,y)
        # z=np.reshape(len(x), len(y))
        # plt.contourf(x,y,z,100)
        # plt.colorbar()
        #
        # plt.show()



        #
        x = np.array([member.params_float[0] for member in population.MEMBERS])
        y = np.array([member.params_float[1] for member in population.MEMBERS])
        z = [member.fitness in population.MEMBERS]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        s=ax.scatter(x,y,z,c="r")
        s.set_edgecolors = s.set_facecolors = lambda *args:None
        ax.legend()
        ax.set_xlim3d(-5.12, 5.12)
        ax.set_ylim3d(-5.12, 5.12)
        ax.set_zlim3d(-1, 1)
        plt.show()

        # x = np.array([member.params_float[0] for member in population.MEMBERS])
        # y = np.array([member.params_float[1] for member in population.MEMBERS])
        # X, Y = np.meshgrid(x, y)
        # Z=np.sqrt(X**2,Y**2)
        #
        #
        # plt.figure()
        # cp = plt.contourf(X, Y, Z)
        # plt.colorbar()
        # plt.show()
