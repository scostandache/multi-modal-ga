# todo-me create test classes
import fitness
from GA import GA
import niche

if __name__ == '__main__':

    galg = GA()
    galg.solve(gen_no=250,
               niche_method = niche.deterministic_crowding,
               mut_prob = 0.3,
               cross_prob = 0.5,
               pop_size=90,
               LIMITS=fitness.dispatcher['rastrigin']['LIMITS'],
               param_no=30,
               precision=5,
               fitness=fitness.dispatcher['rastrigin']['function']
               )





