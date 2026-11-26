---
order: 5
title: Calculus preliminaries
topics:
- Calculus
- Continuity
- Uniform Continuity
- Multivariable Calculus
- Riemann Integrability
- Mean Value Theorem
- Point-Set Topology
- Compactness
- Connectedness
- Metric Spaces
- Completeness
- Euclidean Spaces
- Sequences of Numbers
- Limits
- Convergence
- Differentiation
---

# Calculus preliminaries

## Fixed points

[[PR-5ZSSQ]]

## The implicit and inverse function theorems


::: {.slogan}
Near a point where the derivative in the dependent variables is nonsingular, the solution set of the equation is the graph of a function.

:::

[[T-TUXBP]]

[[T-XECJ3]]

::: {.slogan}
A $C^1$ map is invertible, with $C^1$ inverse, on some neighborhood of each point at which its derivative is invertible.

:::

::: {.example title="Polar coordinates, by the inverse function theorem"}
The map $\Phi(r,\theta) = (r\cos\theta,\ r\sin\theta)$ has derivative
$$
\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix},
$$
of determinant $r$, so [[T-XECJ3|the inverse function theorem]] gives a $C^1$ inverse on a neighbourhood of every point with $r\neq0$: the polar coordinates of a point off the origin.
The local statement is all that can hold, since $\theta$ is determined only modulo $2\pi$.
At $r = 0$ the determinant vanishes and the map is not injective near the origin: every neighbourhood of it contains $(r,\theta)$ and $(r,\theta+\pi)$ with the same image.
:::

## Convergence of series

::: {.example title="A convergent series that is not absolutely convergent"}
$\sum_{k\geq 1} \inverseof{k}$ diverges, but $\sum_{k\geq 1} (-1)^{k+1} \inverseof{k}$ converges.
Its partial sums $S_n$ satisfy $S_2 \leq S_4 \leq \cdots \leq S_3 \leq S_1$, since $S_{2n+2} - S_{2n} = \frac{1}{2n+1}-\frac{1}{2n+2} > 0$ and $S_{2n+3} - S_{2n+1} = -\frac{1}{2n+2} + \frac{1}{2n+3} < 0$.
The even and odd partial sums are monotone and bounded, so they converge, and $S_{2n+1} - S_{2n} = \frac{1}{2n+1}\to 0$, so they have a common limit.

:::

## Integrals

::: {.fact title="Line integrals in the plane"}
\envlist

- For $f\colon\RR^2\to\RR$ differentiable, $\grad f = \thevector{ \dd{f}{x}, \dd{f}{y} }$; a vector field of the form $F = \grad f$ is a gradient field.

- For $f$ differentiable and a differentiable curve $\gamma$, the chain rule gives $\frac{d}{dt} (f\circ \gamma)(t) = \inner{ (\grad f)(\gamma(t))} {\gamma'(t)}$.

- For $F(x, y) = \thevector{M(x, y), N(x, y)}$, $\curl F = \dd{N}{x} - \dd{M}{y}$ and $\divergence F = \dd{M}{x} + \dd{N}{y}$.

- For $\gamma\colon[a,b]\to\RR^2$ piecewise $C^1$, $\int_\gamma F\cdot \dr = \int_a^b F(\gamma(t))\cdot \gamma'(t) \dt$.

The line integral and its independence of a piecewise $C^1$ parametrization are [@Ahl73, ch. 4, §1.1, Line Integrals], which defines $\int_\gamma p\,\dx+q\,\dy$ by this integral along the parameter; the chain rule in the second item is [@Rud76, ch. 9, Theorem 9.15], and the gradient, curl and divergence are the coordinate expressions of that derivative.
:::

### Green's theorem

[[T-4M73O]]

### Stokes' theorem

[[T-LO7QM]]

## Series and sequences

::: {.fact title="Partial fraction decomposition"}
Let $p/q$ be a rational function with $\deg p < \deg q$ and $q$ factored over $\RR$ into linear and irreducible quadratic factors.
Then $p/q$ is a sum of the following terms:

- for each linear factor $(x-r)$ of multiplicity $k$, terms $\frac{A_1}{x-r}, \frac{A_2}{(x-r)^2}, \ldots, \frac{A_k}{(x-r)^k}$;

- for each irreducible quadratic factor $h$ of multiplicity $k$, terms $\frac{B_1x+C_1}{h(x)}, \ldots, \frac{B_kx+C_k}{h(x)^k}$.

The decomposition is [@Ahl73, ch. 5, §2.1, Partial Fractions], which attaches to each pole of a meromorphic function its singular part and, for a rational function, assembles the sum of those parts as the polynomial part plus the proper fraction; over $\RR$ the irreducible quadratic factors are the conjugate pairs of nonreal roots.
:::

[[PR-4LISY]]

[[FF-IAUQG]]

::: {.remark}
Term-by-term differentiation needs a hypothesis on the derivatives, not only on the series: a uniformly convergent series of differentiable functions need not be differentiable term by term ([[complex-analysis/basics/uniform-convergence|Uniform convergence]]).
The power-series case is [[PR-QNDSD|smoothness on the disc of convergence]], and the tail criterion for uniform convergence is [[PR-4LISY]].
:::

[[PR-WIMIM]]


[[PR-NQ64T]]

[[PR-5WUAP]]

The Cauchy product of power series and the standard power series are on [[complex-analysis/basics/series-reference|Series reference]].

::: {.fact title="Polynomial division"}
For polynomials $f, g$ over a field with $g\neq 0$, there are unique polynomials $q, r$ with $f = qg + r$ and $\deg r < \deg g$ or $r = 0$.

This is division with remainder in the [[D-NKRGN|Euclidean domain]] $k[x]$, whose Euclidean function is the degree.
:::

[[FT-3ZL25]]

Uniform continuity, uniform convergence, and the compactness theorem for families of functions are on [[complex-analysis/basics/uniform-convergence|Uniform convergence]]; normal families are on [[complex-analysis/conformal-maps/normal-families-and-montel|Normal families and Montel]].

## Problems

[[E-5GT6F]]

[[E-2JGJL]] [[E-CLMEK]] [[E-DXXL4]] [[E-6ULIT]] [[E-5KI4G]] [[E-4P3T2]] [[E-XXUNZ]]
