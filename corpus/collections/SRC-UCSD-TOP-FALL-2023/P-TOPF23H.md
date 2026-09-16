---
schema: qual/card@1
id: P-TOPF23H
kind: problem
title: "Transfer map for free group actions: rational homology of the quotient is the invariant part"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Group Actions
  - Covering Spaces
  - Transfer Map
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group of order $d$ acting freely on a space $X$, so that we have a covering map $\pi : X \to Y = X/G$.
By lifting singular simplexes, construct a chain map $\tau_* : C_*(Y; \mathbb{Z}) \to C_*(X; \mathbb{Z})$ such that the composite $C_*(Y; \mathbb{Z}) \xrightarrow{\tau_*} C_*(X; \mathbb{Z}) \xrightarrow{\pi_*} C_*(Y; \mathbb{Z})$ is multiplication by $d$.
Use this to show that we can identify the rational homology of $Y$ with the $G$-invariant subspace of the rational homology of $X$:
$$
H_*(Y; \mathbb{Q}) \cong H_*(X; \mathbb{Q})^G.
$$
:::

::: {.solution}
<1>1. For a singular simplex $\sigma:\Delta^n\to Y$, choose one lift $\widetilde\sigma:\Delta^n\to X$ and define
$$\tau_n(\sigma)=\sum_{g\in G}g\widetilde\sigma.$$
::: {.proof}
The simplex has exactly $d=|G|$ lifts, and they are precisely the translates of any chosen lift. Thus the sum is independent of the chosen lift.
:::

<1>2. The maps $\tau_n$ form a chain map
$$\tau_*:C_*(Y;\mathbb Z)\to C_*(X;\mathbb Z).$$
::: {.proof}
Taking faces commutes with lifting and with the $G$-action, so
$$\partial\tau_n(\sigma)=\sum_g g\,\partial\widetilde\sigma=\tau_{n-1}(\partial\sigma).$$
:::

<1>3. The composite $\pi_*\tau_*$ is multiplication by $d$.
::: {.proof}
Every translated lift projects back to $\sigma$, so
$$\pi_*\tau_n(\sigma)=\sum_{g\in G}\sigma=d\sigma.$$
:::

<1>4. The other composite satisfies
$$\tau_*\pi_* = \sum_{g\in G}g_*$$
on $C_*(X;\mathbb Z)$ and hence on homology.
::: {.proof}
For a simplex in $X$, the lifts of its projection to $Y$ are exactly its $G$-translates.
:::

<1>5. Over $\mathbb Q$, the map
$$\pi_*:H_*(X;\mathbb Q)^G\longrightarrow H_*(Y;\mathbb Q)$$
is an isomorphism with inverse $d^{-1}\tau_*$. 
::: {.proof}
By <1>3, $\pi_*(d^{-1}\tau_*)=\operatorname{id}$. If $x$ is $G$-invariant, then <1>4 gives
$$d^{-1}\tau_*\pi_*(x)=d^{-1}\sum_g g_*x=x.$$
Also the image of $\tau_*$ is $G$-invariant because translation permutes the summands.
:::

<1>6. Therefore
$$\boxed{H_*(Y;\mathbb Q)\cong H_*(X;\mathbb Q)^G.}$$
::: {.proof}
This is exactly <1>5.
:::
:::
