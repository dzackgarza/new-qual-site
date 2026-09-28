---
order: 5
title: Calculus Preliminaries
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

::: {.proof}
Let $f\colon X\to X$ be a contraction with constant $c<1$ on a complete metric space $X$.

Uniqueness: if $x, y$ are fixed points, then $\abs{x-y} = \abs{f(x) - f(y)}\leq c \abs{x-y}$, and $c<1$ forces $\abs{x-y} = 0$.

Existence: choose $x_0\in X$ and set $x_k \coloneqq f(x_{k-1})$.
Then $\abs{x_{k+1}-x_k} = \abs{f(x_k) - f(x_{k-1}) } \leq c\abs{x_k - x_{k-1}}$, so by induction $\abs{x_{k+1}- x_k}\leq c^k \abs{x_1 - x_0}$.
For $n < m$,
$$
\abs{x_m - x_n} \leq \sum_{k=n}^{m-1} \abs{x_{k+1} - x_{k}} \leq \sum_{k=n}^{m-1} c^k \abs{x_1 - x_0} \leq \frac{c^n}{1-c} \abs{x_1 - x_0},
$$
which tends to $0$ as $n\to\infty$, so $(x_k)$ is Cauchy and converges to some $x\in X$.
Since $f$ is continuous, $f(x) = \lim_k f(x_k) = \lim_k x_{k+1} = x$.

:::

## The implicit and inverse function theorems

[[T-QMGPN]]

::: {.slogan}
Near a point where the derivative in the dependent variables is nonsingular, the solution set of the equation is the graph of a function.

:::

[[T-TUXBP]]

[[T-XECJ3]]

::: {.slogan}
A $C^1$ map is invertible, with $C^1$ inverse, on some neighborhood of each point at which its derivative is invertible.

:::

## Convergence of series

::: {.example title="A convergent series that is not absolutely convergent"}
$\sum_{k\geq 1} k\inv$ diverges, but $\sum_{k\geq 1} (-1)^{k+1} k\inv$ converges.
Its partial sums $S_n$ satisfy $S_2 \leq S_4 \leq \cdots \leq S_3 \leq S_1$, since $S_{2n+2} - S_{2n} = \frac{1}{2n+1}-\frac{1}{2n+2} > 0$ and $S_{2n+3} - S_{2n+1} = -\frac{1}{2n+2} + \frac{1}{2n+3} < 0$.
The even and odd partial sums are monotone and bounded, so they converge, and $S_{2n+1} - S_{2n} = \frac{1}{2n+1}\to 0$, so they have a common limit.

:::

## Integrals

::: {.fact title="Line integrals in the plane"}
\envlist

- For $f\colon\RR^2\to\RR$ differentiable, $\grad f = \tv{ \dd{f}{x}, \dd{f}{y} }$; a vector field of the form $F = \grad f$ is a gradient field.
- For $f$ differentiable and a differentiable curve $\gamma$, the chain rule gives $\frac{d}{dt} (f\circ \gamma)(t) = \inner{ (\grad f)(\gamma(t))} {\gamma'(t)}$.
- For $F(x, y) = \tv{M(x, y), N(x, y)}$, $\curl F = \dd{N}{x} - \dd{M}{y}$ and $\div F = \dd{M}{x} + \dd{N}{y}$.
- For $\gamma\colon[a,b]\to\RR^2$ piecewise $C^1$, $\int_\gamma F\cdot \dr = \int_a^b F(\gamma(t))\cdot \gamma'(t) \dt$.

:::

### Green's theorem

[[T-4M73O]]

::: {.remark}
Green's theorem is stated for $M$ and $N$ with continuous first partial derivatives on an open set containing the region and its boundary.

:::

### Stokes' theorem

[[T-LO7QM]]

## Series and sequences

::: {.fact title="Partial fraction decomposition"}
Let $p/q$ be a rational function with $\deg p < \deg q$ and $q$ factored over $\RR$ into linear and irreducible quadratic factors.
Then $p/q$ is a sum of the following terms:

- for each linear factor $(x-r)$ of multiplicity $k$, terms $\frac{A_1}{x-r}, \frac{A_2}{(x-r)^2}, \ldots, \frac{A_k}{(x-r)^k}$;
- for each irreducible quadratic factor $h$ of multiplicity $k$, terms $\frac{B_1x+C_1}{h(x)}, \ldots, \frac{B_kx+C_k}{h(x)^k}$.

:::

[[PR-4LISY]]

[[T-AZSCN]]

::: {.remark}
Inside its radius of convergence, a power series may be integrated and differentiated term by term, and the resulting series have the same radius of convergence.
A uniformly convergent series of continuous functions on a compact interval may be integrated term by term.
A uniformly convergent series of differentiable functions need not be differentiable term by term: $\sum_{n\geq1} \frac{\sin(n^2x)}{n^2}$ converges uniformly on $\RR$ while the series of derivatives $\sum_{n\geq 1} \cos(n^2x)$ diverges at $x=0$.

:::

[[PR-WIMIM]]

[[PR-TOK44]]

[[PR-NQ64T]]

[[PR-5WUAP]]

::: {.fact title="Cauchy product"}
Where both series converge absolutely,
$$
\sum_{k\geq 0} a_kz^k \cdot \sum_{k\geq 0} b_k z^k = \sum_{k\geq 0} c_k z^k,\qquad c_k \coloneqq \sum_{j=0}^k a_j b_{k-j}.
$$
The standard power series are on [[complex-analysis/basics/series-reference|Series reference]].

:::

::: {.fact title="Polynomial division"}
For polynomials $f, g$ over a field with $g\neq 0$, there are unique polynomials $q, r$ with $f = qg + r$ and $\deg r < \deg g$ or $r = 0$.

:::

[[FT-3ZL25]] [[FT-BSOZF]]

## Convergence of functions

[[D-AIQG3]]

[[D-5Y4MC]]

::: {.remark title="Arzelà--Ascoli"}
For $X$ compact Hausdorff, equip $C(X; \RR)$ with the uniform norm $\norm{f}_{\infty} \coloneqq \sup_{x\in X} \abs{f(x)}$.
A subset $A \subseteq C(X;\RR)$ is compact if and only if it is closed, bounded, and [[D-5Y4MC|equicontinuous]].
In particular, every bounded equicontinuous sequence in $C(X;\RR)$ has a uniformly convergent subsequence.

:::

[[D-QTJ7T]]

::: {.fact}
A continuous function on a compact metric space is uniformly continuous.

:::

[[D-HL4KE]]

::: {.remark}
If $f\colon \Omega \to \Omega'$ is a holomorphic bijection, then $f\inv$ is holomorphic.
For real functions the analogue fails: $f(x) = x^3$ is a smooth bijection $\RR\to\RR$ with $f'(0) = 0$, and $f\inv(x) = x^{1/3}$ is not differentiable at $0$.

:::

## Exercises

[[E-5GT6F]]

[[E-2JGJL]]
[[E-CLMEK]]
[[E-DXXL4]]
[[E-6ULIT]]
[[E-5KI4G]]
[[E-4P3T2]]
[[E-XXUNZ]]
