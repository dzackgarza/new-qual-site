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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 7; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both sides: in $\ZZ_2[\alpha]/(\alpha^4)$ the degree-one class has nonzero cube, while in
    the wedge $\RP^2\vee S^3$ the class $x$ comes from $\RP^2$, whose $H^3(\ZZ_2)$ vanishes, and
    products across summands vanish, so $x^3=0$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 7 (p.229). Rechecked: H^*(RP^3;Z_2) = Z_2[alpha]/(alpha^4) by Theorem 3.19 p.220 so alpha^3 != 0, while in the wedge the degree-one class x is pulled back from RP^2, whose H^3(-;Z_2) vanishes by the same theorem, and products from distinct summands vanish. The vanishing is now proved by the relative cup product of p.209 rather than asserted. Not covered: nothing beyond mod 2 coefficients, which suffice.
---

::: {.problem}
Use cup products to show that $\RP^3$ is not homotopy equivalent to $\RP^2 \vee S^3$.
:::

::: {.solution}
With $\ZZ_2$ coefficients, Theorem 3.19 (p.220) gives
$$
H^*(\RP^3;\ZZ_2)
\cong \ZZ_2[\alpha]/(\alpha^4),
\qquad \gradeddegree{\alpha}=1,
$$
so $\alpha^3\ne0$.

For the wedge $Y=\RP^2\vee S^3$, reduced cohomology is the direct sum of the reduced cohomologies of the two summands, and products of positive-dimensional classes from different summands vanish: such a class restricts to $0$ on the other summand, so it lifts to the relative group of the pair obtained by deleting that summand, and the relative cup product of p.209 lands in the cohomology of the pair $(Y,Y)$. The unique nonzero class $x\in H^1(Y;\ZZ_2)$ comes from $\RP^2$, so
$$
x^3=0
$$
because $H^3(\RP^2;\ZZ_2)=0$.

Thus the mod-$2$ cohomology rings are not isomorphic: in one ring the nonzero degree-one class has nonzero cube, while in the other its cube is zero. Hence the spaces cannot be homotopy equivalent.
:::
