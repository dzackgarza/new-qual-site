---
schema: qual/card@1
id: P-VPB55
kind: problem
title: Jordan canonical form over a non-algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Canonical Forms
  - Rational Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Talk about Jordan canonical form.
What happens when the field is not algebraically closed?
:::

::: {.solution}
Let $A$ be an $n\times n$ matrix over a field $F$.

::: pf

::: pf-step
If $F$ is algebraically closed, $A$ is similar to a direct sum of Jordan blocks $J_m(\lambda)$, and for each eigenvalue $\lambda$ the numbers and sizes of the blocks are determined by the nullities of the powers $(A-\lambda I)^k$.

::: pf-proof
The characteristic polynomial splits, so $F^n$ is the direct sum of the generalized eigenspaces, and on each the nilpotent operator $A-\lambda I$ has a Jordan form.
The number of blocks for $\lambda$ of size at least $k$ is $\dim\ker(A-\lambda I)^k-\dim\ker(A-\lambda I)^{k-1}$.
:::

:::

::: pf-step
If $F$ is not algebraically closed, a Jordan form over $F$ need not exist.

::: pf-proof
The characteristic polynomial may not split.
For example, the real rotation $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ has characteristic polynomial $x^2+1$, so it has no real eigenvalues and hence no Jordan form over $\RR$.
:::

:::

::: pf-step
Over every field, $A$ is similar to its rational canonical form, which refines to the Jordan form when every invariant factor splits into powers of linear factors.

::: pf-proof
View $F^n$ as an $F[x]$-module via $x\cdot v=Av$.
The structure theorem over the PID $F[x]$ gives invariant factors $d_1\mid d_2\mid\cdots\mid d_r$, and the rational canonical form is the block diagonal matrix of their companion matrices.
When all invariant factors split, the elementary divisor decomposition gives cyclic summands $F[x]/(x-\lambda)^m$, on each of which $A$ acts as $J_m(\lambda)$.
:::

:::

:::
:::
