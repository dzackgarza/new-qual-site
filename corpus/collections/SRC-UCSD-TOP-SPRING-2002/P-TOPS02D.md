---
schema: qual/card@1
id: P-TOPS02D
kind: problem
title: "Properties of covering spaces: manifolds, topological groups, and cell complexes"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Manifolds
  - Topological Groups
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $p : E \to X$ be a covering space.

(a) If $X$ is a manifold, prove $E$ is also.

(b) If $X$ is a topological group, sketch a proof that there is a multiplication map $m : E \times E \to E$ such that $pm = \mu \circ (p \times p)$ where $\mu : X \times X \to X$ is the multiplication on $X$.

(c) If $X$ is a cell complex, prove $E$ is also.
:::

::: {.solution}
<1>1. Part (a) is true: if $X$ is a manifold, then $E$ is a manifold of the same dimension.
::: {.proof}
Every $e\in E$ has an evenly covered neighborhood: there is an open neighborhood $U$ of $p(e)$ and a sheet $V\ni e$ such that $p|_V:V\to U$ is a homeomorphism. Choosing $U$ inside a manifold chart transfers that chart to $V$.
:::

<1>2. Part (b) is false for an arbitrary disconnected covering.
::: {.proof}
Take $X=S^1$ as a topological group. Let $E$ be the disjoint union of the connected $2$-sheeted and $3$-sheeted coverings of $S^1$. Suppose a multiplication $m:E\times E\to E$ with
$$p\circ m=\mu\circ(p\times p)$$
existed. Restrict to the product $E_2\times E_3$ of the two connected components. This domain is connected, so its image lies in one component of $E$, whose covering subgroup is either $2\mathbb Z$ or $3\mathbb Z$ inside $\pi_1(S^1)=\mathbb Z$.

On fundamental groups, however, the map $\mu\circ(p\times p):E_2\times E_3\to S^1$ has image
$$2\mathbb Z+3\mathbb Z=\mathbb Z.$$
The covering-space lifting criterion therefore forbids a lift to either component, a contradiction.
:::

<1>3. If $X$ and $E$ are path-connected and a point $e_0\in p^{-1}(1_X)$ is chosen, then part (b) has the standard corrected form: there is a unique lift
$$m:E\times E\to E,\qquad p\circ m=\mu\circ(p\times p),\qquad m(e_0,e_0)=e_0.$$
::: {.proof}
Let $H=p_*\pi_1(E,e_0)\le\pi_1(X,1_X)$. For a topological group, the multiplication map induces addition under the canonical abelian group structure on $\pi_1(X)$, so
$$\mu_*(H\times H)=H+H=H.$$
Thus the lifting criterion applies to $\mu\circ(p\times p)$, giving the required lift. Uniqueness follows from uniqueness of lifts on the connected domain $E\times E$.
:::

<1>4. Part (c) is true: if $X$ is a CW complex, then $E$ admits a CW structure for which $p$ is cellular and every cell maps homeomorphically to a cell of $X$.
::: {.proof}
Lift the cells inductively. Over each open cell $e^n\subset X$, the covering is trivial because $e^n$ is simply connected, so each component of $p^{-1}(e^n)$ maps homeomorphically onto $e^n$. Lift each characteristic map $D^n\to X$ after choosing a point in the desired sheet over the cell interior. Its boundary lands in the already constructed inverse image of the $(n-1)$-skeleton by uniqueness of lifting. These lifted characteristic maps give the required CW structure on $E$.
:::
:::
