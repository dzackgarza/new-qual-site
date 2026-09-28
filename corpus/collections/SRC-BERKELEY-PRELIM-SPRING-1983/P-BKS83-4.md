---
schema: qual/card@1
id: P-BKS83-4
kind: problem
title: Symmetry group of the Spring 1983 triangular network
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

The diagram defining the network is missing from the retained source PDF.
:::

::: {.solution}
The retained source does not contain the diagram that defines the network:
the PDF itself prints
"../Fig/Pr/Sp83-4.ps not found"
where the figure should occur. Consequently, the symmetry group requested
by the original exam cannot be uniquely recovered from the retained source.

<1>1. The four surviving points
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

::: {.proof}
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

Both networks contain the four points specified in the surviving text, but
their Euclidean symmetry groups are not isomorphic because they have
different orders.
:::

<1>2. Therefore no unique group can be deduced from the retained source
packet.

::: {.proof}
Step <1>1 exhibits two networks compatible with all geometric data that
survive in the retained statement and having different symmetry groups.
Hence those surviving data do not determine which symmetry group the
missing diagram was intended to define.
:::

<1>3. The original exam question can be answered only after recovering the
missing network diagram.

::: {.proof}
The group sought by the source is
$$
\{g\in\operatorname{Isom}(\mathbb R^2):g(N)=N\},
$$
where $N$ is the depicted network. Step <1>2 shows that the four named
points alone do not determine this group. Since the retained PDF supplies
no further description of $N$, a more specific group would require
reconstructing absent source data by guesswork.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 give the strongest determination supported by the retained
source and prove why no unique symmetry group can be stated from it.
:::
:::
