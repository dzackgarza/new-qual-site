---
schema: qual/card@1
id: P-TOPF19F
kind: problem
title: 'Mapping degree is divisible by $[\pi_1(N):f_*(\pi_1(M))]$'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fundamental Group
  - Manifolds
relations: []
review: draft
---

::: problem
Let $M, N$ be two closed, oriented, $n$-dimensional manifolds.
Show that the mapping degree of a continuous map $f : M \to N$ must be divisible by $[\pi_1(N), f_*(\pi_1(M))]$, the index of the subgroup $f_*(\pi_1(M))$ in $\pi_1(N)$.
:::

::: {.solution}
<1>1. Let $H=f_*(\pi_1(M))\le\pi_1(N)$ and let $p:\widehat N\to N$ be the connected covering corresponding to $H$.
::: {.proof}
The subgroup-covering correspondence applies to the manifolds involved. Its number of sheets is the index $d=[\pi_1(N):H]$, possibly infinite a priori.
:::

<1>2. The map $f$ lifts to a map $\widehat f:M\to\widehat N$ with $f=p\circ\widehat f$.
::: {.proof}
This is the covering-space lifting criterion, since $f_*(\pi_1(M))=H=p_*(\pi_1(\widehat N))$.
:::

<1>3. If $d$ is infinite, then $\deg f=0$.
::: {.proof}
An infinite-sheeted connected cover of the compact manifold $N$ is noncompact. Hence $H_n(\widehat N;\mathbb Z)=0$ for the connected noncompact oriented $n$-manifold $\widehat N$. Thus $\widehat f_*[M]=0$, and consequently $f_*[M]=p_*\widehat f_*[M]=0$.
:::

<1>4. If $d<\infty$, then
$$\deg f=d\,\deg\widehat f.$$
::: {.proof}
The finite covering $p$ has degree $d$ after choosing the lifted orientation on $\widehat N$. Degree is multiplicative under composition, and $f=p\circ\widehat f$.
:::

<1>5. Hence the mapping degree is divisible by
$$\boxed{[\pi_1(N):f_*(\pi_1(M))]}$$
whenever that index is finite; nonzero degree in particular forces the index to be finite.
::: {.proof}
This is immediate from <1>3--<1>4.
:::
:::
