---
order: 5
title: Calculus Preliminaries
---

# Calculus Preliminaries

## Definitions

## Derivatives 

[[PR-5ZSSQ]]

:::{.proof}
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

[[T-QMGPN]]

:::{.slogan}
A relation is locally the graph of a function wherever the derivative is nonsingular.

:::

### Inverse Function Theorem

[[T-XECJ3]]

[[T-JH6VL]]

## Convergence

:::{.slogan}
A $C^1$ function is invertible in any neighborhood in which its derivative $f'$ is invertible.

:::

:::{.remark}
Recall that absolutely convergent implies convergent, but not conversely: $\sum k\inv = \infty$ but $\sum (-1)^k k\inv < \infty$.
This converges because the even (odd) partial sums are monotone increasing/decreasing respectively and in $(0, 1)$, so they converge to a finite number.
Their difference converges to 0, and their common limit is the limit of the sum.

:::

## Integrals

:::{.remark}
Some basic facts needed for line integrals in the plane:

- $\grad f = \tv{ \dd{f}{x}, \dd{f}{y} }$.
  - If $F = \grad f$ for some $f$, $F$ is a vector field.
- Given $f(x, y)$ and $\gamma(t)$, the chain rule yields $\dd{}{t} (f\circ \gamma)(t) = \inner{ \grad f\circ \gamma)(t)} {\gamma'(t)}$.
- For $F(x, y) = \tv{M(x, y), N(x, y)}$, $\curl F = \dd{N}{x} - \dd{M}{y}$ and $\div F = \dd{M}{x} + \dd{N}{y}$.
- $\int_\gamma F\cdot \dr = \int_a^b F(\gamma(t))\cdot \gamma'(t) \dt$.

:::

### Green's Theorem

[[T-4M73O]]

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
[[T-LO7QM]]

## Series and Sequences

:::{.fact title="Partial Fraction Decomposition"}
\envlist

- For every root $r_i$ of multiplicity 1, include a term $A/(x-r_i)$.
- For any factors $g(x)$ of multiplicity $k$, include terms $A_1/g(x), A_2/g(x)^2, \cdots, A_k / g(x)^k$.
- For irreducible quadratic factors $h_i(x)$, include terms of the form ${Ax+B \over h_i(x)}$.

:::

[[PR-4LISY]]

[[T-AZSCN]]

:::{.remark}
Note that if a power series converges uniformly, then summing commutes with integrating or differentiating.

:::

[[PR-WIMIM]]

[[PR-TOK44]]

[[PR-NQ64T]]

:::{.fact}
Recall the **$p\dash$test**:
\[
\sum n^{-p} < \infty \iff p \in (1, \infty)
.\]

:::
:::{.fact}
The product of two sequences is given by the Cauchy product
\[
\sum a_kz^k \cdot \sum b_k z^k = \sum c_k z^k,\quad c_k \da \sum_{j\leq k} a_k b_{k-j}
.\]

:::
:::{.fact}
Recall how to carry out polynomial long division:

:::

[[PR-5WUAP]]

## Function Convergence

[[D-AIQG3]]

[[D-5Y4MC]]

:::{.remark}
Recall Arzelà-Ascoli, an analog of Heine-Borel: for $X$ compact Hausdorff, consider the the Banach space $C(X; \RR)$ equipped with the *uniform norm* $\norm{f}_{\infty, X} \da \sup_{x\in X} \abs{f(x)}$.
Then a subset $A \subseteq X$ is compact iff $A$ is closed, uniformly bounded, and equicontinuous.
As a consequence, if $A$ is a sequence, it contains a subsequence converging uniformly to a continuous function.
The proof is an $\eps/3$ argument.

:::
[[D-QTJ7T]]

:::{.remark}
A continuous function on a compact set is uniformly continuous.

:::
[[D-HL4KE]]

:::{.remark}
If $f: \Omega \to \Omega'$ is a univalent surjection, $f$ is invertible on $\Omega$ and $f\inv$ is holomorphic.
Compare to real functions: $f(x) = x^3$ is injective on $(-c, c)$ for any $c$ but $f'(0) = 0$ and $f\inv(x) \da x^{1/3}$ is not differentiable at zero.

:::
## Theorems
[[T-TUXBP]]

## Exercises

[[E-5GT6F]]

[[E-2JGJL]]
[[E-CLMEK]]
[[E-DXXL4]]
[[E-6ULIT]]
[[E-5KI4G]]
[[E-4P3T2]]
[[E-XXUNZ]]
