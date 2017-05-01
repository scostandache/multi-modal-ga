# todo-me create test classes
import fitness
from GA import GA
import niche

if __name__ == '__main__':

    galg = GA()
    galg.solve(gen_no=350,
               niche_method = niche.RTS,
               mut_prob = 0.3,
               cross_prob = 0.5,
               pop_size=200,
               window = 40,
               LIMITS=fitness.dispatcher['griewangk']['LIMITS'],
               param_no=2,
               precision=5,
               fitness=fitness.dispatcher['griewangk']['function']
               )





