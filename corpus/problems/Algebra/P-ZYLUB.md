---
schema: qual/card@1
id: P-ZYLUB
kind: problem
title: $4\times 4$ Jordan forms with minimal polynomial $(x-1)(x-2)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Give the $4 \times 4$ Jordan forms with minimal polynomial $(x - 1)(x - 2)^2$.
:::

::: {.solution}
Let $A$ be a $4\times4$ matrix with $m_A(x)=(x-1)(x-2)^2$, and write $J_k(\lambda)$ for the $k\times k$ Jordan block with eigenvalue $\lambda$.

::: pf

::: {.pf-step #blocks}

The eigenvalues of $A$ are $1$ and $2$; every block for eigenvalue $1$ has size $1$ and at least one occurs; every block for eigenvalue $2$ has size at most $2$ and at least one has size exactly $2$.

::: pf-proof

The exponent of $x-\lambda$ in the minimal polynomial is the size of the largest Jordan block for $\lambda$, and the roots of $m_A$ are exactly the eigenvalues.

:::

:::

::: pf-step

Up to the order of the blocks, the Jordan forms are $\boxed{J_2(2)\oplus[1]\oplus[1]}$ and $\boxed{J_2(2)\oplus[2]\oplus[1]}$.

::: pf-proof

By step [](#blocks){.pf-ref}, the eigenvalue-$2$ blocks contain a $J_2(2)$ and the eigenvalue-$1$ blocks take at least one dimension, so the eigenvalue-$2$ part has dimension $2$ or $3$. Dimension $2$ gives $J_2(2)$ together with two blocks $[1]$. Dimension $3$ gives $J_2(2)\oplus[2]$ together with one block $[1]$. Both have minimal polynomial $(x-1)(x-2)^2$.

:::

:::

:::

:::
