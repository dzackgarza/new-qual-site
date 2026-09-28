---
schema: qual/card@1
id: P-QMMKE
kind: problem
title: Subgroups of $\ZZ^3$ and the structure of the quotient
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Free Modules
relations: []
review: draft
---

::: {.problem}
Describe the subgroups of $\ZZ^3$ and the possible structures of the quotient by such a subgroup.
:::

::: {.solution}
Every subgroup $H\le\ZZ^3$ is a free abelian group of rank
\[
r\in\{0,1,2,3\}.
\]

By Smith normal form, there is a basis $e_1,e_2,e_3$ of $\ZZ^3$ and positive integers
\[
d_1\mid d_2\mid\cdots\mid d_r
\]
such that
\[
H=d_1\ZZ e_1\oplus\cdots\oplus d_r\ZZ e_r.
\]
Therefore
\[
\ZZ^3/H
\cong
\ZZ^{3-r}
\oplus
\ZZ/d_1\ZZ
\oplus\cdots\oplus
\ZZ/d_r\ZZ.
\]

Thus the structure theorem for finitely generated modules over the PID $\ZZ$ completely describes both the subgroup, up to change of basis, and the quotient.
:::
