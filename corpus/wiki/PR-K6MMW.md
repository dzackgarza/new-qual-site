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

::: {.proposition title="?"}
Let $T:V\to V$ be a linear map where $n\da \dim_k V$.
TFAE:

- There exists a basis \( \ts{ e_i } \) of $V$ such that
\[
T(e_i) =
\begin{cases}
e_{i-1} &  i \geq 2
\\
0 & i=1.
\end{cases}
\]

- There exists a cyclic vector $\vector v$ such that \( \ts{ T^k \vector v \st k=1,2,\cdots, n} \) form a basis for $V$.

- $T^{n-1} \neq 0$

- $\dim_k \ker T^\ell = \ell$ for each $1\leq \ell \leq n$.

- $\dim_k \ker T = 1$.
:::
