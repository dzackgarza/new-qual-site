---
schema: qual/card@1
id: E-II4JY
kind: problem
title: The first homology of the Klein bottle
classification:
  areas:
  - topology
  topics:
  - Homology of Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

If $K$ is the Klein bottle, calculate $H_1(K)$ directly.
:::

::: {.solution}
Use the square model of $K$ with boundary word $aba^{-1}b$. Its CW structure has one vertex, the oriented edges $a,b$, and one 2-cell. Thus
$$
C_2(K)\cong\ZZ,\qquad
C_1(K)\cong\ZZ a\oplus\ZZ b,\qquad
\partial_1=0.
$$
The attaching word traverses $a$ once in each direction and $b$ twice in the same direction. Therefore
$$
\partial_2(1)=a+b-a+b=2b.
$$
It follows that
$$
H_1(K)=\ker\partial_1/\operatorname{im}\partial_2
\cong(\ZZ a\oplus\ZZ b)/\langle2b\rangle
\cong\ZZ\oplus\ZZ/2.
$$
:::
