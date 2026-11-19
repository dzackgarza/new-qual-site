---
schema: qual/card@1
id: P-APAS23F
kind: problem
title: Rank of the $D_4$-averaging operator on $\CC[X]$ for a $3\times 3$ board
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Part B, Problem 2 of the Spring 2023 Applied Algebra Qualifying Exam, printed
    p. 2 of the Part B paper retained at assets/attachments/Applied_Algebra_Part_B_SP23.pdf, is the
    statement the card answers, and the head of the solution names it. Checked: the statement against
    the paper's text layer at the page named; the rank of $R$ as the dimension of the $D_4$-invariants,
    and the orbit count that gives it; `qualc.authoring check` on the card, and `tmp/lam.sh` for the
    numbering and the QED. Not checked: no retained solution set exists for this paper to compare the
    argument with, and no other card of the collection in this pass.
---

::: {.problem}
Let $X$ be the $9$-element set of positions in a $3 \times 3$ matrix.
The dihedral group $D_4$ of symmetries of a square acts on $X$ in a natural way.
Let $\CC[X]$ be the corresponding permutation representation and let $R \colon \CC[X] \to \CC[X]$ be the operator defined by
$$
R(v) := \frac{1}{\cardinality{D_4}} \sum_{g \in D_4} g \cdot v
$$
for all $v \in \CC[X]$.
What is the rank of the linear operator $R$?
:::

::: {.solution}

No retained solution set covers this exercise: the problem is Part B, Problem 2, of the Spring 2023 Applied Algebra Qualifying Exam, printed p. 2 of the Part B paper retained at `assets/attachments/Applied_Algebra_Part_B_SP23.pdf` — the earlier text cited the Part A paper, which holds the first four questions of the same examination — and no solutions sheet accompanies it, so the argument below is the card's own. The earlier version of the card asserted both that $\operatorname{im}R$ is the invariant subspace and that there are three orbits; each is argued here, the orbit count through a distance invariant of the square symmetries.

Throughout, $X=\theset{(i,j)\mid i,j\in\theset{1,2,3}}$ is the set of nine positions of the board, $D_{4}$ acts on $X$ through its action on the plane, $\CC[X]$ is the permutation representation with basis $(e_{x})_{x\in X}$, on which $g\cdot e_{x}=e_{gx}$, and $R=\frac{1}{\abs{D_{4}}}\sum_{g\in D_{4}}g$.

::: pf

::: {.pf-step #projection}
$R$ is the projection of $\CC[X]$ onto the invariant subspace $\CC[X]^{D_{4}}$; in particular $\operatorname{rank}R=\dim\CC[X]^{D_{4}}$.

:::: pf-proof

::: {.pf-step #invariance}
$R(v)$ is invariant under every $h\in D_{4}$, and $R(v)=v$ whenever $v$ is invariant.

::: pf-proof
For $h\in D_{4}$ the map $g\mapsto hg$ is a bijection of the finite group $D_{4}$, so
$$
h\cdot R(v)=\frac{1}{\abs{D_{4}}}\sum_{g}hg\cdot v=\frac{1}{\abs{D_{4}}}\sum_{g'}g'\cdot v=R(v).
$$
If $g\cdot v=v$ for every $g$ then each summand equals $v$ and the average is $v$.
:::

:::

::: {.pf-step #idempotent}
$R^{2}=R$, so $R$ is a projection and its rank is the dimension of its image.

::: pf-proof
Applying $R$ to $R(v)$ and using that $R(v)$ is invariant by step [](#invariance){.pf-ref} gives $R(R(v))=R(v)$. For a linear map with $R^{2}=R$ the image is the fixed set of $R$ and the space is the direct sum of the image and the kernel, so the rank equals $\dim\operatorname{im}R$.
:::

:::

::: {.pf-step}
$\operatorname{im}R=\CC[X]^{D_{4}}$.

::: pf-proof
Each $R(v)$ is invariant by step [](#invariance){.pf-ref}, so $\operatorname{im}R\subset\CC[X]^{D_{4}}$; each invariant $v$ satisfies $v=R(v)\in\operatorname{im}R$ by the same step, so the reverse inclusion holds.
:::

:::

::::

:::

::: {.pf-step #orbits-basis}
$\dim\CC[X]^{D_{4}}$ is the number of orbits of $D_{4}$ on $X$.

::: pf-proof
Write $v=\sum_{x}c_{x}e_{x}$. For $g\in D_{4}$, the vector $g\cdot v$ has coefficients $(g\cdot v)_{gx}=c_{x}$, that is $(g\cdot v)_{y}=c_{g^{-1}y}$; so $v$ is invariant exactly when $c_{g^{-1}y}=c_{y}$ for all $g$ and $y$, that is exactly when $c$ is constant on each orbit. Hence the invariant subspace has, as a basis, the indicator functions of the orbits: they are invariant, and every invariant vector is a linear combination of them. Their number is the number of orbits.
:::

:::

::: pf-step
Therefore
$$
\boxed{\operatorname{rank}R=3.}
$$

::: pf-proof
The three classes
$$
\theset{(2,2)},\qquad\theset{(1,1),(1,3),(3,1),(3,3)},\qquad\theset{(1,2),(2,1),(2,3),(3,2)}
$$
are the orbits. A symmetry of the square fixes the centre of the board and is an isometry of the plane, so it preserves the distance of a position from the centre; with unit spacing those distances are $0$ for the centre, $\sqrt2$ for the four corners and $1$ for the four edge-midpoints, so each class is a union of orbits. Within each class the rotation by a quarter turn, an element of $D_{4}$, cycles the members (for the edge-midpoints as well as the corners) and fixes the centre, so each class is a single orbit. Hence there are three orbits, and by steps [](#projection){.pf-ref} and [](#orbits-basis){.pf-ref} the rank of $R$ is $\dim\CC[X]^{D_{4}}=3$; equivalently $R$ is the orthogonal projection onto the span of the three orbit indicator functions.
:::

:::

:::

:::
