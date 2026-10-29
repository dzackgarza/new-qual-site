---
schema: qual/card@1
id: P-MQ3H7
kind: problem
title: Square roots of matrices over $\CC$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Does every complex matrix $A$ admit a complex matrix square root $B$ with
$$
B^2=A?
$$
:::

::: {.solution}
Let $A=J_2(0)=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, the nilpotent Jordan block of size $2$.

::: pf

::: pf-step
$\boxed{\text{No}}$: there is no complex $2\times 2$ matrix $B$ with $B^2=A$.

::: pf-proof
Suppose $B^2=A$.
Every eigenvalue $\mu$ of $B$ satisfies $\mu^2=0$, since $\mu^2$ is an eigenvalue of $A$, so $B$ is nilpotent.
By the Cayley--Hamilton theorem, the characteristic polynomial of $B$ is $x^2$, so $B^2=0\ne A$, a contradiction.
:::

:::

:::

:::

::: {.remark}
Every invertible complex matrix has a square root: on a Jordan block $J_r(\lambda)=\lambda(I+N/\lambda)$ with $\lambda\ne0$, choose a square root of $\lambda$ and use the binomial series for $(I+N/\lambda)^{1/2}$, which terminates because $N$ is nilpotent.
:::
