---
schema: qual/card@1
id: P-ALGF23E
kind: problem
title: "Jordan form of a matrix with minimal polynomial t^p - 1 over C and F_p"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Suppose $p$ is a prime number and the minimal polynomial of $a \in M_p(F)$ is $t^p - 1$.

(a) Find the Jordan form of $a$ if $F = \mathbb{C}$.
Justify your answer.

(b) Find the Jordan form of $a$ if $F = \mathbb{F}_p$.
Justify your answer.
:::

::: solution
**Goal:** Read Jordan form from the minimal polynomial in characteristic $0$ and characteristic $p$.

<1> Over $\mathbb C$, factor
    $$
    t^p-1=\prod_{k=0}^{p-1}(t-\zeta_p^k),\qquad \zeta_p=e^{2\pi i/p}.
    $$
    The factors are distinct.
    Since the minimal polynomial is squarefree, every Jordan block has size $1$.
    So $a$ is diagonalizable and its Jordan form is diagonal with only $p$-th roots of unity on the diagonal.

<1> Over $F=\mathbb F_p$, by Freshman’s dream
    $$
    t^p-1=(t-1)^p.
    $$
    Hence the only eigenvalue is $1$.
    Because the minimal polynomial has degree $p$, the largest Jordan block size is $p$.
    But the matrix size is $p$, so there is exactly one block of size $p$.

<1> Therefore the Jordan form over $\mathbb F_p$ is $J_p(1)$, the single size-$p$ Jordan block with eigenvalue $1$.

Authored by **Codex 5.3 Spark Extra High**.
:::
