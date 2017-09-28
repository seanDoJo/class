import matplotlib.pyplot as pyplot
import numpy
from ode_cheb import ode_cheb

f = lambda x: x*0
ab = [(1, 1), (-2, 2), (3, 4), (1, 0), (0, 1)]
for a,b in ab:
    n = 20
    x, L, rhs = ode_cheb(a, b, f, n)
    u = numpy.linalg.solve(L, rhs)
    u = u[0:n]
    pyplot.plot(x, u, label="a = {}, b = {}".format(a, b))
pyplot.legend(loc="lower left")
pyplot.show()
