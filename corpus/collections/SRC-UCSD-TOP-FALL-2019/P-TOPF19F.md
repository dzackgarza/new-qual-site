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

::: {.problem}
Let $M, N$ be two closed, oriented, $n$-dimensional manifolds.
Show that the mapping degree of a continuous map $f : M \to N$ must be divisible by $[\pi_1(N), f_*(\pi_1(M))]$, the index of the subgroup $f_*(\pi_1(M))$ in $\pi_1(N)$.
:::

::: {.solution}

::: pf

::: pf-step

Let $H=f_*(\pi_1(M))\le\pi_1(N)$ and let $p:\widehat N\to N$ be the connected covering corresponding to $H$.

::: pf-proof

The subgroup-covering correspondence applies to the manifolds involved. Its number of sheets is the index $d=[\pi_1(N):H]$, possibly infinite a priori.

:::

:::

::: pf-step

The map $f$ lifts to a map $\widehat f:M\to\widehat N$ with $f=p\circ\widehat f$.

::: pf-proof

This is the covering-space lifting criterion, since $f_*(\pi_1(M))=H=p_*(\pi_1(\widehat N))$.

:::

:::

::: {.pf-step #s3}

If $d$ is infinite, then $\deg f=0$.

::: pf-proof

An infinite-sheeted connected cover of the compact manifold $N$ is noncompact. Hence $H_n(\widehat N;\mathbb Z)=0$ for the connected noncompact oriented $n$-manifold $\widehat N$. Thus $\widehat f_*[M]=0$, and consequently $f_*[M]=p_*\widehat f_*[M]=0$.

:::

:::

::: {.pf-step #s4}

If $d<\infty$, then
$$\deg f=d\,\deg\widehat f.$$

::: pf-proof

The finite covering $p$ has degree $d$ after choosing the lifted orientation on $\widehat N$. Degree is multiplicative under composition, and $f=p\circ\widehat f$.

:::

:::

::: pf-step

Hence the mapping degree is divisible by
$$\boxed{[\pi_1(N):f_*(\pi_1(M))]}$$
whenever that index is finite; nonzero degree in particular forces the index to be finite.

::: pf-proof

This is immediate from steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
