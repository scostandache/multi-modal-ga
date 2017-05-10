# todo-me create test classes
import fitness
from GA import GA
import niche

if __name__ == '__main__':

    galg = GA()
    galg.solve(gen_no=10000,
               niche_method = niche.deterministic_crowding,
               mut_prob = .4,
               cross_prob = .6,
               # window=20,
               pop_size=50,
               LIMITS=fitness.dispatcher['rastrigin']['LIMITS'],
               param_no=2,
               precision=7,
               fitness=fitness.dispatcher['rastrigin']['function']
               )





