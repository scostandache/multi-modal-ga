from population import Population


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
            if (i % 10 == 0):
                print len(population.MEMBERS)

        population.visualise_scatter()
