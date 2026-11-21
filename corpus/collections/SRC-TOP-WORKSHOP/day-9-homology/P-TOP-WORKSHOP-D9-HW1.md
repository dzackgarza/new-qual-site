---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-HW1
kind: problem
title: Homology of $S^n$ for all $n\ge 0$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the standard CW structure on $S^n$
    has one $0$-cell and one $n$-cell, and the cellular boundary is zero — in degree $n$ for $n\ge2$
    because there are no intermediate cells, and for $n=1$ because the $1$-cell attaches to the
    $0$-cell by the constant map of degree $0$; so the chain complex equals its homology. For
    $S^0$ the two points give $\ZZ\oplus\ZZ$ in degree $0$. Added: the $n=1$ case of the boundary
    argument, which the earlier text covered only by asserting "no cells in intermediate
    dimensions", and the reduced-to-unreduced conversion. No defect found in the statement. The
    collection's provenance is the worksheet, so no retained solution set covers the item.
---

::: {.problem}
Compute the homology groups of $S^n$ for all $n\ge 0$.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the computation is the card's own; it is the cellular chain complex of the standard CW structure on the sphere.

::: pf

::: {.pf-step #cw}
For $n\ge1$ the sphere $S^n$ is a CW complex with one $0$-cell and one $n$-cell, and its cellular chain complex has zero boundary maps.

::: pf-proof
$S^n$ is the one-point compactification of $\RR^n$, and the standard structure is obtained from a point by attaching one $n$-cell by the constant map, or by collapsing the boundary of the $n$-ball to a point; the result has exactly the two cells. For $n\ge2$ there are no cells in degrees between $1$ and $n-1$, so the only boundary maps into or out of $C_n=\ZZ$ and $C_0=\ZZ$ are the ones $C_n\to C_{n-1}=0$ and $C_1=0\to C_0$; for $n=1$ the single $1$-cell is attached to the single $0$-cell by the constant map from $S^0$, whose degree is $0$. In every case the boundary maps vanish.
:::

:::

::: {.pf-step #homology}
For $n\ge1$, $H_k(S^n;\ZZ)=\ZZ$ for $k=0$ and $k=n$, and $0$ otherwise.

::: pf-proof
With all boundary maps zero by step [](#cw){.pf-ref}, the cellular chain complex equals its own homology: $H_k$ is the free abelian group on the $k$-cells, which is $\ZZ$ for $k=0,n$ and $0$ otherwise. Equivalently $\widetilde H_k(S^n)=\ZZ$ for $k=n$ and $0$ else, matching $H_0=\ZZ$ and the vanishing of the reduced group in degree $0$ for $n\ge1$.
:::

:::

::: {.pf-step}
$H_0(S^0;\ZZ)=\ZZ\oplus\ZZ$ and $H_k(S^0;\ZZ)=0$ for $k>0$.

::: pf-proof
$S^0$ is the two-point space, whose zeroth homology is the free abelian group on its two path components, namely $\ZZ\oplus\ZZ$, and which has no simplices or cells in positive degrees. Correspondingly $\widetilde H_0(S^0)=\ZZ$.
:::

:::

::: {.pf-step}
$\boxed{H_k(S^n;\ZZ)=\ZZ\text{ for }k=0,n\text{ and }0\text{ otherwise }(n\ge1),\quad H_0(S^0)=\ZZ^2}$

::: pf-proof
Steps [](#homology){.pf-ref} and this one's predecessor give the two cases $n\ge1$ and $n=0$; the display collects them, with $H_k(S^0)=0$ for $k>0$ and $\widetilde H_k(S^n)=\ZZ$ exactly in degree $k=n$ in both cases.
:::

:::

:::
:::
