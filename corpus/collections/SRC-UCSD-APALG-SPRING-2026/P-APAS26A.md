---
schema: qual/card@1
id: P-APAS26A
kind: problem
title: Operator norm on $\operatorname{Hom}(V,W)$ is not induced by a scalar product
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $V$ and $W$ be Hilbert spaces, each of dimension at least two.
Prove that the operator norm on $\operatorname{Hom}(V, W)$ is not induced by any scalar product on $\operatorname{Hom}(V, W)$.

Note: On this exam, a Hilbert space is a finite-dimensional complex vector space equipped with a scalar product.
:::

::: {.solution}
Any norm induced by an inner product satisfies the parallelogram identity
$$
\norm{S+T}^2+\norm{S-T}^2=2\norm{S}^2+2\norm{T}^2.
$$
We exhibit two operators for which the operator norm violates this identity.

Choose orthonormal vectors $e_1,e_2\in V$ and $f_1,f_2\in W$. Define $S,T\in\operatorname{Hom}(V,W)$ by
$$
S e_1=f_1,\qquad S\restrict_{e_1^\perp}=0,
$$
$$
T e_2=f_2,\qquad T\restrict_{e_2^\perp}=0.
$$
Then
$$
\norm{S}_{\mathrm{op}}=\norm{T}_{\mathrm{op}}=1.
$$
Moreover, on $\operatorname{span}\{e_1,e_2\}$ the maps $S+T$ and $S-T$ send the orthonormal basis $e_1,e_2$ to the orthonormal sets $f_1,f_2$ and $f_1,-f_2$, respectively, and they vanish on the orthogonal complement. Hence
$$
\norm{S+T}_{\mathrm{op}}=\norm{S-T}_{\mathrm{op}}=1.
$$
Thus
$$
\norm{S+T}_{\mathrm{op}}^2+\norm{S-T}_{\mathrm{op}}^2=2,
$$
whereas
$$
2\norm{S}_{\mathrm{op}}^2+2\norm{T}_{\mathrm{op}}^2=4.
$$
The parallelogram identity fails, so the operator norm cannot be induced by any scalar product on $\operatorname{Hom}(V,W)$.
:::
