---
schema: qual/card@1
id: P-VQUPX
kind: problem
title: Taylor coefficients of an entire function as contour integrals, uniform convergence
  on bounded sets, and uniform convergence on $\mathbb{C}$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Cauchy Integral Formula
  - Uniform Convergence
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is entire and has Taylor series $\sum a_n z^n$ about 0.

a. Express $a_n$ as a contour integral along the circle $\abs{z} = R$.

b. Apply (a) to show that the above Taylor series converges uniformly on every bounded subset of $\CC$.

c. Determine those functions $f$ for which the above Taylor series converges uniformly on all of $\CC$.
:::

::: {.solution}
(a) Cauchy's coefficient formula gives, for every $R>0$,
\[
\boxed{a_n=\frac1{2\pi i}\int_{|\zeta|=R}
\frac{f(\zeta)}{\zeta^{n+1}}\,d\zeta.}
\]

(b) Fix a bounded set $E\subset\mathbb C$ and choose $r,R$ with
$E\subset\{|z|\le r\}$ and $R>r$. If
$M_R=\max_{|\zeta|=R}|f(\zeta)|$, then (a) yields
\[
|a_n|\le \frac{M_R}{R^n}.
\]
Thus for $z\in E$,
\[
|a_nz^n|\le M_R(r/R)^n.
\]
The geometric majorant is summable, so the Weierstrass $M$-test gives uniform
convergence on $E$.

(c) Uniform convergence on all of $\mathbb C$ occurs exactly when $f$ is a
polynomial. Indeed, if $\sum a_nz^n$ converges uniformly on $\mathbb C$, then
its terms tend uniformly to zero. Hence for each $n$ sufficiently large,
\[
\sup_{z\in\mathbb C}|a_nz^n|<1.
\]
If $a_n\ne0$ and $n>0$, that supremum is infinite, a contradiction. Therefore
all sufficiently large coefficients vanish, so $f$ is a polynomial. The
converse is immediate because the partial sums are eventually equal to $f$.
:::
