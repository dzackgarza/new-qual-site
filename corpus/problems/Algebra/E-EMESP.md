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

<1>1. $N$ is a disjoint union of $G$-conjugacy classes, and the classes of size $1$ contained in $N$ are the elements of $N\cap Z(G)$.

::: {.proof}
Normality gives $gng^{-1}\in N$ for $n\in N$, $g\in G$, so the $G$-conjugacy class of each $n\in N$ lies in $N$.
The class of $n$ is $\{n\}$ exactly when $n$ commutes with every element of $G$.
:::

<1>2. Every $G$-conjugacy class of size greater than $1$ has size divisible by $p$.

::: {.proof}
The class of $n$ has size $[G:C_G(n)]$, which divides $|G|$ and so is a power of $p$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $|N|\equiv|N\cap Z(G)|\pmod p$.
Since $N\neq1$ is a subgroup of a $p$-group, $p\mid|N|$, so $p\mid|N\cap Z(G)|$.
As $e\in N\cap Z(G)$, this gives $|N\cap Z(G)|\ge p$, so $N\cap Z(G)\neq1$.
:::
:::
