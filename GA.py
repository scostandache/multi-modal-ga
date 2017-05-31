#todo-me create separate function for visualising
from population import Population
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

class GA(object):
    def solve(self,
              gen_no,
              niche_method,
              pop_size,
              LIMITS,
              param_no,
              precision,
              fitness,
              **kwargs):
        population = Population(pop_size,
                                LIMITS,
                                param_no,
                                precision,
                                fitness)

        for i in xrange(gen_no):
            niche_method(population, fitness,**kwargs)
        population.sort()
        return population.MEMBERS[0].fitness



        # ===============================


        #
        # x = np.array([])
        # y = np.array([])
        # z = np.array([])
        # count = 0
        # def update_graph(count):
        #
        #     x = np.array([member.params_float[0] for member in population.MEMBERS])
        #     y = np.array([member.params_float[1] for member in population.MEMBERS])
        #     z = np.array([ member.fitness for member in population.MEMBERS ])
        #
        #     graph.set_data(x, y)
        #     graph.set_3d_properties(z)
        #
        #     ax.set_xlim3d(tuple(LIMITS[0].values()))
        #     ax.set_ylim3d(tuple(LIMITS[0].values()))
        #     ax.set_zlim3d(min([member.fitness for member in population.MEMBERS]) - 3,
        #                   max([member.fitness for member in population.MEMBERS]) + 3)
        #
        #
        #     niche_method(population, fitness,**kwargs)
        #     population.sort()
        #     best = population.MEMBERS[0].fitness
        #     title.set_text('f = {}, n = {}, t={}, best={}'.format(fitness.__name__[:4], niche_method.__name__[:3],count,best))
        #     return title, graph,
        #
        #
        # fig = plt.figure()
        #
        # ax = fig.add_subplot(111, projection = '3d')
        #
        # ax.set_xlabel('first argument')
        # ax.set_ylabel('second argument')
        # ax.set_zlabel('fitness')
        #
        # title = ax.set_title('')
        # graph, = ax.plot(xs=x, ys=y, zs=z, linestyle="", marker=".", color='k')
        # ani = matplotlib.animation.FuncAnimation(fig, update_graph, gen_no, interval=1, blit = True, repeat=True,  repeat_delay= 5000)
        #
        # plt.show()







