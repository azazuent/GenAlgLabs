import numpy

from SimpleGenAlg import SimpleGenAlg
from numpy import cos
import matplotlib.pyplot as ppl


def func(x: float) -> float:
    return cos(3 * x - 15) * x


if __name__ == "__main__":
    ga = SimpleGenAlg(100, 200, 0.5, 0.01, func)
    for i in range(201):
        population = ga.iterate()
        #if not(i % 25):
        if i == 0 or i == 1 or i == 5 or i == 15 or i == 50:
            __x = numpy.linspace(-10, 10, 1000)
            ppl.title(f"Iteration {i}")
            ppl.plot(__x, func(__x))
            ppl.plot(population, [func(_) for _ in population], 'ro')
            ppl.show()
    print(max(map(ga.func_value, ga.population)))
