import random


def deterministic_crowding(population, fitness_func):
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
