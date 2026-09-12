---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW3
kind: problem
title: Reduced versus non-reduced homology
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
What is the difference between the reduced homology and (non-reduced) homology?
:::

::: {.solution}
Ordinary singular homology uses the chain complex
\[
\cdots\to C_1(X)\xrightarrow{\partial_1}C_0(X)\to0.
\]
Reduced homology replaces the bottom by the augmentation map
\[
\varepsilon:C_0(X)\to\mathbb Z,
\qquad
\varepsilon\!\left(\sum n_i x_i\right)=\sum n_i,
\]
forming
\[
\cdots\to C_1(X)\to C_0(X)\xrightarrow{\varepsilon}\mathbb Z\to0.
\]
The resulting groups are \(\widetilde H_n(X)\).

For every nonempty space,
\[
\widetilde H_n(X)\cong H_n(X)\qquad(n>0),
\]
while degree \(0\) has the extra free summand
\[
H_0(X)\cong\widetilde H_0(X)\oplus\mathbb Z.
\]
Thus if \(X\) has \(c\) path components,
\[
H_0(X)\cong\mathbb Z^c,
\qquad
\widetilde H_0(X)\cong\mathbb Z^{c-1}.
\]
In particular, reduced homology of a point is zero in every degree.
:::
