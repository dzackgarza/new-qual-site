---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-04
kind: problem
title: Homology of the unit sphere union the interval from $(0,0,-1)$ to $(0,0,1)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
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
(Michigan Sept ’08) Compute the homology of the space formed as the union of the unit sphere $$\{(x,y,z)\mid x^2+y^2+z^2=1\}$$ and the closed interval along the $z$-axis from $(0,0,-1)$ to $(0,0,1)$.
:::

::: {.solution}
Let \(I\) be the added diameter joining the south and north poles of \(S^2\). Attaching a \(1\)-cell between two distinct points of a connected CW complex adds one free circle up to homotopy. Concretely, choose an arc \(J\subset S^2\) from one pole to the other; the union \(I\cup J\) is a circle, and collapsing a complementary maximal tree in a compatible CW structure yields
\[
S^2\cup I\simeq S^2\vee S^1.
\]
Consequently
\[
H_n(S^2\cup I;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z,&n=1,\\
\mathbb Z,&n=2,\\
0,&n\ge3.
\end{cases}
\]
The same computation follows from Mayer--Vietoris after thickening \(S^2\) and the interval to open neighborhoods whose intersection has two contractible components.
:::
