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
---

::: problem
Consider the rational function $R(z) := \frac{1}{z(z - 3i)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ with poles at $1/3$ and $3$ such that $$\lim_{n \to \infty} \sup_{1 \leq |z| \leq 2} |R(z) - R_n(z)| = 0.$$

(b) Does there exist a sequence of polynomials $R_n(z)$ such that the above holds?
Prove your assertion.
:::

::: solution
Let
\[
K=\{z:1\le |z|\le2\}.
\]
The function $R$ is holomorphic on a neighborhood of $K$, since its poles are
$0$ and $3i$.

For part (a), the complement $\mathbb C\setminus K$ has exactly two connected
components, namely $\{|z|<1\}$ and $\{|z|>2\}$. The prescribed points
$1/3$ and $3$ lie in these two components. By Runge's theorem, rational
functions whose poles are allowed only at one chosen point of each component of
$\mathbb C\setminus K$ are uniformly dense on $K$ in the functions holomorphic
near $K$. Hence there are rational functions $R_n$ with poles only at $1/3$
and $3$ such that
\[
\sup_{1\le |z|\le2}|R(z)-R_n(z)|\longrightarrow0.
\]

For part (b), suppose instead that polynomials $P_n$ converged uniformly to $R$
on $K$. Fix any $\rho\in(1,2)$. Uniform convergence on the circle
$|z|=\rho$ would imply
\[
\int_{|z|=\rho}P_n(z)\,dz
\longrightarrow
\int_{|z|=\rho}R(z)\,dz.
\]
The left side is $0$ for every $n$. On the other hand, the circle encloses the
pole at $0$ but not the pole at $3i$, so
\[
\int_{|z|=\rho}R(z)\,dz
=2\pi i\operatorname{Res}(R,0)
=2\pi i\left(\frac1{-3i}\right)
=-\frac{2\pi}{3}\ne0.
\]
This contradiction shows that no such polynomial sequence exists.
:::
