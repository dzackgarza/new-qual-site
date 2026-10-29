---
schema: qual/card@1
id: P-UQOCE
kind: problem
title: $\int_\gamma\frac{f'(z)}{z-z_0}\,dz=\int_\gamma\frac{f(z)}{(z-z_0)^2}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $f$ be analytic in a domain $D$ and $\gamma$ be a closed, piecewise smooth curve in $D$.
For any $z_0 \in D$ not lying on $\gamma$, show that: $$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$ Give a generalization of this result for higher-order derivatives and powers.
:::

::: {.solution}

::: pf

::: {.pf-step #step}

For integers $k, m \geq 1$,
$$
\oint_\gamma\frac{f^{(k)}(z)}{(z-z_0)^m}\,dz
=m\oint_\gamma\frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}\,dz.
$$

::: pf-proof

Since $z_0$ is not on $\gamma$, the function $F(z) = f^{(k-1)}(z)/(z-z_0)^m$ is holomorphic on the open set $D \setminus \{z_0\}$, which contains $\gamma$, and
$$
F'(z)
=
\frac{f^{(k)}(z)}{(z-z_0)^m}
-m\frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}.
$$
The integral of a derivative around a closed piecewise smooth curve is zero.

:::

:::

::: pf-step

$\displaystyle\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz$.

::: pf-proof

This is step [](#step){.pf-ref} with $k = m = 1$.

:::

:::

::: pf-step

For integers $k, m \geq 1$,
$$
\boxed{
\oint_\gamma\frac{f^{(k)}(z)}{(z-z_0)^m}\,dz
=
\frac{(m+k-1)!}{(m-1)!}
\oint_\gamma\frac{f(z)}{(z-z_0)^{m+k}}\,dz }.
$$

::: pf-proof

Applying step [](#step){.pf-ref} $k$ times lowers the order of the derivative from $k$ to $0$ and raises the power from $m$ to $m + k$, with accumulated factor $m(m+1)\cdots(m+k-1) = \frac{(m+k-1)!}{(m-1)!}$.

:::

:::

:::

:::
