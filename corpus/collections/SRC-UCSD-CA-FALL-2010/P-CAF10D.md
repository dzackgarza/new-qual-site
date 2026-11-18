---
schema: qual/card@1
id: P-CAF10D
kind: problem
title: "Rational function and polynomial approximation of a rational function on an annulus"
classification:
  areas:
  - complex-analysis
  topics:
  - Annuli
  - Laurent Series
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: R has poles 0 and
    3i, both off the annulus; the complement of K has two components, met at 1/3 and 3,
    which is what Runge's theorem needs for part (a); and part (b) now carries the three
    computations separately — vanishing of the polynomial integral, the residue at 0 of
    1/(z(z-3i)) equal to i/3 so the integral is -2pi/3, and the limit of integrals forced
    by uniform convergence on the circle. The collection's provenance is the examination
    paper only, so no retained solution set covers the exercise and the argument is the
    card's own.
---

::: {.problem}
Consider the rational function $R(z) := \frac{1}{z(z - 3i)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ with poles at $1/3$ and $3$ such that $$\lim_{n \to \infty} \sup_{1 \leq \abs{z} \leq 2} \abs{R(z) - R_n(z)} = 0.$$

(b) Does there exist a sequence of polynomials $R_n(z)$ such that the above holds?
Prove your assertion.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Throughout, $K\coloneqq\{z:1\le\abs{z}\le2\}$, a compact set.

::: pf

::: {.pf-step #holomorphic}
$R(z)=\frac{1}{z(z-3i)}$ is holomorphic on an open neighbourhood of $K$.

::: pf-proof
The only poles of $R$ are the zeros of its denominator, namely $0$ and $3i$. Both lie off $K$, since $\abs{0}<1$ and $\abs{3i}=3>2$, and they are at distance at least $1$ from $K$; hence the open annulus $\{z:1/2<\abs{z}<7/2\}$ contains $K$ and misses both poles, and $R$ is holomorphic there.
:::

:::

::: {.pf-step #components}
$\CC\setminus K$ has exactly two connected components, $\{z:\abs{z}<1\}$ and $\{z:\abs{z}>2\}$, and the prescribed points $\frac13$ and $3$ lie in the first and in the second respectively.

::: pf-proof
$\{z:\abs{z}<1\}$ and $\{z:\abs{z}>2\}$ are open, connected and disjoint, and their union is the complement of the closed annulus $K$; so they are the two components. $\abs{1/3}<1$ and $\abs{3}=3>2$.
:::

:::

::: {.pf-step}
(a) There are rational functions $R_n$ with poles only at $\frac13$ and $3$ such that $\sup_{1\le\abs{z}\le2}\abs{R(z)-R_n(z)}\to0$.

::: pf-proof
Let $S\coloneqq\{\frac13,3\}$, which by step [](#components){.pf-ref} meets every component of $\CC\setminus K$. Runge's theorem, in the form for a compact set whose complement has finitely many components, states that every function holomorphic on an open neighbourhood of $K$ is the uniform limit on $K$ of rational functions with poles in $S$. Step [](#holomorphic){.pf-ref} provides such a neighbourhood, on which $R$ is holomorphic, so there are rational functions $R_n$, with poles only at $\frac13$ and $3$, satisfying $\sup_K\abs{R-R_n}\to0$.
:::

:::

::: {.pf-step}
(b) No sequence of polynomials converges uniformly to $R$ on $K$.

::: pf-proof

::: {.pf-step #circle}
For every $\rho$ with $1<\rho<2$ and every polynomial $P$, one has $\sup_{\abs{z}=\rho}\abs{P(z)-R(z)}\le\sup_{z\in K}\abs{P(z)-R(z)}$.

::: pf-proof
Every $z$ with $\abs{z}=\rho$ satisfies $1\le\rho\le2$, hence belongs to $K$, so the supremum over the circle is at most the supremum over $K$.
:::

:::

::: {.pf-step #vanishing-integrals}
$\int_{\abs{z}=\rho}P(z)\,dz=0$ for every polynomial $P$ and every $\rho>0$.

::: pf-proof
A polynomial $P(z)=\sum_{k=0}^{d}c_kz^k$ has the primitive $\sum_{k=0}^{d}\frac{c_k}{k+1}z^{k+1}$, entire, so its integral over the closed curve $\abs{z}=\rho$ vanishes.
:::

:::

::: {.pf-step #residue-integral}
For $0<\rho<3$,
$$
\int_{\abs{z}=\rho}R(z)\,dz=2\pi i\operatorname{Res}(R,0)=-\frac{2\pi}{3}.
$$

::: pf-proof
The circle $\abs{z}=\rho$, traversed once counterclockwise, encloses $0$ and not $3i$, because $\abs{3i}=3>\rho$. So the residue theorem gives the integral as $2\pi i$ times the residue at $0$. Now $R(z)=\frac1z\cdot\frac{1}{z-3i}$, and $z\mapsto\frac{1}{z-3i}$ is analytic near $0$ with value $\frac{1}{-3i}=\frac{i}{3}$ there, so $\operatorname{Res}(R,0)=\frac{i}{3}$ and $2\pi i\cdot\frac{i}{3}=-\frac{2\pi}{3}\ne0$.
:::

:::

::: {.pf-step}
$R$ is not a uniform limit of polynomials on $K$.

::: pf-proof
Suppose $P_n\to R$ uniformly on $K$ and fix $\rho$ with $1<\rho<2$. By step [](#circle){.pf-ref}, $\sup_{\abs{z}=\rho}\abs{P_n-R}\to0$, and
$$
\abs{\int_{\abs{z}=\rho}P_n\,dz-\int_{\abs{z}=\rho}R\,dz}\le2\pi\rho\sup_{\abs{z}=\rho}\abs{P_n-R}\longrightarrow0,
$$
so $\int_{\abs{z}=\rho}P_n\,dz\to\int_{\abs{z}=\rho}R\,dz$. Steps [](#vanishing-integrals){.pf-ref} and [](#residue-integral){.pf-ref} compute the two sides as $0$ and $-\frac{2\pi}{3}$, which is impossible. Hence no such sequence of polynomials exists.
:::

:::

:::

:::

:::
:::
