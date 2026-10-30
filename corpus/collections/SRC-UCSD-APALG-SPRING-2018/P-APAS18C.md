---
schema: qual/card@1
id: P-APAS18C
kind: problem
title: Cauchy–Schwarz form $\abs{x^*y}^2\leq(x^*Px)(y^*P^{-1}y)$ for positive definite $P$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $P\in\CC^{n\times n}$ be a positive definite Hermitian matrix.
Show that
$$
\abs{x^*y}^2\leq(x^*Px)(y^*P^{-1}y)
$$
for all $x,y\in\CC^n$.
:::

::: {.solution}

::: pf

::: {.pf-step #factor}

$x^*y=(P^{1/2}x)^*(P^{-1/2}y)$, where $P^{1/2}$ is the positive definite square root of $P$.

::: pf-proof

$P$ is Hermitian positive definite, so $P=W\Lambda W^*$ with $W$ unitary and $\Lambda$ diagonal with positive entries. Then $P^{1/2}\coloneqq W\Lambda^{1/2}W^*$ is Hermitian, invertible and squares to $P$, and $(P^{1/2}x)^*(P^{-1/2}y)=x^*P^{1/2}P^{-1/2}y=x^*y$.

:::

:::

::: pf-step

$\abs{x^*y}^2\le(x^*Px)(y^*P^{-1}y)$.

::: pf-proof

By step [](#factor){.pf-ref} and the Cauchy--Schwarz inequality in $\CC^n$, $\abs{x^*y}^2\le\norm{P^{1/2}x}^2\norm{P^{-1/2}y}^2$. Since $P^{1/2}$ is Hermitian, $\norm{P^{1/2}x}^2=x^*P^{1/2}P^{1/2}x=x^*Px$ and $\norm{P^{-1/2}y}^2=y^*P^{-1}y$.

:::

:::

:::
:::
