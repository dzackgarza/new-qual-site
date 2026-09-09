---
schema: qual/card@1
id: P-UCTOP-SU01-2
kind: problem
title: Euler characteristic formula for double branched cover of surface
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

Let $\Sigma_g$ be a closed orientable surface of genus $g$.
A map $\pi : \Sigma_g \to S^2$ is a double branched cover if there is a set $Q = \{p_1, p_2, \ldots, p_n\} \subseteq S^2$ of branch points, so that $\pi$ restricted to $\Sigma_g - \pi^{-1}(Q)$ is a double cover of $S^2 - Q$, but the points $p_i$ have only one preimage each.
Use Euler characteristic to find a formula relating $g$ and $n$.

::: {.solution}
<1>1. Choose a CW decomposition of $S^2$ whose branch points $p_1,\dots,p_n$ are vertices.
::: {.proof}
After subdividing a triangulation of the sphere, we may assume every branch point is a $0$-cell and no other cell contains a branch point in its interior.
:::

<1>2. Every non-branch $0$-cell and every positive-dimensional cell has two lifts to $\Sigma_g$, while each branch vertex has only one lift.
::: {.proof}
Away from the branch set, $\pi$ is an ordinary double covering, so every sufficiently small cell lifts to two disjoint copies. By definition, each branch point has a single preimage.
:::

<1>3. Hence
$$
\chi(\Sigma_g)=2\chi(S^2)-n.
$$
::: {.proof}
If the chosen CW decomposition has $c_k$ $k$-cells and exactly $n$ of the $c_0$ vertices are branch points, then the lifted CW structure has $2c_k$ cells for $k>0$ and $2c_0-n$ vertices. Therefore
$$
\chi(\Sigma_g)=(2c_0-n)-2c_1+2c_2=2(c_0-c_1+c_2)-n.
$$
:::

<1>4. Substituting the Euler characteristics of the surfaces gives
$$
2-2g=4-n.
$$
::: {.proof}
For a closed orientable surface of genus $g$, $\chi(\Sigma_g)=2-2g$, while $\chi(S^2)=2$.
:::

<1>5. Therefore
$$
\boxed{n=2g+2}.
$$
::: {.proof}
Rearrange the equation in <1>4.
:::
:::

