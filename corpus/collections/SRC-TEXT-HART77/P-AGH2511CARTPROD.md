---
schema: qual/card@1
id: P-AGH2511CARTPROD
kind: problem
title: The Cartesian product of graded rings and the Segre embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Graded Rings
  - Proj
  - Segre Embedding
relations: []
review: draft
---

::: problem
Let $S$ and $T$ be two graded rings with $S_0 = T_0 = A$.
Define the **Cartesian product** $\fiberprod{S}{A}{T}$ to be the graded ring $\bigoplus_{d \geq 0} S_d \tensor_A T_d$.
If $X = \Proj S$ and $Y = \Proj T$, show that $\Proj(\fiberprod{S}{A}{T}) \cong \fiberprod{X}{A}{Y}$, and show that the sheaf $\OO(1)$ on $\Proj(\fiberprod{S}{A}{T})$ is isomorphic to $p_1^*(\OO_X(1)) \tensor p_2^*(\OO_Y(1))$ on $X \times Y$.

The Cartesian product of rings is related to the **Segre embedding** of projective spaces (I, Ex. 2.14) as follows.
If $x_0, \ldots, x_r$ generate $S_1$ over $A$, corresponding to a projective embedding $X \injects \PP^r_A$, and if $y_0, \ldots, y_s$ generate $T_1$, corresponding to $Y \injects \PP^s_A$, then $\ts{x_i \tensor y_j}$ generates $(\fiberprod{S}{A}{T})_1$, and hence defines a projective embedding $\Proj(\fiberprod{S}{A}{T}) \injects \PP^N_A$ with $N = rs + r + s$.
This is just the image of $X \times Y \subseteq \PP^r \times \PP^s$ in its Segre embedding.
:::
