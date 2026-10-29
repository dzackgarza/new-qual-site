---
schema: qual/card@1
id: E-DR5LY
kind: problem
title: Hadamard expansion of $\sin$
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Factorization
  - Entire Functions
  - Zeros
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Find a Hadamard expansion of $\sin(\pi z)$.
:::

::: {.solution}

::: pf

::: {.pf-step #hadamard-form}
There are constants $a,b\in\CC$ with
$$
\sin(\pi z) = ze^{az+b} \prod_{k\in \ZZ\smz} \qty{1 - {z\over k}}e^{z\over k} = ze^{az+b} \prod_{k\geq 1}\qty{1 - {z^2\over k^2}}.
$$

::: pf-proof
The function $\sin(\pi z)$ is entire of order $1$, and its zeros are the integers, each simple.
The Hadamard factorization theorem gives the first product, with genus $1$.
Grouping the factors for $k$ and $-k$ gives $\qty{1-\frac zk}e^{z/k}\qty{1+\frac zk}e^{-z/k}=1-\frac{z^2}{k^2}$, which gives the second product.
:::

:::

::: {.pf-step #constants}
$a=0$ and $e^b=\pi$.

::: pf-proof
Put $P(z)=\prod_{k\geq 1}\qty{1-z^2/k^2}$, so that $e^{az+b}=\sin(\pi z)/(zP(z))$ off the integers.
The right side is even, because $\sin(\pi z)$ and $z$ are odd and $P$ is even.
Hence $e^{az}=e^{-az}$ for all $z$, so $e^{2az}=1$ and $a=0$.
Letting $z\to0$ gives $e^b=\lim_{z\to0}\sin(\pi z)/z=\pi$, since $P(0)=1$.
:::

:::

::: pf-step
$$
\boxed{\sin(\pi z) = \pi z \prod_{k\geq 1}\qty{1- {z^2\over k^2}}}.
$$

::: pf-proof
Substitute step [](#constants){.pf-ref} into step [](#hadamard-form){.pf-ref}.
:::

:::

:::

:::
