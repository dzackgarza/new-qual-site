---
order: 5
title: Calculus Preliminaries
---

# Calculus Preliminaries

## Derivatives 

:::{.proposition title="Contraction principle"}
If $(X, \abs{\wait})$ is a metric space and $f: X\to X$ with
\[
\abs{f(x) - f(y)} \leq c \abs{x-y} \text{ for some }c < 1, \forall x, y\in X
,\]
then $f$ is a **contraction**.
If $X$ is complete, then $f$ has a unique fixed point $x_0$ such that $f(x_0) = x_0$.
:::

:::{.proof title="?"}
Uniqueness: if $x, y$ are two fixed points, then 
\[
0 \leq \abs{x-y} = \abs{f(x) - f(y)}\leq c \abs{x-y}\leq \abs{x-y}
,\]
forcing $\abs{x-y} = 0$

Existence:
Define a sequence by picking $x_0$ arbitrarily and setting $x_k \da f(x_{k-1})$.
Then 
\[
\abs{x_{k+1}-x_k} = \abs{f(x_k) - f(x_{k-1}) } \leq c\abs{x_k - x_{k-1}}
,\]
so inductively
\[
\abs{x_{k+1}- x_k}\leq c^k \abs{x_1 - x_0}
.\]
The claim is that this makes $\ts{x_k}$ a Cauchy sequence, this follows from the fact that if $n < m$ then
\[
\abs{x_n - x_m} \leq \sum_{n+1\leq k \leq m} \abs{x_k - x_{k-1}} \leq \sum_{n \leq k \leq m-1} c^k \abs{x_1 - x_0} \leq c^n \abs{x_1 - x_0 \over 1-c} \to 0
.\]
:::

## Implicit Function Theorem

:::{.theorem title="Implicit Function Theorem"}
Suppose $f\in C^1(\RR^{n+m}, \RR^n)$, that $f(a, b) = 0$, and the derivative $D_f(a, b)$ at $(a, b)$ is an invertible linear map.
Then there exists a neighborhood $U\subseteq \RR^n$ containing $a$ and a unique $g\in C^1(U, \RR^m)$ such that $g(a) = b$ and $f(a, g(a)) = 0$ for all $x\in U$.
:::

:::{.slogan}
A relation is locally the graph of a function wherever the derivative is nonsingular.
:::

### Inverse Function Theorem

:::{.theorem title="Inverse Function Theorem"}
For $f \in C^1(\RR; \RR)$ with $f'(a) \neq 0$, then $f$ is invertible in a neighborhood $U \ni a$, $g\da f\inv \in C^1(U; \RR)$, and at $b\da f(a)$ the derivative of $g$ is given by
\[
g'(b) = {1 \over f'(a)}
.\]
For $F \in C^1(\RR^n, \RR^n)$ with $D_f$ invertible in a neighborhood of $a$, so $\det(J_f)\neq 0$, then setting $b\da F(a)$,
\[
J_{F\inv}(q) = \qty{J_F(p)}\inv
.\]

The version for holomorphic functions: if $f\in \Hol(\CC; \CC)$ with $f'(p)\neq 0$ then there is a neighborhood $V\ni p$ with that $f\in \BiHol(V, f(V))$.
:::

:::{.slogan}
A $C^1$ function is invertible in any neighborhood in which its derivative $f'$ is invertible.
:::

:::{.remark}
Recall that absolutely convergent implies convergent, but not conversely: $\sum k\inv = \infty$ but $\sum (-1)^k k\inv < \infty$.
This converges because the even (odd) partial sums are monotone increasing/decreasing respectively and in $(0, 1)$, so they converge to a finite number.
Their difference converges to 0, and their common limit is the limit of the sum.
:::

## Integrals

### Green's Theorem

:::{.theorem title="Green's Theorem"}
If $\Omega \subseteq \CC$ is bounded with $\bd \Omega$ piecewise smooth and $f, g\in C^1(\bar \Omega)$, then 
$$\int_{\bd \Omega} f\, dx + g\, dy = \iint_{\Omega} \qty{ \dd{g}{x} - \dd{f}{y} } \, \dA.$$
In vector form,
\[
\int_\gamma F\cdot \dr = \iint_R \curl F \dA
.\]
As a consequence, areas can be computed as
\[
\mu(\Omega) = {1\over 2}\oint_{\bd\Omega} \qty{y\dx - x\dy} = \oint_{\bd \Omega} x\dy = -\oint_{\bd \Omega} y\dx
.\]

> In general, $\mu(\Omega) = \int_{\Omega} \abs{f'(z)} \dz$.

:::

:::{.remark}
Some basic facts needed for line integrals in the plane:

- Green's theorem requires $C^1$ partial derivatives.
- $\grad f = \tv{ \dd{f}{x}, \dd{f}{y} }$.
  - If $F = \grad f$ for some $f$, $F$ is a vector field.
- Given $f(x, y)$ and $\gamma(t)$, the chain rule yields $\dd{}{t} (f\circ \gamma)(t) = \inner{ \grad f\circ \gamma)(t)} {\gamma'(t)}$.
- For $F(x, y) = \tv{M(x, y), N(x, y)}$, $\curl F = \dd{N}{x} - \dd{M}{y}$ and $\div F = \dd{M}{x} + \dd{N}{y}$.
- $\int_\gamma F\cdot \dr = \int_a^b F(\gamma(t))\cdot \gamma'(t) \dt$.

:::

### Stokes Theorem
:::{.theorem title="Stokes Theorem"}
Suppose $\omega \da f(z)\dz$ is a differential 1-form on an orientable manifold $\Omega$, then 
$$\int_{\bd\Omega}\omega = \int_\Omega d\omega \qquad \text{i.e.} \qquad \int_{\bd\Omega}f(z)\dz = \int_\Omega d(f(z)\dz)$$
:::

## Series and Sequences

:::{.fact title="Partial Fraction Decomposition"}
\envlist

- For every root $r_i$ of multiplicity 1, include a term $A/(x-r_i)$.
- For any factors $g(x)$ of multiplicity $k$, include terms $A_1/g(x), A_2/g(x)^2, \cdots, A_k / g(x)^k$.
- For irreducible quadratic factors $h_i(x)$, include terms of the form ${Ax+B \over h_i(x)}$.
:::

:::{.proposition title="Uniform Convergence of Series"}
A series of functions $\sum_{n=1}^\infty f_n(x)$ converges uniformly iff 
\[  
\lim_{n\to \infty} \norm{ \sum_{k\geq n} f_k }_\infty = 0
.\]
:::

:::{.theorem title="Weierstrass $M\dash$Test"}
If $\theset{f_n}$ with $f_n: \Omega \to \CC$ and there exists a sequence $\theset{M_n}$ with $\norm{f_n}_\infty \leq M_n$ and $\sum_{n\in \NN} M_n < \infty$, then $f(x) \definedas \sum_{n\in \NN} f_n(x)$ converges absolutely and uniformly on $\Omega$. 
Moreover, if the $f_n$ are continuous, by the uniform limit theorem, $f$ is again continuous.
:::

:::{.remark}
Note that if a power series converges uniformly, then summing commutes with integrating or differentiating.
:::

:::{.proposition title="Ratio Test"}
Consider $\sum c_k z^k$, set $R = \lim \abs{c_{k+1} \over c_k}$, and recall the **ratio test**:

- $R\in (0, 1) \implies$ convergence.
- $R\in (1, \infty] \implies$ divergence.
- $R=1$ yields no information.
:::

:::{.proposition title="Root Test"}
![figures/image_2021-05-27-15-40-58.png](../../../assets/figures/image_2021-05-27-15-40-58.png)
:::

:::{.proposition title="Radius of Convergence by the Root Test"}
For $f(z) = \sum_{k\in \NN} c_k z^k$, defining
\[
{1\over R} \da \limsup_{k} \abs{a_k}^{1\over k}
,\]
then $f$ converges absolutely and uniformly for $D_R \da\abs{z} < R$ and diverges for $\abs{z} > R$.
So the radius of convergence is given by
\[
R = {1\over \limsup_n \abs{a_n}^{1\over n}}
.\]

Moreover $f$ is holomorphic in $D_R$, can be differentiated term-by-term, and $f' = \sum_{k\in \NN} n c_k z^k$.
:::

:::{.proposition title="The $p\dash$test"}
Recall the **$p\dash$test**:
\[
\sum n^{-p} < \infty \iff p \in (1, \infty)
.\]
:::

## Function Convergence

:::{.definition title="Locally uniform convergence"}
A sequence of functions $f_n$ is said to converge **locally uniformly** on $\Omega \subseteq \CC$ iff $f_n\to f$ uniformly on every compact subset $K \subseteq \Omega$.
:::

## Exercises

[[E-2JGJL]]
[[E-CLMEK]]
[[E-DXXL4]]
[[E-6ULIT]]
[[E-5KI4G]]
[[E-4P3T2]]
[[E-XXUNZ]]
