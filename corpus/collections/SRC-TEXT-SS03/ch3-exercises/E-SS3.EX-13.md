---
schema: qual/card@1
id: E-SS3.EX-13
kind: problem
title: "A mild pole bound forces a removable singularity"
classification:
  areas:
    - complex-analysis
  topics: [Removable Singularities, Isolated Singularities]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Structured the card's prose argument into numbered steps without changing the mathematics, and
      re-checked each step against the definitions and theorems it invokes. What was not checked: no
      copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
      collection provenance is the Google Books ISBN link), so the printed statement and page were
      not re-read; the exercise number is the one the collection index records. No published
      solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
Suppose $f(z)$ is holomorphic in a punctured disc $D_r(z_0) - \{z_0\}$. Suppose also that
$$
\abs{f(z)} \leq A\abs{z - z_0}^{-1+\epsilon}
$$
for some $\epsilon > 0$, and all $z$ near $z_0$. Show that the singularity of $f$ at $z_0$ is removable.
:::

::: {.solution}
The statement is Exercise 13 of [@SS03, ch. 3 (p. 105)], printed with the hypothesis $\abs{f(z)}\le A\abs{z-z_0}^{-1+\epsilon}$ for some $\epsilon>0$ and all $z$ near $z_0$.


The argument is the card's own: no copy of Stein and Shakarchi and no published solution set for this book is retained in `tmp/sources`, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 3, Exercise 13. Here $f$ is holomorphic on a punctured disc $D_r(z_0)-\theset{z_0}$ and satisfies $\abs{f(z)}\leq A\abs{z-z_0}^{-1+\epsilon}$ for some $\epsilon>0$, some $A$ and all $z$ near $z_0$; after translating, $z_0=0$, and $f(z)=\sum_{n\in\ZZ}a_nz^{n}$ is its Laurent expansion on an annulus $0<\abs{z}<\rho$.

::: pf

::: {.pf-step #coef}

For $m\geq1$ and $0<\rho'<\rho$, $a_{-m}=\frac{1}{2\pi i}\int_{\abs{z}=\rho'}f(z)z^{m-1}\,dz$.

::: pf-proof

This is Cauchy's formula for the Laurent coefficients on the circle $\abs{z}=\rho'$ inside the annulus of convergence, the function $f(z)z^{m-1}$ being holomorphic there.

:::

:::

::: {.pf-step #bound}

$\abs{a_{-m}}\leq A\rho'^{m-1+\epsilon}$.

::: pf-proof

On $\abs{z}=\rho'$, $\abs{f(z)}\leq A\rho'^{-1+\epsilon}$ for $\rho'$ small enough, and $\abs{z^{m-1}}=\rho'^{m-1}$, so the integrand is bounded by $A\rho'^{m-2+\epsilon}$ and the integral by $2\pi\rho'$ times that: $A\rho'^{m-1+\epsilon}$.

:::

:::

::: {.pf-step #vanish}

$a_{-m}=0$ for every $m\geq1$.

::: pf-proof

In step [](#bound){.pf-ref} the exponent $m-1+\epsilon$ is positive, so $A\rho'^{m-1+\epsilon}\to0$ as $\rho'\downarrow0$; a constant bounded by quantities tending to $0$ is $0$.

:::

:::

::: {.pf-step #done}

The singularity of $f$ at $0$ is removable.

::: pf-proof

By step [](#vanish){.pf-ref} the principal part of the Laurent expansion vanishes, so $f$ agrees on the punctured disc with the holomorphic function $\sum_{n\geq0}a_nz^{n}$; extending by that value at $0$ gives a holomorphic function on the disc, which is the definition of a removable singularity.

:::

:::

:::

:::
