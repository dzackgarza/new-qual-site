---
schema: qual/card@1
id: D-CRVDUAL
kind: definition
title: The dual curve, and the Plücker formula for its degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Dual Curves
  - Singularities
relations:
- kind: uses
  target: D-CRVPLSING
review: draft
prompts:
- What is the dual curve?
---

::: {.definition title="Dual curve"}
Let $C \subseteq \PP^2$ be an irreducible plane curve over an algebraically closed field of characteristic $0$ that is not a line.
The \dfn{dual curve} $C^\vee \subseteq (\PP^2)^\vee$ is the closure of the set of tangent lines $T_p C$ at the smooth points $p$ of $C$.
Its degree is the \dfn{class} of $C$: the number of tangent lines to $C$ through a general point of $\PP^2$.
:::

::: {.theorem}
1. (Biduality) $(C^\vee)^\vee = C$.

2. (Plücker) If $C$ has degree $d$ and its only singularities are $\delta$ nodes and $\kappa$ ordinary cusps, then
$$\deg C^\vee = d(d-1) - 2\delta - 3\kappa.$$
In particular a smooth plane curve of degree $d \geq 2$ has class $d(d-1)$.
:::

::: {.example}
The dual of a smooth conic is a smooth conic.
The dual of a smooth plane cubic has degree $6$; its $9$ cusps correspond to the $9$ flexes of the cubic, and it has no nodes because a smooth cubic has no bitangents.
Its genus is $\binom{5}{2} - 9 = 1$, the genus of the cubic, as it must be for a birational image.
:::
