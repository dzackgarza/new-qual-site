---
schema: qual/card@1
id: P-WESCA12-I2
kind: problem
title: 'Integral formula for higher derivatives of analytic functions'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Basic facts, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State a theorem expressing the $m$th derivative of an analytic function as a contour integral.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Cauchy's integral formula for derivatives.**

Let
$$
f:D\to\CC
$$
be holomorphic, let
$$
z_0\in D,
$$
and choose
$$
r>0
$$
such that
$$
\overline{B(z_0,r)}
\subset D.
$$
Then for every integer
$$
m\ge0,
$$
$$
\boxed{
f^{(m)}(z_0)
=
\frac{m!}{2\pi i}
\int_{|\zeta-z_0|=r}
\frac{f(\zeta)}
{(\zeta-z_0)^{m+1}}
\,d\zeta.
}
$$
The circle is positively oriented.


::: pf-proof

For
$$
m=0,
$$
this is the ordinary Cauchy integral formula.

Differentiating
$$
f(z)
=
\frac1{2\pi i}
\int_{|\zeta-z_0|=r}
\frac{f(\zeta)}{\zeta-z}
\,d\zeta
$$
with respect to $z$, and repeating $m$ times, gives
$$
\frac{d^m}{dz^m}
\frac1{\zeta-z}
=
\frac{m!}{(\zeta-z)^{m+1}}.
$$
Evaluation at
$$
z=z_0
$$
gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

More generally, if $\gamma$ is a positively oriented simple closed
contour in $D$ whose interior lies in $D$ and contains $z_0$, then
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

Apply the Cauchy integral formula on the region bounded by $\gamma$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem, with step [](#s1-2){.pf-ref} recording the standard
contour-generalized form.

:::

:::

:::
