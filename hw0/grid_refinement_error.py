import numpy
from diffmat import diffmat
import matplotlib.pyplot as pyplot

def error_inf(u, up, x, dmat):
	L = dmat(x)
	a_up = L.dot(u(x))

	return numpy.linalg.norm(a_up - up(x), numpy.inf)

def error_l2(u, up, x, dmat):
	L = dmat(x)
	a_up = L.dot(u(x))

	return numpy.linalg.norm(a_up - up(x))/numpy.sqrt(x.size)

def grid_refinement_error(u, up, dmat, error):
	grids = 2**numpy.arange(3, 10)

	uniform_grid = [numpy.linspace(-1, 1, n) for n in grids]

	uniform_error = [error(u, up, x, dmat) for x in uniform_grid]

	return (grids, uniform_error)


if __name__ == '__main__':
	pyplot.figure()

	gs, error = grid_refinement_error(numpy.sin, numpy.cos, diffmat, error_l2)
	pyplot.loglog(gs, error, 'o', label="error_l2")

	gs, error = grid_refinement_error(numpy.sin, numpy.cos, diffmat, error_inf)
	pyplot.loglog(gs, error, 'o', label="error_inf")

	pyplot.loglog(gs, (gs-1)**(-1.), label='$h$')
	pyplot.loglog(gs, (gs-1)**(-2.), label='$h^2$')
	pyplot.xlabel('Resolution $n$')
	pyplot.ylabel('First Derivative Error')
	pyplot.legend(loc='upper right')
	pyplot.show()
