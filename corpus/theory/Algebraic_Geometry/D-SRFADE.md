---
schema: qual/card@1
id: D-SRFADE
kind: definition
title: ADE surface singularities
classification:
  areas:
  - algebraic-geometry
  topics:
  - Du Val Singularities
  - Quotient Singularities
  - Dynkin Diagrams
relations:
- kind: related-to
  target: D-VARCREPANT
- kind: related-to
  target: FE-TORMINRES
review: draft
prompts:
- What are ADE singularities?
---

::: {.definition title="ADE singularities"}
An \dfn{ADE singularity}, also called a du Val singularity or rational double point, is a surface singularity over $\CC$ analytically isomorphic to the singularity at the origin of one of the following hypersurfaces in $\AA^3$:

| Type | Equation | Group $G \subseteq \SL_2(\CC)$ |
| --- | --- | --- |
| $A_n$, $n \geq 1$ | $x^2 + y^2 + z^{n+1} = 0$ | cyclic of order $n+1$ |
| $D_n$, $n \geq 4$ | $x^2 + y^2 z + z^{n-1} = 0$ | binary dihedral of order $4(n-2)$ |
| $E_6$ | $x^2 + y^3 + z^4 = 0$ | binary tetrahedral of order $24$ |
| $E_7$ | $x^2 + y^3 + y z^3 = 0$ | binary octahedral of order $48$ |
| $E_8$ | $x^2 + y^3 + z^5 = 0$ | binary icosahedral of order $120$ |
:::

::: {.theorem}
1. The ADE singularities are exactly the quotient singularities $\CC^2 / G$ for finite subgroups $G \subseteq \SL_2(\CC)$, with $G$ as in the table.

2. They are exactly the rational double points, and exactly the canonical surface singularities.

3. The exceptional locus of the minimal resolution is a union of smooth rational curves of self-intersection $-2$ whose dual graph is the Dynkin diagram of the same name, and the minimal resolution is crepant.
:::

::: {.example}
$A_1$ is the quadric cone $x^2 + y^2 + z^2 = 0$, the quotient $\CC^2 / \{\pm 1\}$; its minimal resolution is the blowup of the vertex, with one $(-2)$-curve.
:::
