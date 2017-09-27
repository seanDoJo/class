import numpy
import matplotlib.pyplot as pyplot
from ode_cheb import ode_cheb

if __name__ == '__main__':
    cosPoints_f = lambda x: (numpy.cos(x) - 1) + (-1*numpy.sin(x)) + (-1*numpy.cos(x))
    errs_inf = []
    errs_l2 = []
    xs = []
    grids = (2**numpy.arange(3, 10))
    grids = [k for k in range(2, 21)]
    for gridSize in grids:
        x, L, rhs = ode_cheb(1, 1, cosPoints_f, gridSize)
        u_n = numpy.linalg.solve(L, rhs)
        u_n = u_n[0:gridSize+1]
        u = (numpy.cos(x) - 1)
        err = numpy.linalg.norm((u - u_n), numpy.inf)
        errs_inf.append(err)
        err = numpy.linalg.norm((u - u_n))/numpy.sqrt(x.size)
        errs_l2.append(err)
        xs.append(x.size)

    xs = numpy.array(xs)
    pyplot.figure()
    pyplot.loglog(xs, errs_inf, 'o', label="error_inf")
    pyplot.loglog(xs, errs_l2, 'o', label="error_l2")
    pyplot.loglog(xs, (xs-1)**(-1.), label='$h$')
    pyplot.loglog(xs, (xs-1)**(-2.), label='$h^2$')
    pyplot.legend(loc='upper right')
    pyplot.show()

    xCubed_f = lambda x: (x*x*x) + (3*x*x) + (6*x)
    errs_inf = []
    errs_l2 = []
    xs = []
    for gridSize in grids:
        x, L, rhs = ode_cheb(1, 1, xCubed_f, gridSize)
        u_n = numpy.linalg.solve(L, rhs)
        u_n = u_n[0:gridSize+1]
        u = (x*x*x)
        err = numpy.linalg.norm((u - u_n), numpy.inf)
        errs_inf.append(err)
        err = numpy.linalg.norm((u - u_n))/numpy.sqrt(x.size)
        errs_l2.append(err)
        xs.append(x.size)

    xs = numpy.array(xs)
    pyplot.figure()
    pyplot.loglog(xs, errs_inf, 'o', label="error_inf")
    pyplot.loglog(xs, errs_l2, 'o', label="error_l2")
    pyplot.loglog(xs, (xs-1)**(-1.), label='$h$')
    pyplot.loglog(xs, (xs-1)**(-2.), label='$h^2$')
    pyplot.legend(loc='upper right')
    pyplot.show()
