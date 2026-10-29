---
schema: qual/card@1
id: P-CLHXQ
kind: problem
title: Simplicial homology of $S^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source text was a worked attempt, not a question: it computed H_3 in place of H_2 and miscounted cycles. The statement now poses the computation for the listed triangulation."
---

::: {.problem}
Compute the simplicial homology of $S^2$, triangulated as the boundary of an octahedron with vertices $1,\ldots,6$:

![](../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1513072379449.png)

The simplices are

- vertices $1,2,3,4,5,6$;
- edges $[12],[14],[15],[16],[23],[25],[26],[34],[35],[36],[45],[46]$;
- triangles $[126],[236],[346],[146],[125],[235],[345],[145]$.
:::

::: {.solution}

::: pf

::: pf-step

The listed triangulation has $V=6$, $E=12$, and $F=8$, and its underlying space is $S^2$.

::: pf-proof

The eight listed triangles form the boundary of an octahedron; each edge lies in exactly two triangles.

:::

:::

::: pf-step

Since the complex is connected, $H_0\cong\ZZ$.

::: pf-proof

Zeroth simplicial homology of a connected complex is $\ZZ$.

:::

:::

::: pf-step

The oriented sum of all eight triangular faces, with coherent orientations, is a $2$-cycle generating $H_2\cong\ZZ$.

::: pf-proof

Every edge occurs twice with opposite induced orientations, so the boundary cancels. For a connected triangulated closed orientable surface this fundamental cycle generates top homology.

:::

:::

::: pf-step

Euler characteristic gives
$$2=V-E+F=\operatorname{rank}H_0-\operatorname{rank}H_1+\operatorname{rank}H_2,$$
so $H_1=0$.

::: pf-proof

The Euler characteristic of a finite complex equals the alternating sum of the ranks of its homology groups, and $H_0,H_2$ each have rank $1$, so $H_1$ has rank $0$.
It is also torsion-free: simplicial homology agrees with singular homology, and by the Hurewicz theorem $H_1(S^2;\ZZ)\cong\pi_1(S^2)^{\mathrm{ab}}=0$.

:::

:::

::: pf-step

Thus
$$\boxed{H_k(S^2;\ZZ)\cong\begin{cases}\ZZ,&k=0,2,\\0,&\text{otherwise.}\end{cases}}$$

::: pf-proof

There are no simplices above dimension $2$.

:::

:::

:::

:::
