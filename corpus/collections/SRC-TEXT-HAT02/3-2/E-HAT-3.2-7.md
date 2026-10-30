---
schema: qual/card@1
id: E-HAT-3.2-7
kind: problem
title: $\RP^3$ is not homotopy equivalent to $\RP^2\vee S^3$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
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
Use cup products to show that $\RP^3$ is not homotopy equivalent to $\RP^2 \vee S^3$.
:::

::: {.solution}
With $\ZZ_2$ coefficients,
$$
H^*(\RP^3;\ZZ_2)
\cong \ZZ_2[\alpha]/(\alpha^4),
\qquad \gradeddegree{\alpha}=1,
$$
so $\alpha^3\ne0$.

For the wedge $Y=\RP^2\vee S^3$, reduced cohomology splits additively as the direct sum of the reduced cohomologies of the two wedge summands, and products between positive-dimensional classes coming from different summands vanish. The unique nonzero class $x\in H^1(Y;\ZZ_2)$ comes from $\RP^2$, so
$$
x^3=0
$$
because $H^3(\RP^2;\ZZ_2)=0$.

Thus the mod-$2$ cohomology rings are not isomorphic: in one ring the nonzero degree-one class has nonzero cube, while in the other its cube is zero. Hence the spaces cannot be homotopy equivalent.
:::
