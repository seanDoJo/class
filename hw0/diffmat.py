import numpy
import matplotlib.pyplot as pyplot

def diffmat(x):
	# compute interior using centered difference
	h_interior = x[2:] - x[:-2]

	# compute boundary using one-sided difference
	h_oneside = x[1:] - x[:-1]

	h = numpy.insert(h_interior, 0, h_oneside[0])
	h = numpy.append(h, h_oneside[-1])

	h = 1/h
	
	# build centered difference matrix
	e = numpy.ones_like(x)
	D = -1*numpy.diag(e[:-1], -1) + numpy.diag(e[:-1], 1)

	# make first and last row a one-sided difference
	D[0, 0] = -1
	D[-1, -1] = 1
	
	# divide by h
	hmat = numpy.repeat(h, x.size).reshape((x.size, x.size))
	D = D * hmat

	return D	
	

if __name__ == '__main__':
	x = numpy.linspace(0, 8, 20)
	y = numpy.sin(x)
	L = diffmat(x)
	ay = L.dot(y)

	pyplot.figure()
	pyplot.plot(x, ay, 'o', label='analytical')
	pyplot.plot(x, numpy.cos(x), label='exact')
	pyplot.legend(loc='upper left')
	pyplot.show()

