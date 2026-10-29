---
schema: qual/card@1
id: P-PZCPD
kind: problem
title: Complex numbers on one side of a line through the origin have nonzero sum and
  sum of reciprocals
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $z_{k}(k=1, \cdots, n)$ be complex numbers lying on the same side of a straight line passing through the origin.
Show that

$$
z_{1}+z_{2}+\cdots+z_{n} \neq 0, \quad 1 / z_{1}+1 / z_{2}+\cdots+1 / z_{n} \neq 0
$$
:::

::: {.hint}
Consider a special situation first.
:::

::: {.solution}
Choose $\lambda$ with $\abs\lambda=1$ such that multiplication by $\lambda$ carries the line onto the imaginary axis and the $z_k$ into the open right half-plane. Replacing $z_k$ by $\lambda z_k$ multiplies the first sum by $\lambda$ and the second by $\lambda^{-1}$, so we may assume $\Re z_k>0$ for every $k$.

::: pf

::: pf-step

$z_1+\cdots+z_n\neq0$.

::: pf-proof

$\Re\left(\sum_{k=1}^n z_k\right)=\sum_{k=1}^n\Re z_k>0$.

:::

:::

::: pf-step

$1/z_1+\cdots+1/z_n\neq0$.

::: pf-proof

For each $k$,
$$
\Re\frac1{z_k}=\Re\frac{\overline{z_k}}{\abs{z_k}^2}=\frac{\Re z_k}{\abs{z_k}^2}>0,
$$
so $\Re\left(\sum_{k=1}^n 1/z_k\right)>0$.

:::

:::

:::

:::
