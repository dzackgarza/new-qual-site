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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the comparison: both spaces have $\ZZ$ in degrees 0, 1 (rank two) and 2 and zero above, while the universal cover of the wedge sum contains a sphere and so has $H_2\ne0$, unlike the plane covering the torus.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line, both halves. Homology: the torus has one `0`-cell, two `1`-cells and one
    `2`-cell with all cellular boundaries zero, giving `Z, Z^2, Z`; reduced homology of a finite wedge
    is the direct sum over the summands, so `S^1 vee S^1 vee S^2` has the same groups. Universal
    covers, which is the point: that of `T` is `R^2` by the quotient `R^2 -> R^2/Z^2`, hence
    contractible with vanishing reduced homology; that of `Y` has fundamental group `F_2`, so the
    preimage of the `1`-skeleton is the Cayley tree, and at every lift of the wedge point the simply
    connected `S^2` summand contributes a copy, so `Y~` is a tree with a `2`-sphere at each vertex.
    Collapsing the contractible tree gives a wedge of one `S^2` per vertex, so
    `H_2(Y~) = direct sum over F_2 of Z`, which is nonzero. Homology is a homotopy invariant, so the
    two universal covers are neither homeomorphic nor homotopy equivalent, even though the two spaces
    have isomorphic homology in every degree. No correction was needed.
---

::: {.problem}
Show that $S^1 \times S^1$ and $S^1 \lor S^1 \lor S^2$ have isomorphic homology groups in all dimensions, but their universal covering spaces do not.
:::

::: {.solution}
Set
$$
T=S^1\times S^1,
\qquad
Y=S^1\vee S^1\vee S^2.
$$

::: pf

::: pf-step

The spaces $T$ and $Y$ have isomorphic homology groups in every degree:
$$
H_n(T)\cong H_n(Y)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ^2,&n=1,\\
\ZZ,&n=2,\\
0,&n>2.
\end{cases}
$$

::: pf-proof

For the torus this is the standard cellular chain computation with one $0$-cell, two $1$-cells, and one $2$-cell, all cellular boundary maps zero. For the wedge, reduced homology splits over a finite wedge:
$$
\widetilde H_n(Y)
\cong
\widetilde H_n(S^1)\oplus\widetilde H_n(S^1)\oplus\widetilde H_n(S^2),
$$
which gives the same groups.

:::

:::

::: pf-step

The universal cover of $T$ is $\RR^2$, hence is contractible.

::: pf-proof

The quotient map
$$
\RR^2\longrightarrow\RR^2/\ZZ^2\cong S^1\times S^1
$$
is the universal covering map. Therefore its universal cover has trivial reduced homology.

:::

:::

::: {.pf-step #s3}

The universal cover of $Y$ has nonzero $H_2$.

::: pf-proof

The fundamental group of $Y$ is the free group $F_2$ coming from the two circle summands. The universal cover of the $1$-skeleton $S^1\vee S^1$ is the Cayley tree of $F_2$. At every lift of the wedge point, a copy of the simply connected summand $S^2$ lifts and is attached at that vertex. Hence the universal cover of $Y$ is a tree with one $2$-sphere attached at each vertex.

Collapsing the tree to a point gives a homotopy equivalence to a wedge of one $S^2$ for each vertex, so
$$
H_2(\widetilde Y)
\cong
\bigoplus_{F_2}\ZZ,
$$
which is nonzero.

:::

:::

::: pf-step

Therefore the universal covering spaces are not homeomorphic, and indeed not homotopy equivalent.

::: pf-proof

The universal cover of $T$ has $H_2=0$, whereas the universal cover of $Y$ has nonzero $H_2$ by step [](#s3){.pf-ref}. Homology is a homotopy invariant, so the universal covers cannot be homotopy equivalent or homeomorphic.

:::

:::

:::

:::
