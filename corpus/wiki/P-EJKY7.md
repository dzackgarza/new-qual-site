---
schema: qual/card@1
id: P-EJKY7
kind: problem
title: "Let $X$ be $S^1$ with two 2-cells attached via $z\\mapsto z^5$ and $z\\mapsto z^3$."
classification:
  areas:
  - topology
  topics:
  - cell-complexes
  - fundamental-group
  - cohomology
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $X$ be $S^1$ with two 2-cells attached via $z\mapsto z^5$ and $z\mapsto z^3$.

- Compute $\pi_1(X)$ and $H^*(X)$ as a ring.
- Show that $X$ is not homeomorphic to $S^2$.

:::

:::{.solution}
\envlist

- $X$ is path-connected, so $H_0(X) = \ZZ$.
- $X$ is a CW complex with only one 1-cell, so $\pi_1(X^{(1)}) = \ZZ$ for the 1-skeleton.
  - Use that $3\ZZ + 5\ZZ = 1\ZZ$ as a ring, so the attached cells kill off all 1-homotopy and $\pi_1(X) = 1$.
- By Hurewicz, $H_1(X) = 1$.
- By UCT, $H^1(X) = H_1(X)\dual = \Hom_\ZZ(1, \ZZ) = 1$
- By UCT, $H^2(X) = H_2(X)\dual$
- We can compute $H_2$ directly: 
\[
C^*(X) 
= (0 \to C_2(X) \mapsvia{d_2} C_1(X) \mapsvia{d_1} C_0(X) )
= (0 \to \ZZ\adjoin{e_1, e_2} \mapsvia{\substack{e_1\mapsto 3e \\ e_2 \mapsto 5e} } \ZZ\adjoin{e} \mapsvia{d_1} \ZZ\adjoin{\pt} )
.\]
- $\ker d_2 = \gens{ 5e_1, -3e_2 }$, so $H_2 = \ZZ$.
- Thus $H^*(X) = \Extalgebra_\ZZ(x)$ where $\abs{x} = 2$.
- $X\not\cong S^2$: delete a point $p$ in the interior of the 2-cell corresponding to $z^3$, then use that $S^2\sm\ts{\pt} \cong \RR^2$ is contractible but $\pi_1 X\sm\ts{\pt} = \ZZ/5$. 

:::

