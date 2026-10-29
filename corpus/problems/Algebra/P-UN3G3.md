---
schema: qual/card@1
id: P-UN3G3
kind: problem
title: The number and sizes of Jordan blocks
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $A \in M_n(\CC)$ (or an algebraically closed field).
How do you determine the **number** and **sizes** of the blocks in the Jordan Canonical Form of $A$?
:::

::: {.solution}
Fix an eigenvalue $\lambda$ and set $d_k=\dim\ker(A-\lambda I)^k$ for $k\ge0$, so $d_0=0$.
Let $m_1,\ldots,m_r$ be the sizes of the Jordan blocks for $\lambda$.

::: pf

::: {.pf-step #nullity}

$d_k=\sum_{j=1}^r\min(k,m_j)$.

::: pf-proof

$(A-\lambda I)^k$ is invertible on the blocks for the other eigenvalues. On a Jordan block $J_m(\lambda)$, $(J_m(\lambda)-\lambda I)^k$ is the $k$th power of a nilpotent shift of size $m$, whose kernel has dimension $\min(k,m)$.

:::

:::

::: {.pf-step #atleast}

$d_k-d_{k-1}$ is the number of Jordan blocks for $\lambda$ of size at least $k$.

::: pf-proof

By step [](#nullity){.pf-ref}, $d_k-d_{k-1}=\sum_j\bigl(\min(k,m_j)-\min(k-1,m_j)\bigr)$, and each summand is $1$ if $m_j\ge k$ and $0$ otherwise.

:::

:::

::: pf-step

The number of blocks for $\lambda$ is $d_1$, and the number of blocks of size exactly $k$ is
$$
(d_k-d_{k-1})-(d_{k+1}-d_k)=\boxed{2d_k-d_{k-1}-d_{k+1}}.
$$

::: pf-proof

This follows from step [](#atleast){.pf-ref} with $k=1$, and by subtracting the number of blocks of size at least $k+1$ from the number of size at least $k$.

:::

:::

::: pf-step

The largest block size for $\lambda$ is the least $m$ with $d_m=d_{m+1}$, and it equals the exponent of $(x-\lambda)$ in the minimal polynomial of $A$.

::: pf-proof

By step [](#atleast){.pf-ref}, $d_{m+1}=d_m$ exactly when no block has size at least $m+1$. The minimal polynomial of $J_m(\lambda)$ is $(x-\lambda)^m$, and the minimal polynomial of $A$ is the least common multiple of those of its blocks.

:::

:::

::: pf-qed

Thus the nullities of the powers $(A-\lambda I)^k$, for each eigenvalue $\lambda$, determine the number and sizes of all Jordan blocks.

:::

:::

:::
