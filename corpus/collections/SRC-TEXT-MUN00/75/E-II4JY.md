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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 75 Exercise 2, printed p. 457. The square scheme aba^{-1}b gives partial_2 = a + b - a + b = 2b, so H_1 = Z + Z/2. Checked against the cell structure of Section 74 and Theorem 75.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
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
