---
schema: qual/card@1
id: E-HAT-3.3-22
kind: problem
title: "Compactly supported cohomology and $\\times \\mathbb{R}$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $H_c^n(X \times \mathbb{R}; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
Under the standing locally compact Hausdorff hypotheses for compactly supported cohomology,
\[
H_c^q(Y;G)\cong\widetilde H^q(Y^+;G),
\]
where $Y^+$ denotes the one-point compactification.

One-point compactification converts products into smash products:
\[
(X\times\mathbb R)^+\cong X^+\wedge\mathbb R^+.
\]
Since $\mathbb R^+\cong S^1$, this is the reduced suspension
\[
X^+\wedge S^1\cong\Sigma X^+.
\]
Hence the suspension isomorphism gives
\[
H_c^n(X\times\mathbb R;G)
\cong
\widetilde H^n(\Sigma X^+;G)
\cong
\widetilde H^{n-1}(X^+;G)
\cong
H_c^{n-1}(X;G).
\]
Thus
\[
\boxed{H_c^n(X\times\mathbb R;G)\cong H_c^{n-1}(X;G)}
\]
for all $n$.
:::
