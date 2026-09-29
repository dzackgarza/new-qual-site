---
schema: qual/card@1
id: P-BKS83-4
kind: problem
title: Symmetry group of a triangular network through the vertices of the unit square
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF itself does not contain the required diagram. In place of the figure it prints "../Fig/Pr/Sp83-4.ps not found". The statement is therefore preserved without reconstructing the missing network.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: Confirmed that no Sp83-4 asset, duplicate statement containing the diagram, or embedded image occurs in the retained repository source packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked that two explicit triangular networks through the four surviving points have different Euclidean symmetry groups, so the retained data do not determine the requested group.
---

::: {.problem}
In the triangular network in $\mathbb R^2$ referred to by the source, the points $P_0,P_1,P_2,P_3$ are respectively
\[
(0,0),\qquad(1,0),\qquad(0,1),\qquad(1,1).
\]
Describe the structure of the group of all Euclidean transformations of $\mathbb R^2$ that leave this network invariant.
:::

::: {.solution}
::: pf

::: {.pf-step #network-underdetermined}
The four points
$$
P_0=(0,0),
\qquad
P_1=(1,0),
\qquad
P_2=(0,1),
\qquad
P_3=(1,1)
$$
do not determine the Euclidean symmetry group of a triangular network
containing them.

::: pf-proof
Let $N_1$ be the boundary of the unit square together with the diagonal
segment from $P_0$ to $P_3$. This is a planar network consisting of two
triangular cells.

Any Euclidean isometry preserving $N_1$ must preserve its convex hull,
which is the unit square, and therefore must be a symmetry of that square.
Among the eight square symmetries, exactly four preserve the distinguished
diagonal $P_0P_3$ as a set: the identity, the half-turn about the center,
and the reflections in the two diagonals. Thus
$$
\operatorname{Sym}(N_1)
$$
has order $4$.

Now let $N_2$ be the boundary of the unit square together with both
diagonals, regarding their intersection at the center as a vertex. This is
a planar network consisting of four triangular cells. Every symmetry of
the square preserves the union of the two diagonals, so
$$
\operatorname{Sym}(N_2)
$$
is the full square symmetry group, of order $8$.

Both networks contain $P_0,P_1,P_2,P_3$, but their Euclidean symmetry
groups are not isomorphic because they have different orders.
:::

:::

::: pf-qed
The requested group is
$$
\{g\in\operatorname{Isom}(\mathbb R^2):g(N)=N\}
$$
for the network $N$. Step [](#network-underdetermined){.pf-ref} shows that it depends on $N$ beyond the
points $P_0,P_1,P_2,P_3$: the networks $N_1$ and $N_2$ give symmetry
groups of orders $4$ and $8$.
:::

:::
:::
