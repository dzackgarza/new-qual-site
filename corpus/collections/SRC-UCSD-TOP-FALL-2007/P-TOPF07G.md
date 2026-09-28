---
schema: qual/card@1
id: P-TOPF07G
kind: problem
title: "Second homology of a closed 1-connected 4-manifold is free abelian"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $W$ be a closed (i.e. compact, without boundary) $4$-manifold which is $1$-connected (i.e. is path-connected and simply-connected).
Show that its second homology group is a free abelian group (in other words, has no finite cyclic summands).
:::

::: {.solution}
<1>1. Since $W$ is simply connected,
$$
H_1(W;\mathbb Z)=0.
$$
::: {.proof}
The first homology group is the abelianization of the fundamental group.
:::

<1>2. The universal coefficient theorem gives
$$
H^2(W;\mathbb Z)\cong\operatorname{Hom}(H_2(W;\mathbb Z),\mathbb Z).
$$
::: {.proof}
The UCT exact sequence has left term $\operatorname{Ext}(H_1(W),\mathbb Z)=0$ by <1>1.
:::

<1>3. Poincaré duality gives
$$
H^2(W;\mathbb Z)\cong H_2(W;\mathbb Z).
$$
::: {.proof}
A simply connected closed manifold is orientable, so integral Poincaré duality applies in dimension $4$.
:::

<1>4. The group $\operatorname{Hom}(H_2(W),\mathbb Z)$ is free abelian, hence so is $H_2(W)$.
::: {.proof}
The homology of a compact manifold is finitely generated. For a finitely generated abelian group $A\cong\mathbb Z^r\oplus T$, one has $\operatorname{Hom}(A,\mathbb Z)\cong\mathbb Z^r$. Combine with <1>2--<1>3.
:::
:::
