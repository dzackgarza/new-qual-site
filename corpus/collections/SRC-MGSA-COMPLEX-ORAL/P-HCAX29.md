---
schema: qual/card@1
id: P-HCAX29
kind: problem
title: Local power-series expansions of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the disc of radius
    below dist(a, boundary) lies in the domain; Cauchy's integral formula applies with z inside
    the circle; the geometric series converges uniformly in zeta by the M-test with ratio
    |z-a|/R < 1; term-by-term integration gives the coefficients as contour integrals; Cauchy's
    differentiation formula identifies them as f^(n)(a)/n!. Added the case dist = infinity and
    the uniform-convergence estimate that licenses the termwise step, which the prose asserted.
    The statement is true as printed. The collection's provenance is the examination paper only,
    so no retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Prove that every holomorphic function has a convergent power-series expansion about each point of its domain.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #disc}
For each $a$ in the domain $\Omega$ and each $R$ with $0<R<\operatorname{dist}(a,\partial\Omega)$, the closed disc $\overline{D(a,R)}$ lies in $\Omega$.

::: pf-proof
If $\operatorname{dist}(a,\partial\Omega)=\infty$, as for $\Omega=\CC$, the claim is immediate. Otherwise every point $z$ with $\abs{z-a}\le R<\operatorname{dist}(a,\partial\Omega)$ is at distance less than the distance from $a$ to the boundary, so $z\in\Omega$; $\Omega$ being open, its boundary is disjoint from $\Omega$ itself.
:::

:::

::: {.pf-step #cauchy}
For $\abs{z-a}<R$,
$$
f(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{\zeta-z}\,d\zeta .
$$

::: pf-proof
$f$ is holomorphic on an open set containing $\overline{D(a,R)}$, and the point $z$ lies inside the circle $\abs{\zeta-a}=R$, which is traversed once counterclockwise; Cauchy's integral formula then gives the displayed identity.
:::

:::

::: {.pf-step #geometric}
For $\zeta$ on that circle and $\abs{z-a}<R$,
$$
\frac{1}{\zeta-z}=\frac{1}{\zeta-a}\cdot\frac{1}{1-\frac{z-a}{\zeta-a}}=\sum_{n=0}^{\infty}\frac{(z-a)^n}{(\zeta-a)^{n+1}},
$$
the series converging uniformly in $\zeta$ on the circle.

::: pf-proof
Since $\abs{(z-a)/(\zeta-a)}=\abs{z-a}/R=\varrho<1$, the geometric series $\sum_n\varrho^n$ converges; the Weierstrass $M$-test with $M_n=\varrho^n/\abs{\zeta-a}$ gives uniform convergence in $\zeta$ on the circle, whose length is finite.
:::

:::

::: {.pf-step #expansion}
$f(z)=\sum_{n\ge0}a_n(z-a)^n$ with $a_n=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-a)^{n+1}}d\zeta$, for $\abs{z-a}<R$.

::: pf-proof
Insert the uniformly convergent series of step [](#geometric){.pf-ref} into the integral of step [](#cauchy){.pf-ref} and integrate term by term, which uniformity permits; the factor $f(\zeta)$ is bounded on the circle because $f$ is continuous there.
:::

:::

::: {.pf-step #coefficients}
$a_n=\frac{f^{(n)}(a)}{n!}$.

::: pf-proof
Cauchy's differentiation formula gives $f^{(n)}(a)=\frac{n!}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-a)^{n+1}}d\zeta$, which is $n!\,a_n$ by step [](#expansion){.pf-ref}.
:::

:::

::: {.pf-step}
$f$ is the sum of its Taylor series at $a$ on the disc of radius $\operatorname{dist}(a,\partial\Omega)$:
$$
f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(z-a)^n\qquad(\abs{z-a}<R).
$$

::: pf-proof
Steps [](#expansion){.pf-ref} and [](#coefficients){.pf-ref} give the identity for $\abs{z-a}<R$; since $R$ was any number below the distance from $a$ to the boundary, the identity holds on the whole disc $\abs{z-a}<\operatorname{dist}(a,\partial\Omega)$. Hence every holomorphic function is the sum of a convergent power series about each point of its domain, with coefficients $f^{(n)}(a)/n!$.
:::

:::

:::
:::
