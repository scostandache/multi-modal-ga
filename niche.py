import random
import numpy
import copy

def deterministic_crowding(population, fitness_func, mut_prob=1.0, cross_prob=1.0):
    # Deterministic Crowding niching method

    for _ in xrange(len(population.MEMBERS) / 2):
        # select two parents randomly, with no replacement
        first_parent = random.choice(population.MEMBERS)
        population.MEMBERS.remove(first_parent)
        second_parent = random.choice(population.MEMBERS)
        population.MEMBERS.remove(second_parent)

        first_desc, second_desc = first_parent.crossover(second_parent)

        first_desc.mutate()
        second_desc.mutate()
        first_desc.calc_fitness(fitness_func)
        second_desc.calc_fitness(fitness_func)

        if first_parent.distance(first_desc) + second_parent.distance(second_desc) <= \
                        first_parent.distance(second_desc) + second_parent.distance(first_desc):
            if first_desc.fitness <= first_parent.fitness:
                population.MEMBERS.append(first_desc)
            else:
                population.MEMBERS.append(first_parent)

            if second_desc.fitness <= second_parent.fitness:
                population.MEMBERS.append(second_desc)
            else:
                population.MEMBERS.append(second_parent)

        else:
            if second_desc.fitness <= first_parent.fitness:
                population.MEMBERS.append(second_desc)
            else:
                population.MEMBERS.append(first_parent)

            if first_desc.fitness <= second_parent.fitness:
                population.MEMBERS.append(first_desc)
            else:
                population.MEMBERS.append(second_parent)


def RTS(population, fitness_funct, mut_prob, cross_prob, window):
    # Restricted Tournament Selection niching method

    first_parent = random.choice(population.MEMBERS)
    second_parent = random.choice(population.MEMBERS)

    first_desc = copy.deepcopy(first_parent)
    second_desc = copy.deepcopy(second_parent)

    perform_tournament = False

    mut_p = random.random()
    if mut_p <= mut_prob:
        first_desc.mutate()
        first_desc.calc_fitness(fitness_funct)
        #perform_tournament = True

    #mut_p = random.random()
    #if mut_p <= mut_prob:
        second_desc.mutate()
        second_desc.calc_fitness(fitness_funct)
        perform_tournament = True

    cross_p = random.random()
    if cross_p <= cross_prob:
        first_desc, second_desc = first_desc.crossover(second_desc)

        first_desc.calc_fitness(fitness_funct)
        second_desc.calc_fitness(fitness_funct)
        perform_tournament = True

    if perform_tournament == True:

        #we get a sample of the population
        population_sample = random.sample(population.MEMBERS, window)

        #sort it by resemblence with the first_desc
        population_sample = sorted(population_sample,
                                   key=lambda member: member.distance(first_desc), reverse=False)

        #get the most resembling member
        closest_resemble = population_sample[0]

        if first_desc.fitness < closest_resemble.fitness:
            population.MEMBERS.remove(closest_resemble)
            population.MEMBERS.append(first_desc)

        #repeat the process for the second descendent

        population_sample = random.sample(population.MEMBERS, window)

        population_sample = sorted(population_sample,
                                   key=lambda member: member.distance(second_desc), reverse=False)
        closest_resemble = population_sample[0]

        if second_desc.fitness < closest_resemble.fitness:
            population.MEMBERS.remove(closest_resemble)
            population.MEMBERS.append(second_desc)


