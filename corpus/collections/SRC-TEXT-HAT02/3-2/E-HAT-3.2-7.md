---
schema: qual/card@1
id: E-HAT-3.2-7
kind: problem
title: $\mathbb{RP}^3$ is not homotopy equivalent to $\mathbb{RP}^2\vee S^3$
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Use cup products to show that $\mathbb{RP}^3$ is not homotopy equivalent to $\mathbb{RP}^2 \vee S^3$.
:::

::: {.solution}
With $\mathbb Z_2$ coefficients,
\[
H^*(\mathbb{RP}^3;\mathbb Z_2)
\cong \mathbb Z_2[\alpha]/(\alpha^4),
\qquad |\alpha|=1,
\]
so $\alpha^3\ne0$.

For the wedge $Y=\mathbb{RP}^2\vee S^3$, reduced cohomology splits additively as the direct sum of the reduced cohomologies of the two wedge summands, and products between positive-dimensional classes coming from different summands vanish. The unique nonzero class $x\in H^1(Y;\mathbb Z_2)$ comes from $\mathbb{RP}^2$, so
\[
x^3=0
\]
because $H^3(\mathbb{RP}^2;\mathbb Z_2)=0$.

Thus the mod-$2$ cohomology rings are not isomorphic: in one ring the nonzero degree-one class has nonzero cube, while in the other its cube is zero. Hence the spaces cannot be homotopy equivalent.
:::
