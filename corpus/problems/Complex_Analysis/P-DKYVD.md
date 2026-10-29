---
schema: qual/card@1
id: P-DKYVD
kind: problem
title: $\int_\gamma\frac{dz}{(z-a)(z-b)}=\frac{2\pi i}{a-b}$ for $\abs{a}<r<\abs{b}$
  without Cauchy's formula
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Contour Integration
  - Residues
relations: []
review: draft
---

::: {.problem}
Without using Cauchy's integral formula, show that if $\abs{a} < r < \abs{b}$, then
$$
\int_{\gamma} \frac{d z}{(z-a)(z-b)}
=\frac{2 \pi i}{a-b}
$$
where $\gamma$ denotes the circle centered at the origin of radius $r$ with positive orientation.
:::

::: {.hint}
Take a Laurent expansion.
:::

::: {.solution}

::: pf

::: {.pf-step #expansions}
On $\abs{z}=r$,
$$
\frac1{z-a}=\sum_{m=0}^\infty a^mz^{-m-1},\qquad
\frac1{z-b}=-\sum_{n=0}^\infty\frac{z^n}{b^{n+1}},
$$
and both series converge absolutely and uniformly on the circle.

::: pf-proof
Write $\frac1{z-a}=\frac1z\frac1{1-a/z}$ and $\frac1{z-b}=-\frac1b\frac1{1-z/b}$, and use the geometric series with ratios $\abs{a}/r<1$ and $r/\abs{b}<1$.
:::

:::

::: {.pf-step #coefficient}
The coefficient of $z^{-1}$ in the product of the two series is $\frac1{a-b}$.

::: pf-proof
The term $a^mz^{-m-1}\cdot z^n$ has degree $-1$ exactly when $n=m$, so the coefficient is $-\sum_{m\ge0}\frac{a^m}{b^{m+1}}=-\frac{1/b}{1-a/b}=\frac1{a-b}$.
:::

:::

::: pf-step
$\int_\gamma\frac{dz}{(z-a)(z-b)}=\frac{2\pi i}{a-b}$.

::: pf-proof
By step [](#expansions){.pf-ref}, the product series converges absolutely and uniformly on $\gamma$, so it may be integrated term by term.
$\int_\gamma z^k\,dz=0$ for $k\ne-1$ and $\int_\gamma z^{-1}\,dz=2\pi i$, by direct parametrization; step [](#coefficient){.pf-ref} gives the result.
:::

:::

:::

:::
