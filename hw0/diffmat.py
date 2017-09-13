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

def diff2mat(x):
    # calculate the left-looking grid space for each point
    h_interior = x[1:] - x[:-1]

    e = numpy.ones_like(x)
    D = numpy.diag(e)

    for i in range(1, x.size-1):
        # for unevenly spaced grids we can't assume the exterior denominator is 1/(h*h), and is instead 1/(0.5*(hl+hr)*(hlhr))
        denom = 0.5*(h_interior[(i-1)] + h_interior[i])*(h_interior[(i-1)]*h_interior[i])
        
        # again, since unevenly spaced grids don't have hl = hr, rewriting the equation makes the stencil [hl -(hl+hr) hr]
        D[i, (i-1):(i+2)] = numpy.array([h_interior[(i-1)], -(h_interior[(i-1)] + h_interior[i]), h_interior[i]]) / denom
    
    leftDenom = (0.5*h_interior[0])*(h_interior[0] + h_interior[1])*(h_interior[0])
    D[0, 0:3] = numpy.array([h_interior[1], -(h_interior[0] + h_interior[1]), h_interior[0]])/leftDenom

    rightDenom = (0.5*h_interior[-1])*(h_interior[-1] + h_interior[-2])*(h_interior[-1])
    D[-1, -3:] = numpy.array([h_interior[-1], -(h_interior[-1] + h_interior[-2]), h_interior[-2]])/rightDenom

    #print D
    return D
    
	

if __name__ == '__main__':
	x = numpy.sort(numpy.random.uniform(0, 10, 1000))
	x = numpy.linspace(0, 10, 1000)
        #x = numpy.array([k**1.5 for k in range(10)])
	y = numpy.exp(x)
	L = diff2mat(x)
	ay = L.dot(y)

	pyplot.figure()
	pyplot.plot(x, ay, 'o', label='analytical')
	pyplot.plot(x, numpy.exp(x), label='exact')
	pyplot.legend(loc='upper left')
	pyplot.show()

