---
schema: qual/card@1
id: P-EH22O
kind: problem
title: Area of $f(\{|z|<r\})$ is $\pi\sum_{n=1}^\infty n|c_n|^2 r^{2n}$ for univalent
  $f(z)=\sum_{n=0}^\infty c_n z^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
---

::: problem
Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be analytic and one-to-one in $|z| < 1$.
For $0<r<1$, let $D_r$ be the disk $|z|<r$.
Show that the area of $f(D_r)$ is finite and is given by $$S = \pi \sum_{n=1}^\infty n |c_n|^2 r^{2n}.$$ (Note that in general the area of $f(D_1)$ is infinite.)
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f(z) = \sum_{n=0}^\infty c_n z^n$ analytic and one-to-one in $\abs{z} < 1$, show the area of $f(D_r)$, $0 < r < 1$, is finite and equals $S = \pi \sum_{n=1}^\infty n\abs{c_n}^2 r^{2n}$.

<1>1. The area of $f(D_r)$ equals $\iint_{D_r} \abs{f'(z)}^2\, dA(z)$.
Proof: $f$ is injective and holomorphic on $D_r$, so it is a $C^1$ diffeomorphism onto its image with Jacobian $\abs{\det J_f} = \abs{f'}^2$ (the Cauchy–Riemann equations make the Jacobian $\abs{f'}^2$); the change-of-variables formula gives $\mathrm{Area}(f(D_r)) = \int_{f(D_r)} 1\, dA = \int_{D_r} \abs{f'}^2\, dA$.

<1>2. $f'(z) = \sum_{n=1}^\infty n c_n z^{n-1}$, converging uniformly on compact subsets of $D_1$.
Proof: Term-by-term differentiation of the power series is valid inside the radius of convergence, which is at least $1$ since $f$ is analytic in $\DD$.

<1>3. $\iint_{D_r} \bar{z}^{m} z^{n}\, dA(z) = 0$ for $m \neq n$, and $\iint_{D_r} \abs{z}^{2k}\, dA(z) = \frac{2\pi r^{2k+2}}{2k+2}$.
Proof: In polar coordinates $z = \rho e^{i\theta}$, $\iint_{D_r} z^n \bar{z}^m\, dA = \int_0^r \rho^{n+m+1} d\rho \int_0^{2\pi} e^{i(n-m)\theta} d\theta$, and $\int_0^{2\pi} e^{ik\theta} d\theta = 0$ for $k \neq 0$, $2\pi$ for $k = 0$.

<1>4. $\iint_{D_r} \abs{f'(z)}^2\, dA = \sum_{n=1}^\infty n^2\abs{c_n}^2 \cdot \frac{2\pi r^{2n}}{2n}$.
Proof: Expand $\abs{f'}^2 = \qty(\sum n c_n z^{n-1})\qty(\sum m \bar{c_m} \bar{z}^{m-1})$; by <1>3 the cross terms with $n \neq m$ integrate to zero, and $\iint_{D_r} \abs{z}^{2n-2}\, dA = \frac{2\pi r^{2n}}{2n}$ by <1>3 with $k = n-1$.
Uniform convergence on $\overline{D_r}$ justifies integrating the (absolutely convergent) product term by term; the series is finite by <1>5.

<1>5. The series $\sum_{n=1}^\infty n\abs{c_n}^2 r^{2n}$ converges.
Proof: Since $f$ is analytic in $\DD$, $\abs{c_n} s^n \to 0$ for every $s < 1$; fixing $s$ with $r < s < 1$, $\abs{c_n} \leq M s^{-n}$, so $n\abs{c_n}^2 r^{2n} \leq M^2 n (r/s)^{2n}$, a convergent geometric-type series.

<1>6. Q.E.D. Proof: <1>1, <1>4 and <1>5 give $\mathrm{Area}(f(D_r)) = \sum_{n\geq1} n^2\abs{c_n}^2 \frac{2\pi r^{2n}}{2n} = \pi\sum_{n\geq1} n\abs{c_n}^2 r^{2n}$, finite as claimed.
:::
