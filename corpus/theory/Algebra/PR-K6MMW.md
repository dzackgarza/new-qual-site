---
schema: qual/card@1
id: PR-K6MMW
kind: proposition
title: Equivalent characterizations of a single nilpotent Jordan block of size $n$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Jordan Canonical Form
  - Linear Algebra
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, $V$ a $k$-vector space of dimension $n \coloneqq \dim_k V \geq 1$, and $T\colon V\to V$ a nilpotent linear map.
The following are equivalent:

- There exists a basis $e_1, \ldots, e_n$ of $V$ such that
$$
T(e_i) =
\begin{cases}
e_{i-1} & \text{if } i \geq 2,
\\
0 & \text{if } i=1.
\end{cases}
$$

- There exists a cyclic vector $v \in V$: the vectors $T^k v$ for $k = 0, 1, \ldots, n-1$ form a basis of $V$.

- $T^{n-1} \neq 0$.

- $\dim_k \ker T^\ell = \ell$ for each $1\leq \ell \leq n$.

- $\dim_k \ker T = 1$.
:::
