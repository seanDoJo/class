import numpy
from diffmat import diffmat, diff2mat
import matplotlib.pyplot as pyplot

def error_inf(u, up, x, dmat):
	L = dmat(x)
	a_up = L.dot(u(x))

	return numpy.linalg.norm(a_up - up(x), numpy.inf)

def error_l2(u, up, x, dmat):
	L = dmat(x)
	a_up = L.dot(u(x))

	return numpy.linalg.norm(a_up - up(x))/numpy.sqrt(x.size)

def uniform_grid_refinement_error(u, up, dmat, error):
	grids = 2**numpy.arange(3, 10)

	uniform_grid = [numpy.linspace(-1, 1, n) for n in grids]

	uniform_error = [error(u, up, x, dmat) for x in uniform_grid]

	return (grids, uniform_error)

def random_grid_refinement_error(u, up, dmat, error):
	grids = 2**numpy.arange(3, 10)

	random_grid = [numpy.sort(numpy.random.uniform(-1, 1, n)) for n in grids]

	random_error = [error(u, up, x, dmat) for x in random_grid]

	return (grids, random_error)

def show_refinement_error(u, up, dmat):
	pyplot.figure()

	pyplot.subplot(311)

	gs, error = uniform_grid_refinement_error(u, up, dmat, error_l2)
	pyplot.loglog(gs, error, 'o', label="error_l2")

	gs, error = uniform_grid_refinement_error(u, up, dmat, error_inf)
	pyplot.loglog(gs, error, 'o', label="error_inf")

	pyplot.loglog(gs, (gs-1)**(-1.), label='$h$')
	pyplot.loglog(gs, (gs-1)**(-2.), label='$h^2$')
	pyplot.xlabel('Resolution $n$')
	pyplot.ylabel('Error')
	pyplot.title('Uniform Grid Refinement Error for {} on {}'.format(dmat.__name__, u.__name__))
	pyplot.legend(loc='lower left')

	pyplot.subplot(312)

	gs, error = random_grid_refinement_error(u, up, dmat, error_l2)
	pyplot.loglog(gs, error, 'o', label="error_l2")

	gs, error = random_grid_refinement_error(u, up, dmat, error_inf)
	pyplot.loglog(gs, error, 'o', label="error_inf")

	pyplot.loglog(gs, (gs-1)**(-1.), label='$h$')
	pyplot.loglog(gs, (gs-1)**(-2.), label='$h^2$')
	pyplot.xlabel('Resolution $n$')
	pyplot.ylabel('Error')
	pyplot.title('Random Uniform Grid Refinement Error for {} on {}'.format(dmat.__name__, u.__name__))
	pyplot.legend(loc='lower left')

	
	pyplot.subplot(313)
	x = numpy.linspace(-1, 1, 50)
	y = up(x)
	L = dmat(x)
	a_y = L.dot(u(x))
	pyplot.plot(x, a_y, 'o', label="numerical")
	pyplot.plot(x, y, label="exact")
	pyplot.xlabel('$x$')
	pyplot.ylabel('$y$')
	pyplot.title('Exact and Numerical Solution to {} using {}'.format(u.__name__, dmat.__name__))
	
	pyplot.tight_layout()
	pyplot.show()


if __name__ == '__main__':
	test_fns = [
		(numpy.exp, numpy.exp, numpy.exp),
		(numpy.sin, numpy.cos, lambda x: -numpy.sin(x)),
		(numpy.cos, lambda x: -numpy.sin(x), lambda x: -numpy.cos(x)),
	]
	for u, up, upp in test_fns:
		show_refinement_error(u, up, diffmat)
		show_refinement_error(u, upp, diff2mat)
