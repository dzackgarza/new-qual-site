---
schema: qual/card@1
id: PR-434DX
kind: proposition
title: Recurrence for the partition numbers $P_k(n)$ and $P(n)$
classification:
  areas:
  - algebra
  topics:
  - Partitions
  - Number Theory
relations: []
review: draft
---

::: {.proposition}
For integers $m \geq 0$ and $k \geq 0$, let $P_k(m)$ be the number of partitions of $m$ into exactly $k$ positive parts, so that $P_0(0) = 1$, $P_0(m) = 0$ for $m \geq 1$, and $P_k(m) = 0$ for $k > m$.
Let $P(m) \coloneqq \sum_{k=0}^m P_k(m)$ be the number of partitions of $m$.
Then for $n \geq k \geq 1$,
$$
P_k(n) = P_k(n-k) + P_{k-1}(n-1),
$$
and for $n \geq 1$,
$$
P(n) = \sum_{k=1}^n P_k(n-k) + P(n-1).
$$
:::

::: {.proof}
Divide the partitions of $n$ into $k$ parts into two classes.
Those whose parts are all at least $2$ correspond bijectively to partitions of $n-k$ into $k$ parts, by subtracting $1$ from each part; in the other direction, $[1,1,1,3] \mapsto [2,2,2,4]$.
Those with a part equal to $1$ correspond bijectively to partitions of $n-1$ into $k-1$ parts, by deleting one part equal to $1$; in the other direction, $[1,1,2,5] \mapsto [1,1,2,5,1]$.
This proves the first identity.

Summing it over $1 \leq k \leq n$ gives
$$
P(n) = \sum_{k=1}^n P_k(n-k) + \sum_{j=0}^{n-1} P_j(n-1) = \sum_{k=1}^n P_k(n-k) + P(n-1).
$$
Applying the same identity to $P(n-1)$, $P(n-2)$, and so on computes $P(n)$ recursively:
$$
\begin{aligned}
P(n)
&= \sum_{k=1}^n P_k(n-k) + P(n-1) \\
&= \sum_{k=1}^n P_k(n-k) + \sum_{k=1}^{n-1} P_k(n-1-k) + P(n-2) \\
&= \cdots
\end{aligned}
$$
:::
