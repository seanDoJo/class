CSCI 5636 HW1

Sean Donohoe

- The stencil for diffmat, assuming the interior uses a centered difference, is [-1 0 1]

- To handle the boundary conditions, I took a right-sided and left-sided difference for the left and right bounds, respectively

- This meant altering the first row to be [-1 1 0 0...] and the last row to be [0 0....0 -1 1], and divided by the one sided difference


- To handle non-uniform grids, I redid the second derivative equation utilizing the left and right one-sided differences to get the following diff2mat stencil for the interior

u''(x) = (1 / (0.5*(Hl + Hr)*(Hl*Hr))) * stencil([Hl, -(Hl + Hr), Hr]), where Hl = Xn - X(n-1) and Hr = X(n+1) - Xn

- To handle the boundary conditions, I did a one-sided difference of the one-sided and centered first derivatives of U0 and U1, and Un-1 and Un

- This created the row stencils

u''(x) = 
		(1/(0.5*(Hr)*(Hr+Hrr)*Hr)) * stencil([Hrr, -(Hr + Hrr), Hr])

for the left boundary, where Hr = X(1) - X(0) and Hrr = X(2) - X(1), and

		(1/(0.5*(Hl)*(Hl+Hll)*Hl)) * stencil([Hll, -(Hl + Hll), Hll])

for the right boundary, where Hl = X(n) - X(n-1) and Hll = X(n-1) - X(n-2)

- For diffmat, I analyzed the rate of convergence using both the L2 and Infinity norms. 

- The Infinity norm shows that diffmat is first order convergent, which makes sense since it will be focusing on the error generated by the boundaries. Their one-sided difference methods are first order convergent, therefore masking the convergence of the interior.

- The L2 norm was only slightly better, and appears to still be first-order convergent (perhaps a little better)

- The rate of convergence was the same for both norms, for both uniform and uniformly-random-sampled grids over sin, cos, and exp

- For diff2mat, I also analyzed the rate of convergence using both the L2 and Infinity norms.

- As with diffmat, both the Infinity and L2 norms showed diff2mat as first-order convergent for uniform grids

- For uniformly-random-sampled grids, however, diff2mat appeared much worse than first-order convergent. I initially suspected that this might be due to an error in my boundary difference calculations, however upon plotting solutions it became apparent that the errors happened all over the interval.



To run this code, execute `python grid_refinement_error.py`, and plots of errors for both L2 and Infinity norms will be displayed, as well as a plot of the analytical solution versus the exact solution over the interval [-1, 1]