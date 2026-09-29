---
schema: qual/card@1
id: E-EMESP
kind: problem
title: Nontrivial normal subgroups of a $p$-group meet the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Class Equation
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.exercise}
Prove that if $G$ is a $p\dash$group, every subgroup $N\normal G$ intersects the center $Z(G)$.

> Hint: use the class equation.

:::

::: {.solution}
Let $G$ be a finite $p$-group and $1\neq N\normal G$.

::: pf

::: {.pf-step #n-classes-fixed-points-eq-cap-z}
$N$ is a disjoint union of $G$-conjugacy classes, and the classes of size $1$ contained in $N$ are the elements of $N\cap Z(G)$.

::: pf-proof
Normality gives $gng^{-1}\in N$ for $n\in N$, $g\in G$, so the $G$-conjugacy class of each $n\in N$ lies in $N$.
The class of $n$ is $\{n\}$ exactly when $n$ commutes with every element of $G$.
:::

:::

::: {.pf-step #nontrivial-classes-div-by-p}
Every $G$-conjugacy class of size greater than $1$ has size divisible by $p$.

::: pf-proof
The class of $n$ has size $[G:C_G(n)]$, which divides $|G|$ and so is a power of $p$.
:::

:::

::: pf-qed
By steps [](#n-classes-fixed-points-eq-cap-z){.pf-ref} and [](#nontrivial-classes-div-by-p){.pf-ref}, $|N|\equiv|N\cap Z(G)|\pmod p$.
Since $N\neq1$ is a subgroup of a $p$-group, $p\mid|N|$, so $p\mid|N\cap Z(G)|$.
As $e\in N\cap Z(G)$, this gives $|N\cap Z(G)|\ge p$, so $N\cap Z(G)\neq1$.
:::

:::

:::
