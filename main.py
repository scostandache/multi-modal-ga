# todo-me create test classes
import fitness
from GA import GA
import niche


def stats():
    for niche_met in [(niche.deterministic_crowding, 150), (niche.RTS, 4000)]:

        with open(niche_met[0].__name__ + '/raport.txt', 'w+') as f:
            print niche_met[0].__name__
            for function in ['rastrigin', 'griewangk', 'rosenbrock']:

                print function
                for no_params in [5, 10, 30]:
                    line = ''
                    print no_params
                    fitness_mean = 0.0
                    for _ in xrange(3):
                        result = galg.solve(gen_no=niche_met[1],
                                            niche_method=niche_met[0],
                                            mut_prob=.8,
                                            cross_prob=.6,
                                            window=20,
                                            pop_size=80,
                                            LIMITS=fitness.dispatcher[function]['LIMITS'],
                                            param_no=no_params,
                                            precision=5,
                                            fitness=fitness.dispatcher[function]['function']
                                            )
                        fitness_mean += result
                    fitness_mean = fitness_mean / 30.0
                    line += function + ' ' + str(no_params) + ' ' + str(fitness_mean) + '\n'
                    f.write(line)

if __name__ == '__main__':

    galg = GA()

    galg.solve(gen_no=150,
               niche_method=niche.deterministic_crowding,
               mut_prob=.8,
               cross_prob=.6,
               window=20,
               pop_size=80,
               LIMITS=fitness.dispatcher['rastrigin']['LIMITS'],
               param_no=5,
               precision=5,
               fitness=fitness.dispatcher['rastrigin']['function']
               )








