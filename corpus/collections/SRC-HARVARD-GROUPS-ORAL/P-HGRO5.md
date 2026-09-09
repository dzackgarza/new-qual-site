---
schema: qual/card@1
id: P-HGRO5
kind: problem
title: A nonabelian group of order 27
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, question asking for a nonabelian group of order 27.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an example of a nonabelian group of order $27$.
:::

::: solution
Take the unitriangular group
\[
G=UT_3(\mathbf F_3)
=
\left\{
\begin{pmatrix}
1&a&c\\
0&1&b\\
0&0&1
\end{pmatrix}
:a,b,c\in\mathbf F_3
\right\}.
\]

<1>1. The group $G$ has order $27$.
::: proof
The entries $a,b,c$ can be chosen independently from the three-element field
$\mathbf F_3$, so $|G|=3^3=27$.
:::

<1>2. The group $G$ is nonabelian.
::: proof
Let
\[
x=I+E_{12},\qquad y=I+E_{23}.
\]
Since $E_{12}E_{23}=E_{13}$ but $E_{23}E_{12}=0$,
\[
xy=I+E_{12}+E_{23}+E_{13},
\qquad
yx=I+E_{12}+E_{23}.
\]
Hence $xy\ne yx$, so $G$ is nonabelian.
:::
:::
