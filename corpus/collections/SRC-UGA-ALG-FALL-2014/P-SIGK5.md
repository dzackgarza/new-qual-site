---
schema: qual/card@1
id: P-SIGK5
kind: problem
title: Jordan forms of a $5\times 5$ matrix with characteristic polynomial $(x-3)^5$
  and minimal polynomial $(x-3)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, and the count checked: block sizes are a partition of 5 with parts at most 2 and at least one part 2, giving 2+2+1 and 2+1+1+1 and nothing else. Written out where the prose only quoted the fact: the exponent of (x-3) in the minimal polynomial is the size of the largest block, because J_s(lambda)^k vanishes exactly for k >= s. Added that the two forms are distinguished by dim ker(T-3I), namely 3 and 4, so the list has no repetitions. Statement unchanged; the card says the argument is its own.
---

::: {.problem}
Let $T$ be a $5\times 5$ complex matrix with characteristic polynomial $\chi(x) = (x-3)^5$ and minimal polynomial $m(x) = (x-3)^2$.
Determine all possible Jordan forms of $T$.
:::

::: {.solution}
The characteristic polynomial fixes the eigenvalue and that the block sizes sum to $5$; the minimal polynomial fixes the size of the largest block at exactly $2$. So the block sizes are a partition of $5$ into parts $1$ and $2$ with at least one $2$, of which there are two. The argument is this card's own: the checkout retains no solution set for this exam.

::: pf

::: {.pf-step #eigen}
Every Jordan block of $T$ is a block for the eigenvalue $3$, and the sum of the block sizes is $5$.

::: pf-proof
The characteristic polynomial is $\chi(x)=\det(xI-T)=(x-3)^5$, so its only root is $3$, with algebraic multiplicity $5$; the eigenvalues of $T$ are the roots of $\chi$, and the algebraic multiplicity of an eigenvalue is the sum of the sizes of its Jordan blocks. Hence all blocks belong to $3$ and their sizes sum to $5$.
:::

:::


::: {.pf-step #largest}
The size of the largest Jordan block of $T$ is exactly $2$.

::: pf-proof
For a single eigenvalue the minimal polynomial is $\prod(x-\lambda)^{m_\lambda}$ where $m_\lambda$ is the size of the largest Jordan block for $\lambda$; this holds because the $k$-th power of a Jordan block $J_s(\lambda)$ is zero exactly when $k\ge s$. Here $m_T(x)=(x-3)^2$, so the largest block has size $2$.
:::

:::


::: {.pf-step #partitions}
The possible multisets of block sizes are $\{2,2,1\}$ and $\{2,1,1,1\}$.

::: pf-proof
By steps [](#eigen){.pf-ref} and [](#largest){.pf-ref} the block sizes are positive integers, each at most $2$, at least one equal to $2$, with sum $5$. If there are two $2$'s the remaining part is $1$; if there is exactly one $2$ the remaining three parts are all $1$. So the only possibilities are $2+2+1$ and $2+1+1+1$.
:::

:::


::: {.pf-step #realized}
Both multisets occur, with the displayed Jordan forms, and they are not similar to each other.

::: pf-proof
Let $J_2(3)=\begin{pmatrix}3&1\\0&3\end{pmatrix}$. The matrix $J_2(3)\oplus J_2(3)\oplus[3]$ has characteristic polynomial $(x-3)^5$ and minimal polynomial $(x-3)^2$, and so does $J_2(3)\oplus[3]\oplus[3]\oplus[3]$: in each case the eigenvalue is $3$ with algebraic multiplicity $5$ and the largest block has size $2$. The two are not similar because the number of Jordan blocks for $3$ is the geometric multiplicity $\dim\ker(T-3I)$, which is $3$ for the first and $4$ for the second.
:::

:::


::: {.pf-step #conclusion}
The possible Jordan forms of $T$ are, up to ordering of the blocks, $J_2(3)\oplus J_2(3)\oplus[3]$ and $J_2(3)\oplus[3]\oplus[3]\oplus[3]$.

::: pf-proof
Step [](#partitions){.pf-ref} shows there are no others and step [](#realized){.pf-ref} that both occur and are distinct, so the list is complete and without repetition.
:::

:::

:::
:::
