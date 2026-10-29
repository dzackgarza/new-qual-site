---
schema: qual/card@1
id: P-WESCA11-6
kind: problem
title: 'State Cauchy’s theorem for triangles'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State Cauchy's theorem for triangles.
:::

::: {.solution}

::: pf

::: pf-step

Let $T\subset\CC$ be a closed triangle, including its
interior, and let $U\subset\CC$ be an open set containing $T$.


::: pf-proof

These are the geometric hypotheses in the triangle form of Cauchy's
theorem.

:::

:::

::: pf-step

Suppose
$$
f:U\to\CC
$$
is holomorphic.


::: pf-proof

This is the analytic hypothesis.

:::

:::

::: pf-step

Orient the boundary
$$
\partial T
$$
positively, that is, counterclockwise.


::: pf-proof

This is the standard orientation convention for contour integration around
a planar region.

:::

:::

::: {.pf-step #s1-4}

Cauchy's theorem for triangles states that
$$
\boxed{
\int_{\partial T}f(z)\,dz=0}.
$$


::: pf-proof

This is the theorem requested in the problem.

:::

:::

::: pf-step

Equivalently, if the three oriented sides of the triangle are
$$
\gamma_1,\gamma_2,\gamma_3,
$$
then
$$
\boxed{
\int_{\gamma_1}f(z)\,dz
+
\int_{\gamma_2}f(z)\,dz
+
\int_{\gamma_3}f(z)\,dz
=0}.
$$


::: pf-proof

The positively oriented boundary contour is the concatenation of the three
oriented sides.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested statement.

:::

:::

:::
