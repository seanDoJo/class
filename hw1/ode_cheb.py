import matplotlib.pyplot as pyplot
from fdtools import *

def ode_cheb(a, b, n):
	x = cosspace(-1, 1, n+1)
	u_0_index = -1
	for i,v in enumerate(x):
		if v == 0.:
			u_0_index = i
			break
		elif v > 0.:
			u_0_index = i
			x = numpy.insert(x, i, 0.)
			break

	T = chebeval(x)
	Tinv = numpy.linalg.inv(T[0])
	
	L = T[2].dot(Tinv) + a*T[1].dot(Tinv) + b * numpy.eye(x.size)

	

	return x, L

if __name__ == '__main__':
	f = lambda x: (x*x*x) + (3*x*x) + (6*x)
	for n in range(1, 400):
		x, L = ode_cheb(1, 1, n)
	
	u_a = x*x*x

	u = numpy.linalg.solve(L, f(x))

	pyplot.figure()
	pyplot.plot(x, u, 'o')
	pyplot.plot(x, u_a)
	pyplot.show()
