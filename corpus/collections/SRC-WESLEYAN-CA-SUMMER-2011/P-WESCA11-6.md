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
<1>1. Let \(T\subset\mathbb C\) be a closed triangle, including its
interior, and let \(U\subset\mathbb C\) be an open set containing \(T\).

::: {.proof}
These are the geometric hypotheses in the triangle form of Cauchy's
theorem.
:::

<1>2. Suppose
\[
f:U\to\mathbb C
\]
is holomorphic.

::: {.proof}
This is the analytic hypothesis.
:::

<1>3. Orient the boundary
\[
\partial T
\]
positively, that is, counterclockwise.

::: {.proof}
This is the standard orientation convention for contour integration around
a planar region.
:::

<1>4. Cauchy's theorem for triangles states that
\[
\boxed{
\int_{\partial T}f(z)\,dz=0}.
\]

::: {.proof}
This is the theorem requested in the problem.
:::

<1>5. Equivalently, if the three oriented sides of the triangle are
\[
\gamma_1,\gamma_2,\gamma_3,
\]
then
\[
\boxed{
\int_{\gamma_1}f(z)\,dz
+
\int_{\gamma_2}f(z)\,dz
+
\int_{\gamma_3}f(z)\,dz
=0}.
\]

::: {.proof}
The positively oriented boundary contour is the concatenation of the three
oriented sides.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 is the requested statement.
:::
:::
