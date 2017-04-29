from chromosome import Chromosome
import random


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
            member.fitness = (round(1.0/fitness(member.params_float), precision))
        self.__fitness = fitness
        self.__precision = precision

    def sort(self):
        # function to sort the population by fitness
        self.MEMBERS = sorted(self.MEMBERS, key=lambda member: member.fitness, reverse=False)

    def randomly_mutate(self):
        random_el = random.choice(self.MEMBERS)
        random_el.mutate()
        random_el.fitness = round(self.__fitness(random_el.params_float), self.__precision)
