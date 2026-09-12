---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-12
kind: problem
title: Connected covering spaces of the sphere with antipodal poles identified
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
  - Quotient Spaces
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
(May ’13) Let $X$ be the space obtained from the $2$-sphere $S^2$ by identifying the north and south poles (i.e. by identifying two diametrically opposite points).

(a) Show that $X$ is homotopy equivalent to $S^1\vee S^2$.

(b) Describe all connected covering spaces of $X$.
:::

::: {.solution}
(a) Give \(S^2\) a CW decomposition in which the north and south poles are \(0\)-cells. After identifying these two vertices, choose a maximal tree in the resulting \(1\)-skeleton and collapse it. The quotient CW complex reduces to one \(1\)-cell accounting for the identified pair of vertices and one \(2\)-sphere summand. Equivalently, the standard cofibration fact for a path-connected CW complex says that identifying two distinct \(0\)-cells adds a circle up to homotopy. Hence
\[
X\simeq S^2\vee S^1.
\]
In particular,
\[
\pi_1(X)\cong\mathbb Z.
\]

(b) Connected coverings are classified by subgroups of \(\pi_1(X)\cong\mathbb Z\). These are
\[
n\mathbb Z\quad(n=1,2,3,\dots)
\qquad\text{and}\qquad
\{0\}.
\]
They admit a concrete geometric description. The universal cover is a bi-infinite chain
\[
\cdots\cup S^2_{-1}\cup S^2_0\cup S^2_1\cup\cdots,
\]
where the north pole of \(S^2_i\) is identified with the south pole of \(S^2_{i+1}\). The deck generator shifts \(S^2_i\) to \(S^2_{i+1}\).

For \(n\ge1\), quotienting this universal cover by the subgroup \(n\mathbb Z\) gives an \(n\)-sheeted connected cover: a cyclic necklace of \(n\) spheres, with the north pole of each sphere identified with the south pole of the next, cyclically. For \(n=1\) this is \(X\) itself. The subgroup \(\{0\}\) gives the universal infinite chain. These exhaust all connected covering spaces up to equivalence.
:::
