import matplotlib.pyplot as pyplot
from fdtools import *

def ode_cheb(a, b, rhsfunc, n):
        #x(t) = 2*t - 1
        #T(x(t))' = T'(x(t))*x'(t) = 2*T'(x(t))
        x = cosspace(-1, 1, n)

        T = chebeval(x)
        Tinv = numpy.linalg.inv(T[0])

        L11 = b*numpy.eye(x.size)
        L11[0,:] = numpy.eye(x.size)[0,:]
        L12 = a*numpy.eye(x.size) + (2*T[1]).dot(Tinv)
        L12[0,:] = numpy.zeros(x.size)
        L1 = numpy.hstack((L11, L12))

        L21 = (2*T[1]).dot(Tinv)
        L21[0,:] = numpy.zeros(x.size)
        L22 = -1*numpy.eye(x.size)
        L22[0,:] = numpy.eye(x.size)[0,:]
        L2 = numpy.hstack((L21, L22))

        L = numpy.vstack((L1, L2))
        rhs = numpy.zeros(x.size*2)
        rhs[0:x.size] = rhsfunc(x)

        rhs[0] = 1


	return ((x + 1)/2.), L, rhs

if __name__ == '__main__':
        n = 100
	f = lambda x: (x*x*x + 1) + (3*x*x) + (6*x)
        #f = lambda x: (numpy.cos(x)) + (-1*numpy.sin(x)) + (-1*numpy.cos(x))
	x, L, rhs = ode_cheb(1, 1, f, n)
	
        u_a = x*x*x + 1
	#u_a = (numpy.cos(x))
        
	u = numpy.linalg.solve(L, rhs)

        u = u[0:n]

	pyplot.figure()
	pyplot.plot(x, u, 'o', label="numerical")
	pyplot.plot(x, u_a,  label="actual")
        #pyplot.legend(loc='upper right')
	pyplot.show()
