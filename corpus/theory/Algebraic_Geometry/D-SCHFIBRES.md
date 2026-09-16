---
schema: qual/card@1
id: D-SCHFIBRES
kind: definition
title: Generic, special and central fibres; fat points; scheme-theoretic intersections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibres
  - Families
  - Fibre Products
relations:
- kind: uses
  target: D-MORFIB
- kind: uses
  target: D-SCHFPR
review: draft
prompts:
- What are the generic, special and central fibres of a family?
- What is an $n$-fold point over $k$?
- What is a scheme-theoretic intersection?
---

::: {.definition title="Generic, special and central fibres"}
Let $f \colon X \to S$ be a morphism.
If $S$ is irreducible with generic point $\eta$, the \dfn{generic fibre} is $X_\eta = X \times_S \Spec \kappa(\eta)$.
If $S = \Spec R$ for a discrete valuation ring $R$ with fraction field $K$ and residue field $k$, the generic fibre is $X_K$ and the \dfn{special fibre} is $X_k = X \times_R \Spec k$, the fibre over the closed point.
When $S$ is a pointed curve or the spectrum of a local ring, the fibre over the distinguished point $0$ is called the \dfn{central fibre}.
:::

::: {.definition title="Fat points"}
An \dfn{$n$-fold point} over a field $k$ is a scheme $\Spec R$ with one point, where $R$ is a local $k$-algebra with $\dim_k R = n$.
:::

::: {.definition title="Scheme-theoretic intersection"}
For closed subschemes $X_1, X_2 \subseteq Y$, the \dfn{scheme-theoretic intersection} is the fibre product $X_1 \times_Y X_2$, a closed subscheme of $Y$.
If $Y = \Spec R$ and $X_i = \Spec R/J_i$, it is $\Spec (R/J_1 \otimes_R R/J_2) = \Spec R/(J_1 + J_2)$.
:::

::: {.example}
The family $X = V(y^2 - x^3 - t) \subseteq \AA^2 \times \AA^1_t \to \AA^1_t$ over a field of characteristic $0$ has smooth general fibres and the cuspidal cubic $y^2 = x^3$ as central fibre.
The line $y = 0$ and the parabola $y = x^2$ in $\AA^2$ meet in $\Spec k[x,y]/(y, y - x^2) = \Spec k[x]/(x^2)$, a $2$-fold point, which records the tangency that the set-theoretic intersection $\{0\}$ forgets.
:::
