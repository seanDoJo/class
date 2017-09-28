Sean Donohoe
HW 1

For this assignment, I tried rewriting the second order equation as a system of first order equations

[bI | aI + T[1]Tinv][x1, x2] = f(t)
[T[1]Tinv | -I][x1, x2] = 0

setting:

  the first row to the first identity row and the first rhs element to 1, to enforce u(0) = 1

  the len(t)-th row to be the len(t)-th identity row, to enforce u'(0) = 0

Since the chebyshev polynomials are based around cosspace(-1, 1), set a function x(t) = 2*t - 1 to scale the interval [0, 1] back to [-1, 1]. Calculating T(t) therefore became T(x(t)), meaning T(x(t))' = T'(x(t)) * x'(t), or T[1]*2

The numerical solutions for cos(x) and (x^3) + 1 appear to be off from their analytical counterparts, most likely due to me not considering how T(x(t)) interacts with the normal u(t), or because the interval is normally assumed to be opened. I, however, cannot figure out what the problem is exactly. Though the numerical solutions are not accurate, they do appear to be stable, as adding more points makes their solution more defined (rather than becoming noisy).

The grid refinement error obviously doesn't converge when compared to a true function such as cos(x), however as points are added, the difference in their values as n increases appears to reflect a second order convergence (e.g. u(xi) for n = 10 and u(xi) for n = 20 change in value around 0.001, whereas u(xi) for n = 30 and u(xi) for n = 31 change 0.000001, implying the convergence is around second order).

Assuming the approximations are somewhat representative of the correct solution, two sets of (a, b) with qualitatively different dynamics include (a=1, b=0), a straight line,  and (a=-2, b=2), a line representing a curve similar to cos(t)
