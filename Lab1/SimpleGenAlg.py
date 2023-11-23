import random as r
import bitmap as bm


class SimpleGenAlg:

    def __init__(self, power, iter_amount, cross_p, mut_p, func, a=-9.6, b=9.1):

        self.power = power

        self.iter_amount = iter_amount

        self.cross_p = cross_p
        self.mut_p = mut_p

        self.a = a
        self.b = b
        self.func = func

        self.population = [bm.BitMap.fromstring(
            ''.join([str(r.randint(0, 1)) for _ in range(16)]))
            for __ in range(power)]

    def func_value(self, chromosome: bm.bitmap) -> float:
        dec_value = int(chromosome.tostring(), 2)
        return self.func(self.a + dec_value * (self.b - self.a) / (2 ** 16 - 1))

    def reproduction(self):

        population_value = [self.func_value(c) + 9 for c in self.population]
        population_sum = sum(population_value)

        probabilities = [ind / population_sum for ind in population_value]

        self.population = r.choices(self.population, probabilities, k=self.power)

    def crossingover(self):

        if r.random() > self.cross_p:
            return

        individual1 = r.choice(self.population)
        self.population.remove(individual1)
        individual2 = r.choice(self.population)
        self.population.remove(individual2)

        k = r.randint(0, 15)

        child1 = bm.BitMap(16)
        child2 = bm.BitMap(16)

        for i in range(0, k):
            child1[i] = individual1[i]
            child2[i] = individual2[i]
        for i in range(k, 16):
            child1[i] = individual2[i]
            child2[i] = individual1[i]

        self.population.append(child1)
        self.population.append(child2)

    def mutation(self):
        for individual in self.population:
            if r.random() < self.mut_p:
                individual.flip(r.randint(0, 15))

    def find_max(self):
        for i in range(self.iter_amount):
            self.iterate()
        return max(map(self.func_value, self.population))

    def iterate(self):
        prev_pop = [self.a + int(x.tostring(), 2) * (self.b - self.a) / (2 ** 16 - 1)
                    for x in self.population]
        self.reproduction()
        self.crossingover()
        self.mutation()
        return prev_pop
