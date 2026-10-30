---
schema: qual/card@1
id: P-WESCA06-I5
kind: problem
title: "State Cauchy's Integral Formula"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Theorems and Definitions, item 5 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State Cauchy's Integral Formula.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Cauchy's Integral Formula.**

Let $f$ be holomorphic on a domain containing a positively oriented simple
closed contour
$$
\gamma
$$
and its interior. Let
$$
z_0
$$
lie inside $\gamma$. Then
$$
\boxed{
f(z_0)
=
\frac1{2\pi i}
\int_\gamma
\frac{f(\zeta)}
{\zeta-z_0}
\,d\zeta.
}
$$


::: pf-proof

Equivalently, if
$$
\overline{B(z_0,r)}
$$
lies in the domain of holomorphy of $f$, then
$$
f(z_0)
=
\frac1{2\pi i}
\int_{\abs{\zeta-z_0}=r}
\frac{f(\zeta)}
{\zeta-z_0}
\,d\zeta.
$$
This is the standard circle form of Cauchy's formula.

:::

:::

::: {.pf-step #s1-2}

More generally, for every integer
$$
m\ge0,
$$
$$
f^{(m)}(z_0)
=
\frac{m!}{2\pi i}
\int_\gamma
\frac{f(\zeta)}
{(\zeta-z_0)^{m+1}}
\,d\zeta.
$$


::: pf-proof

Differentiate the formula in step [](#s1-1){.pf-ref} under the integral sign.
This is Cauchy's integral formula for derivatives.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement; step [](#s1-2){.pf-ref} records its standard
derivative extension.

:::

:::

:::
