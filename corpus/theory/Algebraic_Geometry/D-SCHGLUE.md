---
schema: qual/card@1
id: D-SCHGLUE
kind: definition
title: Gluing schemes along open subschemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Gluing
  - Projective Space
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- How do you build a scheme that is not affine?
- How is $\PP^n$ built by gluing?
---

::: {.definition title="Gluing data"}
Let $\ts{X_i}$ be schemes, and for each pair $i,j$ let $U_{ij} \subseteq X_i$ be open with isomorphisms $\varphi_{ij}: U_{ij} \to U_{ji}$ satisfying $\varphi_{ii} = \id$, $\varphi_{ji} = \varphi_{ij}\inv$, and the cocycle condition $\varphi_{ik} = \varphi_{jk} \circ \varphi_{ij}$ on $U_{ij} \intersect U_{ik}$.
Then there is a scheme $X$ with an open cover by copies of the $X_i$ inducing the $\varphi_{ij}$, unique up to isomorphism.
:::

::: {.example title="Projective space by charts"}
Take $n+1$ copies of $\AA^n\slice k = \Spec k[x_0/x_i, \dots, x_n/x_i]$ and glue $U_{ij} = D(x_j/x_i)$ to $U_{ji} = D(x_i/x_j)$ by inverting the ratio.
The result is $\PP^n\slice k$, and its global sections are $k$, so it is not affine for $n\geq1$.
:::

::: {.remark}
The cocycle condition makes the identifications consistent on triple overlaps.

Gluing two copies of $\AA^1$ along $\AA^1 \sm \ts{0}$ by the identity gives the line with a doubled origin. Gluing by $t \mapsto t\inv$ gives $\PP^1$.
The two origins remain distinct in both constructions; the doubled-origin line is nonseparated, whereas $\PP^1$ is separated.
:::
