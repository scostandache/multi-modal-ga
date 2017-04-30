# todo-me create test classes
import fitness
from GA import GA
import niche

if __name__ == '__main__':

    galg = GA()
    galg.solve(gen_no=50,
               niche_method=niche.deterministic_crowding,
               pop_size=150,
               LIMITS=fitness.dispatcher['SHCB']['LIMITS'],
               param_no=2,
               precision=5,
               fitness=fitness.dispatcher['SHCB']['function']
               )





