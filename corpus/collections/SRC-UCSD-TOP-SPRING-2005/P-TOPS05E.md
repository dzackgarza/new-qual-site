---
schema: qual/card@1
id: P-TOPS05E
kind: problem
title: "Compact non-orientable 3-manifold has nonzero H^1"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Orientation
relations: []
review: draft
---

::: {.problem}
Let $X$ be a compact non-orientable $3$-manifold.
Prove $H^1(X; \mathbb{Z}) \neq 0$.
:::

::: {.solution}
<1>1. The statement as printed is false if compact manifolds with boundary are allowed.
::: {.proof}
Take $X=\mathbb{RP}^2\times I$. This is a compact nonorientable $3$-manifold with boundary, but it deformation retracts onto $\mathbb{RP}^2$. Hence
$$H^1(X;\mathbb Z)\cong H^1(\mathbb{RP}^2;\mathbb Z)=0.$$
:::

<1>2. The standard corrected statement is true for a connected closed nonorientable $3$-manifold $M$.
::: {.proof}
A closed odd-dimensional manifold has Euler characteristic $0$, whether orientable or not: pass to the orientation double cover and use multiplicativity of Euler characteristic together with Poincaré duality upstairs. Since $M$ is nonorientable, $H_3(M;\mathbb Q)=0$, while $H_0(M;\mathbb Q)\cong\mathbb Q$. Thus
$$0=\chi(M)=1-b_1(M)+b_2(M),$$
so $b_1(M)=1+b_2(M)\ge1$.
:::

<1>3. Therefore, under the corrected closedness hypothesis,
$$H^1(M;\mathbb Z)\ne0.$$
::: {.proof}
The universal coefficient theorem gives
$$H^1(M;\mathbb Z)\cong\operatorname{Hom}(H_1(M;\mathbb Z),\mathbb Z).$$
Since $b_1(M)>0$ by <1>2, $H_1(M;\mathbb Z)$ has a nonzero free summand, so the Hom group is nonzero.
:::
:::
