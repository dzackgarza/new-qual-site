---
schema: qual/card@1
id: P-BKF09-8B
kind: problem
title: Embeddings of $C_6$ into $\mathbb R^*$, $\mathbb C^*$, $C_2\times C_3$, $S_4$ and $\operatorname{SL}_2(\mathbb R)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n$ be a positive integer, $C_n$ the cyclic group of order $n$, and $S_n$ the symmetric group on $n$ points.
For each of the groups
$$
A=\RR^*,\qquad B=\CC^*,\qquad C=C_2\times C_3,\qquad D=S_4,\qquad E=\operatorname{SL}_2(\RR)
$$
prove or disprove that $C_6$ is isomorphic to a subgroup of it.
:::

::: {.solution}
$C_6$ is not a subgroup of $A$ because in $\RR^*$, if $r\neq\pm1$, then $r^6\neq1$, or of $D$ because if $s\in D$ and $s$ is not the identity, $s$ has a cycle decomposition of the form $(ab)(cd)$, $(abc)$ or $(abcd)$, and these have orders $2$, $3$ and $4$.
$C_6$ is a subgroup of $B$, $C$ and $E$ because $\cos(\pi/3)+i\sin(\pi/3)\in B$, $(1,1)\in C$, and
$$
\begin{pmatrix}\cos(2\pi/3)&-\sin(2\pi/3)\\\sin(2\pi/3)&\cos(2\pi/3)\end{pmatrix}\in E
$$
all have order $6$.
:::
