---
schema: qual/card@1
id: E-KQTPV
kind: exercise
title: "Define"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Define
\[  
G \definedas \theset{z\in \CC\suchthat \Re(z) > 0, \, \abs{z-1} > 1}
.\]

Find all of the injective conformal maps $G\to \DD$.
These may be expressed as compositions of maps, but explain why this list is complete.
:::

:::{.solution}
Use that every element of $\Aut(\DD)$ is of the form $f(z) = \lambda\psi_a(z)$, and the region $G$ is conformally equivalent to $\DD$.
Thus every element of $\Aut(G)$ can be conjugated to an element of $\Aut(\DD)$ by a conformal map $F: G\to \DD$.
One such map is gotten by rotating $z\mapsto iz$ to get $\HH \intersect \abs{z}>1$, then applying a Joukowski map $z\mapsto z+z\inv$ to get $\HH$.
So
\[
f\in \Aut(G) \implies f = F\inv \circ \psi_{a} \circ F \text{ for some } \psi_a \in \Aut(\DD)
.\]

:::

