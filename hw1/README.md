Sean Donohoe
HW 1

For this assignment, I tried rewriting the second order equation as a system of first order equations

[bI | aI + T[1]Tinv][x1, x2] = f(t)
[T[1]Tinv | -I][x1, x2] = 0

setting:

  the first row to the first identity row and the first rhs element to 1, to enforce u(0) = 1

  the len(t)-th row to be the len(t)-th identity row, to enforce u'(0) = 0

Since the chebyshev polynomials are based around cosspace(-1, 1), I first scaled t by 1/2 to make the interval cosspace(-0.5, 0.5), then added 0.5 to make the interval cosspace(0, 1)

I'm not sure why, but for n > 20 the method becomes *extremely* unstable. I suspect it's because I haven't properly asserted the constraint u'(0) = 0, but am not sure exactly what's wrong.

Scoping n to have a max value of 20, the grid refinement error doesn't appear to converge (supporting my method as unstable), however qualitatively the solutions lend the idea that the method would have first order convergence if implemented correctly.

Again, scoping n to have a max value of 20, two sets of (a, b) with qualitatively different dynamics include (a=1, b=0), a straight line,  and (a=-2, b=2), a line representing a curve similar to cos(t)
