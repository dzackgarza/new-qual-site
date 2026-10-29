---
schema: qual/card@1
id: P-LO76D
kind: problem
title: If $Q/N$ is a Sylow $p$-subgroup of $G/N$ then $Q$ contains a Sylow $p$-subgroup
  of $G$, and every Sylow $p$-subgroup of $G/N$ is such an image
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Isomorphism Theorems
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and let $N \trianglelefteq G$,
and let $p$ be a prime number and $Q$ a subgroup of $G$ such that
$N \subset Q$ and $Q/N$ is a Sylow $p$-subgroup of $G/N$.

(a) Prove that $Q$ contains a Sylow $p$-subgroup of $G$.

(b) Prove that every Sylow $p$-subgroup of $G/N$ is the image of a Sylow $p$-subgroup of $G$.
:::

::: {.solution}
Write $\abs{G}=p^nm$ with $p\nmid m$. A $p$-subgroup $P\le G$ is a Sylow $p$-subgroup exactly when $p\nmid[G:P]$.

::: pf

::: {.pf-step #part-a}
(a) Every Sylow $p$-subgroup of $Q$ is a Sylow $p$-subgroup of $G$.

::: pf-proof
By the third isomorphism theorem, $[G:Q]=[G/N:Q/N]$, which is prime to $p$ because $Q/N$ is Sylow in $G/N$. Let $P$ be a Sylow $p$-subgroup of $Q$. Then $[G:P]=[G:Q]\,[Q:P]$ is a product of two integers prime to $p$, so $P$ is a Sylow $p$-subgroup of $G$ contained in $Q$.
:::

:::

::: pf-step
(b) Every Sylow $p$-subgroup of $G/N$ is the image of a Sylow $p$-subgroup of $G$.

::: pf-proof
Let $\bar P$ be a Sylow $p$-subgroup of $G/N$. By the correspondence theorem, $\bar P=H/N$ for a subgroup $H$ with $N\le H\le G$. Let $P$ be a Sylow $p$-subgroup of $H$.

::: pf-step
$P$ is a Sylow $p$-subgroup of $G$.

::: pf-proof
Apply step [](#part-a){.pf-ref} with $Q=H$.
:::

:::

::: pf-step
$PN/N=\bar P$.

::: pf-proof
Since $P\le H$ and $N\le H$, we have $PN/N\le H/N=\bar P$. By the second isomorphism theorem $PN/N\cong P/(P\cap N)$ is a $p$-group. Its index $[G/N:PN/N]=[G:PN]$ divides $[G:P]$, which is prime to $p$. So $PN/N$ is a Sylow $p$-subgroup of $G/N$, and it has the same order as $\bar P$. Being contained in $\bar P$, it equals $\bar P$.
:::

:::

:::

:::

:::

:::
