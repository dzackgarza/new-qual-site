---
schema: qual/card@1
id: E-HAT-2.1-29
kind: problem
title: $S^1 \times S^1$ and $S^1 \lor S^1 \lor S^2$ have isomorphic homology but different universal covers
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Cover
  - Torus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 29; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed against the relevant chain, relative-homology, local-homology, or covering-space calculation.
---

Show that $S^1 \times S^1$ and $S^1 \lor S^1 \lor S^2$ have isomorphic homology groups in all dimensions, but their universal covering spaces do not.

::: {.solution}
Set
\[
T=S^1\times S^1,
\qquad
Y=S^1\vee S^1\vee S^2.
\]

<1>1. The spaces $T$ and $Y$ have isomorphic homology groups in every degree:
\[
H_n(T)\cong H_n(Y)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z^2,&n=1,\\
\mathbb Z,&n=2,\\
0,&n>2.
\end{cases}
\]
::: {.proof}
For the torus this is the standard cellular chain computation with one $0$-cell, two $1$-cells, and one $2$-cell, all cellular boundary maps zero. For the wedge, reduced homology splits over a finite wedge:
\[
\widetilde H_n(Y)
\cong
\widetilde H_n(S^1)\oplus\widetilde H_n(S^1)\oplus\widetilde H_n(S^2),
\]
which gives the same groups.
:::

<1>2. The universal cover of $T$ is $\mathbb R^2$, hence is contractible.
::: {.proof}
The quotient map
\[
\mathbb R^2\longrightarrow\mathbb R^2/\mathbb Z^2\cong S^1\times S^1
\]
is the universal covering map. Therefore its universal cover has trivial reduced homology.
:::

<1>3. The universal cover of $Y$ has nonzero $H_2$.
::: {.proof}
The fundamental group of $Y$ is the free group $F_2$ coming from the two circle summands. The universal cover of the $1$-skeleton $S^1\vee S^1$ is the Cayley tree of $F_2$. At every lift of the wedge point, a copy of the simply connected summand $S^2$ lifts and is attached at that vertex. Hence the universal cover of $Y$ is a tree with one $2$-sphere attached at each vertex.

Collapsing the tree to a point gives a homotopy equivalence to a wedge of one $S^2$ for each vertex, so
\[
H_2(\widetilde Y)
\cong
\bigoplus_{F_2}\mathbb Z,
\]
which is nonzero.
:::

<1>4. Therefore the universal covering spaces are not homeomorphic, and indeed not homotopy equivalent.
::: {.proof}
The universal cover of $T$ has $H_2=0$, whereas the universal cover of $Y$ has nonzero $H_2$ by <1>3. Homology is a homotopy invariant, so the universal covers cannot be homotopy equivalent or homeomorphic.
:::
:::
