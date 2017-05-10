# todo-me create test classes
import fitness
from GA import GA
import niche

if __name__ == '__main__':

    galg = GA()
    galg.solve(gen_no=4000,
               niche_method = niche.RTS,
               mut_prob = .4,
               cross_prob = .6,
               window=20,
               pop_size=50,
               LIMITS=fitness.dispatcher['SHCB']['LIMITS'],
               param_no=2,
               precision=7,
               fitness=fitness.dispatcher['SHCB']['function']
               )





