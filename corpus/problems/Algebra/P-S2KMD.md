---
schema: qual/card@1
id: P-S2KMD
kind: problem
title: If $N$ and $G/N$ are solvable then $G$ is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Normal Subgroups
relations: []
review: draft
---

::: {.problem}
Let $N\normal G$. Show that if $N$ and $G/N$ are solvable, then $G$ is solvable.
:::

::: {.solution}

Let $\pi\colon G\to G/N$ be the quotient map, and let $H^{(i)}$ denote the $i$-th derived subgroup of a group $H$.

::: pf

::: {.pf-step #in-N}

There is $r$ with $G^{(r)}\le N$.

::: pf-proof

Since $G/N$ is solvable, $(G/N)^{(r)}=1$ for some $r$. A surjective homomorphism maps commutators onto commutators, so $\pi(G^{(i)})=(G/N)^{(i)}$ for every $i$ by induction. Hence $\pi(G^{(r)})=1$, that is, $G^{(r)}\le N$.

:::

:::

::: pf-qed

Since $N$ is solvable, $N^{(s)}=1$ for some $s$. Derived subgroups are monotone under inclusion, so step [](#in-N){.pf-ref} gives
$$
G^{(r+s)}=(G^{(r)})^{(s)}\le N^{(s)}=1 .
$$
Thus the derived series of $G$ reaches $1$, and $G$ is solvable.

:::

:::

:::
