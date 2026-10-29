---
schema: qual/card@1
id: E-BV7DD
kind: problem
title: Polynomials cannot uniformly approximate $z^{-m}$ on an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Polynomials
  - Uniform Convergence
  - Laurent Series
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states (1) for every polynomial p and (2) for K = {r <= |z| <= R} with only r < R. Part (1) fails for p = 0, where M_R = 1, and z^{-m} is undefined on K unless r > 0; the statement takes p nonzero in (1) and 0 < r < R in (2).'
---

::: {.problem}
(1) Let $p(z)$ be a nonzero polynomial, $R>0$ any positive number, and $m \geq 1$ an integer.
Let $M_R = \sup \theset{ \abs{z^{m} p(z) - 1}: \abs{z} = R }$.
Show that $M_R>1$.

(2) Let $m \geq 1$ be an integer and $K = \theset{z \in \CC: r \leq \abs{z} \leq R }$ where $0<r<R$.
Show (i) using (1) as well as, (ii) without using (1) that there exists a positive number $\varepsilon_0>0$ such that for each polynomial $p(z)$, $$\sup \theset{\abs{p(z) - z^{-m}}: z \in K } \geq \varepsilon_0.$$
:::

::: {.solution}
Let $f(z) = z^m p(z) - 1$, let $S_p\coloneqq\sup_{z \in K} \abs{p(z) - z^{-m}}$, and let $\gamma_\rho$ be the circle $z = \rho e^{i\theta}$, $0\le\theta\le2\pi$, of radius $\rho = \frac{r+R}{2}$, which lies in $K$.

::: pf

::: pf-step
(1) $M_R>1$ for every nonzero polynomial $p$.

::: pf-proof

::: {.pf-step #f-props}
$f$ is a nonconstant polynomial with $\abs{f(0)} = 1$.

::: pf-proof
$f(0) = 0^m p(0) - 1 = -1$ since $m\ge1$, and $z^m p(z)$ has degree $m + \deg(p) \ge 1$.
:::

:::

::: pf-qed
By step [](#f-props){.pf-ref} and the maximum modulus principle on the closed disc $\overline{D(0,R)}$, the modulus of $f$ at the interior point $0$ is strictly less than its maximum on the circle $\abs z=R$, so $M_R > \abs{f(0)} = 1$.
:::

:::

:::

::: pf-step
(2)(i) $S_p\geq\varepsilon_0\coloneqq R^{-m}$ for every polynomial $p$.

::: pf-proof
If $p\equiv0$, then $S_p=r^{-m}>R^{-m}$.
Otherwise, on the circle $\abs z=R$, which lies in $K$,
$$
\abs{p(z) - z^{-m}} = \frac{\abs{z^m p(z) - 1}}{R^m},
$$
so $S_p \geq M_R/R^m>R^{-m}$ by (1).
:::

:::

::: pf-step
(2)(ii) $S_p\geq\varepsilon_0\coloneqq\rho^{-m} = \qty{\frac{2}{r+R}}^m$ for every polynomial $p$.

::: pf-proof

::: {.pf-step #contour-integral-value}
$\oint_{\gamma_\rho} \qty( p(z) - z^{-m} ) z^{m-1} \, dz = -2\pi i$.

::: pf-proof
The integral is $\oint_{\gamma_\rho} p(z) z^{m-1} \, dz - \oint_{\gamma_\rho} \frac{dz}{z}$.
The first integral vanishes by Cauchy's theorem, since $p(z)z^{m-1}$ is a polynomial, and the second equals $2\pi i$.
:::

:::

::: pf-qed
On $\gamma_\rho$, $\abs{z^{m-1}} = \rho^{m-1}$, and $\gamma_\rho$ has length $2\pi \rho$.
By step [](#contour-integral-value){.pf-ref} and the $ML$-inequality,
$$
2\pi = \abs{ \oint_{\gamma_\rho} \qty( p(z) - z^{-m} ) z^{m-1} \, dz } \leq S_p \cdot \rho^{m-1} \cdot 2\pi \rho = 2\pi \rho^m S_p.
$$
:::

:::

:::

:::

:::
