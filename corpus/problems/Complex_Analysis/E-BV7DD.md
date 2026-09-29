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
---

::: {.problem}
(1) Let $p(z)$ be a polynomial, $R>0$ any positive number, and $m \geq 1$ an integer.
Let $M_R = \sup \{ |z^{m} p(z) - 1|: |z| = R  \}$.
Show that $M_R>1$.

(2) Let $m \geq 1$ be an integer and $K = \{z \in {\mathbb C}: r \leq |z| \leq R \}$ where $r<R$.
Show (i) using (1) as well as, (ii) without using (1) that there exists a positive number $\varepsilon_0>0$ such that for each polynomial $p(z)$, $$\sup \{|p(z) - z^{-m}|: z \in K  \} \geq \varepsilon_0 \, .$$
:::

::: {.solution}
Throughout, $0<r<R$, so that $z^{-m}$ is defined on $K$. Let $f(z) = z^m p(z) - 1$.

**Part (1).**

::: pf

::: {.pf-step #f-value-at-zero}
$f$ is a polynomial with $\abs{f(0)} = 1$.

::: pf-proof
$z^m p(z) - 1$ is a polynomial, and $f(0) = 0^m p(0) - 1 = -1$ since $m\ge1$.
:::

:::

::: {.pf-step #f-nonconstant}
If $p \not\equiv 0$, then $f$ is nonconstant.

::: pf-proof
The term $z^m p(z)$ has degree $m + \deg(p) \ge 1$.
:::

:::

::: pf-qed
Let $p\not\equiv0$. By step [](#f-nonconstant){.pf-ref} and the maximum modulus principle on the closed disk $\overline{D(0,R)}$, the modulus of $f$ at the interior point $0$ is strictly less than its maximum on the circle $\abs z=R$. By step [](#f-value-at-zero){.pf-ref}, $M_R > \abs{f(0)} = 1$. The remark treats $p\equiv0$.
:::

:::

**Part (2)(i).**

::: pf

::: {.pf-step #lower-bound-on-circle-R}
For every polynomial $p$, $\sup_{z \in K} |p(z) - z^{-m}| \geq R^{-m}$.

::: pf-proof
On the circle $\abs z=R$, which lies in $K$,
$$|p(z) - z^{-m}| = \frac{|z^m p(z) - 1|}{|z|^m} = \frac{|z^m p(z) - 1|}{R^m},$$
so $\sup_{z \in K} |p(z) - z^{-m}| \geq M_R/R^m$. If $p\not\equiv0$, Part (1) gives $M_R>1$. If $p\equiv0$, then $\sup_{z\in K}\abs{z^{-m}}=r^{-m}>R^{-m}$.
:::

:::

::: pf-qed
Step [](#lower-bound-on-circle-R){.pf-ref} gives the bound with $\varepsilon_0 = R^{-m}$.
:::

:::

**Part (2)(ii).** Let $\rho = \frac{r+R}{2}$ and let $\gamma_\rho$ be the circle $z = \rho e^{i\theta}$, $0\le\theta\le2\pi$, which lies in $K$. Let $S = \sup_{z \in K} |p(z) - z^{-m}|$.

::: pf

::: {.pf-step #contour-integral-value}
$\oint_{\gamma_\rho} \big( p(z) - z^{-m} \big) z^{m-1} \, dz = -2\pi i$ for every polynomial $p$.

::: pf-proof
By linearity the integral is $\oint_{\gamma_\rho} p(z) z^{m-1} \, dz - \oint_{\gamma_\rho} \frac{dz}{z}$. The first integral vanishes by Cauchy's theorem, since $p(z)z^{m-1}$ is a polynomial, and the second equals $2\pi i$.
:::

:::

::: {.pf-step #lower-bound-rho}
$S\geq\rho^{-m}$.

::: pf-proof
On $\gamma_\rho$, $|z^{m-1}| = \rho^{m-1}$, and $\gamma_\rho$ has length $2\pi \rho$. By step [](#contour-integral-value){.pf-ref} and the $ML$-inequality,
$$2\pi = \left| \oint_{\gamma_\rho} \big( p(z) - z^{-m} \big) z^{m-1} \, dz \right| \leq S \cdot \rho^{m-1} \cdot 2\pi \rho = 2\pi \rho^m S.$$
:::

:::

::: pf-qed
Step [](#lower-bound-rho){.pf-ref} gives the bound with $\varepsilon_0 = \rho^{-m} = \left(\frac{2}{r+R}\right)^m$, which depends only on $r$, $R$ and $m$.
:::

:::

::: {.remark}
Part (1) requires $p\not\equiv0$: for $p\equiv0$, $z^mp(z)-1\equiv-1$ and $M_R=1$. Part (2) holds for every polynomial, including $p\equiv0$.
:::
