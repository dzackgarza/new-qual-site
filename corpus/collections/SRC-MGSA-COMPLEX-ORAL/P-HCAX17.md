---
schema: qual/card@1
id: P-HCAX17
kind: problem
title: Laurent coefficients and growth on a punctured disk
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Isolated Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the three parts already on the card, whose estimates and
    conclusions are correct. Added: the Laurent theorem's annulus and the independence of the
    coefficients from the radius, which the card used silently; the derivation of Cauchy's
    estimate from the coefficient formula with the length of the circle; the passage through the
    Hadamard formula in moving from limsup bounds to radii of convergence, in both parts of (b);
    and the naming of Riemann's removable-singularity theorem in (c). Not claimed: a retained
    solution set; the collection's provenance is the oral examination compilation.
---

::: {.problem}
Let $f$ be holomorphic on the punctured unit disk.

(a) Write the Laurent expansion of $f$ and give bounds on its coefficients in terms of the values of $f$ on circles.

(b) Relate these bounds to the radii of convergence of the positive and negative parts.

(c) What additional conclusions follow if $f$ is bounded?
:::

::: {.solution}
Throughout $f$ is holomorphic on the punctured disc $\theset{0 < \abs{z} < 1}$, $M(r) \coloneqq \max_{\abs{\zeta} = r}\abs{f(\zeta)}$ for $0 < r < 1$, and $w \coloneqq 1/z$. The collection's `provenance` is the oral-examination compilation, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #laurent}
(a) $f(z) = \sum_{n = -\infty}^{\infty}a_{n}z^{n}$ on $0 < \abs{z} < 1$, with $a_{n} = \frac{1}{2\pi i}\int_{\abs{\zeta} = r}\frac{f(\zeta)}{\zeta^{n+1}}\\,d\zeta$ for every $0 < r < 1$.

::: pf-proof
For a fixed $r$ with $0 < r < 1$ and $\rho$ with $r < \rho < 1$, the Laurent theorem on the annulus $r \le \abs{z} \le \rho$, whose inner and outer boundary circles both lie in the domain of $f$, gives the expansion and the coefficient formula with the integral over $\abs{\zeta} = \rho$. The Cauchy theorem for the annulus, applied to $f(\zeta)/\zeta^{n+1}$, shows the integral does not change when $\rho$ is replaced by any other radius in $(0,1)$, so the coefficients are independent of $r$.

:::

:::

::: {.pf-step #cauchy}
(a) $\abs{a_{n}} \le M(r)r^{-n}$ for every $n \in \ZZ$ and every $0 < r < 1$.

::: pf-proof
This is Cauchy's estimate applied to the coefficient formula of step [](#laurent){.pf-ref}: on the circle $\abs{\zeta} = r$ the integrand is $f(\zeta)\zeta^{-n-1}$, whose modulus is at most $M(r)r^{-n-1}$, and the circle has length $2\pi r$, so $\abs{a_{n}} \le \frac{1}{2\pi}\cdot M(r)r^{-n-1}\cdot 2\pi r = M(r)r^{-n}$.

:::

:::

::: {.pf-step #positive}
(b) The series $\sum_{n \ge 0}a_{n}z^{n}$ has radius of convergence at least $1$.

::: pf-proof
Fix $0 < r < 1$. By step [](#cauchy){.pf-ref}, $\abs{a_{n}} \le M(r)r^{-n}$ for $n \ge 0$, so $\abs{a_{n}}^{1/n} \le M(r)^{1/n}r^{-1}$, whose limsup as $n \to \infty$ is at most $r^{-1}$ because $M(r) \ge 0$ has a constant $n$-th root in the limit. Hence $\limsup_{n}\abs{a_{n}}^{1/n} \le r^{-1}$, and letting $r \uparrow 1$ gives a limsup at most $1$, which is the Hadamard formula's statement that the radius of convergence is at least $1$.

:::

:::

::: {.pf-step #negative}
(b) The series $\sum_{m \ge 1}a_{-m}w^{m}$ has infinite radius of convergence, so the negative part converges for every $z \ne 0$.

::: pf-proof
Putting $m = -n$ in step [](#cauchy){.pf-ref} gives $\abs{a_{-m}} \le M(r)r^{m}$ for every $0 < r < 1$, hence $\abs{a_{-m}}^{1/m} \le M(r)^{1/m}r$, whose limsup is at most $r$ for each fixed $r$. Since $r > 0$ was arbitrary, $\limsup_{m}\abs{a_{-m}}^{1/m} = 0$, and a zero limsup is exactly the Hadamard statement that the radius of convergence of the series in $w$ is infinite.

:::

:::

::: {.pf-step #bounded}
(c) If $\abs{f} \le B$ on the punctured disc then $a_{n} = 0$ for every $n < 0$.

::: pf-proof
Take $M(r) \le B$ in step [](#cauchy){.pf-ref} with $n = -m < 0$: $\abs{a_{-m}} \le Br^{m}$ for every $0 < r < 1$, and letting $r \downarrow 0$ gives $a_{-m} = 0$.

:::

:::

::: pf-step
(c) If $f$ is bounded then the singularity at $0$ is removable and $f$ extends holomorphically to $\DD$, with $f(z) = \sum_{n \ge 0}a_{n}z^{n}$ there.

::: pf-proof
By step [](#bounded){.pf-ref} the principal part vanishes, so the expansion of step [](#laurent){.pf-ref} is a power series in $z$; by step [](#positive){.pf-ref} it converges on $\DD$, and on the punctured disc it sums to $f$. Defining $f(0)$ as the constant term therefore gives a holomorphic extension, which is the removable-singularity statement of Riemann.

:::

:::

:::
:::
