---
schema: qual/card@1
id: P-TOPS01B
kind: problem
title: "Genus of a double branched cover of S^2 via Euler characteristic"
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Covering Spaces
  - Euler Characteristic
relations: []
review: draft
---

::: problem
Let $\Sigma_g$ be a closed orientable surface of genus $g$.
A map $\pi : \Sigma_g \to S^2$ is a double branched cover if there is a set $Q = \{p_1, p_2, \ldots, p_n\} \subset S^2$ of branch points, so that $\pi$ restricted to $\Sigma_g \setminus \pi^{-1}(Q)$ is a double cover of $S^2 \setminus Q$, but the points $p_i$ have only one preimage each.
Use Euler characteristic to find a formula relating $g$ and $n$.
:::

::: {.solution}
<1>1. Remove pairwise disjoint small open disks around the $n$ branch points of $S^2$. The resulting surface $B$ has
$$
\chi(B)=2-n.
$$
::: {.proof}
Removing one open disk decreases Euler characteristic by one, so removing $n$ disks from $S^2$ gives $2-n$.
:::

<1>2. Remove corresponding small disks around the unique preimages of the branch points in $\Sigma_g$. The resulting surface $\widetilde B$ is an ordinary double cover of $B$.
::: {.proof}
Near a simple branch point a double branched cover is locally modeled by $z\mapsto z^2$. Deleting a small disk around the branch point and its unique preimage removes the ramification, leaving a genuine two-sheeted covering.
:::

<1>3. Therefore
$$
\chi(\widetilde B)=2\chi(B)=4-2n.
$$
::: {.proof}
Euler characteristic multiplies by the degree of a finite covering of finite CW complexes.
:::

<1>4. On the other hand, $\widetilde B$ is obtained from $\Sigma_g$ by deleting $n$ disks, so
$$
\chi(\widetilde B)=2-2g-n.
$$
::: {.proof}
A closed orientable genus-$g$ surface has Euler characteristic $2-2g$, and deleting each disk subtracts one.
:::

<1>5. Equating <1>3 and <1>4 gives
$$
2-2g-n=4-2n,
$$
so
$$
\boxed{n=2g+2}.
$$
::: {.proof}
Rearranging yields $n=2g+2$, equivalently $g=(n-2)/2$.
:::
:::
