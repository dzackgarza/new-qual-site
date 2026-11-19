---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW3
kind: problem
title: Classification of compact surfaces without boundary
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which states the classification rather
    than proving it, as the worksheet asks. Added what the description left implicit: that the sphere
    is the genus-zero member of the orientable family, the additivity formula
    chi(M # N) = chi(M) + chi(N) - 2 from which the two displayed Euler characteristics follow with
    chi(S^2) = 2 and chi(RP^2) = 1, the injectivity of g -> 2 - 2g and k -> 2 - k that makes the Euler
    characteristic separate the members within a family, and the compactness argument that gives
    finitely many components in the disconnected case. Not checked: the printed worksheet.
---

::: {.problem}
Briefly describe the classification of compact surfaces without boundary.
:::

::: {.solution}
This is a worksheet question of the 2020 topology workshop (`SRC-TOP-WORKSHOP-2020`, worksheet 3A). No solution set is retained for it and the worksheet itself was not re-read in this pass; the card states the classification and records the invariants that distinguish its members, as the worksheet's "briefly describe" asks.

::: pf

::: {.pf-step #list}
Every connected compact surface without boundary is homeomorphic to exactly one member of the following list: the sphere $S^{2}$; for each $g\geq1$ the connected sum $\Sigma_{g}=T^{2}\#\cdots\#T^{2}$ of $g$ tori; and for each $k\geq1$ the connected sum $N_{k}=\RP^{2}\#\cdots\#\RP^{2}$ of $k$ projective planes.

::: pf-proof
This is the classification theorem for compact surfaces, whose proof triangulates the surface, reduces the triangulation to a normal form, and reads off the list. The list is exhaustive and no two of its members are homeomorphic; the sphere is the case $g=0$ of the orientable family, so it is the only member not indexed by a positive parameter.
:::
:::

::: {.pf-step #disjoint}
The orientable members $\Sigma_{g}$ and the nonorientable members $N_{k}$ are mutually non-homeomorphic.

::: pf-proof
Orientability is a topological invariant: a homeomorphism carries an orientation of one surface to an orientation of the other. The sphere $S^{2}$ and the torus $T^{2}=\RR^{2}/\ZZ^{2}$ are orientable, the second because the plane's orientation is invariant under the translation lattice and descends to the quotient. The projective plane is not orientable: it is the quotient of $S^{2}$ by the antipodal map, which reverses orientation, so no orientation of $S^{2}$ descends to it. Finally, a connected sum with a nonorientable summand is nonorientable, since an orientation of the sum would restrict, on the punctured summand, to an orientation of that summand. Hence $\Sigma_{g}$ is orientable and $N_{k}$ is not, and the two are never homeomorphic.
:::
:::

::: {.pf-step #invariant}
Within each family the genus is a homeomorphism invariant, detected by the Euler characteristic: $\chi(\Sigma_{g})=2-2g$ and $\chi(N_{k})=2-k$.

::: pf-proof
The Euler characteristic of a finite cell decomposition is a homeomorphism invariant, and connected sum satisfies $\chi(M\#N)=\chi(M)+\chi(N)-2$. With $\chi(S^{2})=2$ and $\chi(\RP^{2})=1$ this gives $\chi(\Sigma_{g})=2-2g$ and $\chi(N_{k})=1\cdot k-2(k-1)=2-k$. The function $g\mapsto2-2g$ is injective on $g\geq0$ and $k\mapsto2-k$ is injective on $k\geq1$, so the Euler characteristic separates the members within each family.
:::
:::

::: {.pf-step #disconnected}
A compact surface without boundary that is not connected is a finite disjoint union of connected compact surfaces without boundary, hence of members of the list.

::: pf-proof
A compact space has finitely many connected components, each of which is compact and, being a component of a surface, is a connected surface without boundary. So the disconnected case reduces to the connected one component by component.
:::
:::
:::

:::
