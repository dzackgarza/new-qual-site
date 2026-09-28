---
schema: qual/card@1
id: P-TOPF09H
kind: problem
title: "Free group F_2 contains subgroups isomorphic to F_n for all n via covering spaces"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Free Groups
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Let $F_n$ denote the free group on $n$ generators.
Use covering space theory to prove that $F_2$ contains subgroups isomorphic to $F_n$ for every $n \geq 1$.
:::

::: {.solution}
<1>1. Let $X=S^1_a\vee S^1_b$, so $\pi_1(X)\cong F_2$.
::: {.proof}
This is the standard bouquet model for the free group of rank two.
:::

<1>2. For $n\ge2$, put $d=n-1$. Construct a connected $d$-sheeted covering graph $Y_d\to X$ with vertices $v_0,\ldots,v_{d-1}$ by letting the $a$-edges form the directed $d$-cycle
$$
v_0\to v_1\to\cdots\to v_{d-1}\to v_0
$$
and placing one $b$-loop at every vertex.
::: {.proof}
At each vertex there is exactly one incoming and one outgoing lift of each oriented edge $a,b$, so this is a covering. The $a$-cycle makes the covering connected.
:::

<1>3. The graph $Y_d$ has rank $d+1=n$.
::: {.proof}
It has $d$ vertices and $2d$ edges, hence
$$
\chi(Y_d)=d-2d=-d,
$$
so its free fundamental group has rank $1-\chi(Y_d)=d+1=n$.
:::

<1>4. Covering-space theory identifies $\pi_1(Y_d)$ with a subgroup of $\pi_1(X)=F_2$. Therefore $F_2$ contains a subgroup isomorphic to $F_n$ for every $n\ge2$.
::: {.proof}
The induced map on fundamental groups of a connected covering is injective.
:::

<1>5. For $n=1$, the cyclic subgroup $\langle a\rangle\le F_2$ is isomorphic to $F_1\cong\mathbb Z$.
::: {.proof}
A free generator has infinite order in a free group.
:::

<1>6. Hence
$$
\boxed{F_2\text{ contains a subgroup isomorphic to }F_n\text{ for every }n\ge1.}
$$
::: {.proof}
Combine <1>4 and <1>5.
:::
:::
