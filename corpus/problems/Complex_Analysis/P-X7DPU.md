---
schema: qual/card@1
id: P-X7DPU
kind: problem
title: Partial sums $P_n(z)=\sum_{k=0}^n z^k/k!$ are eventually zero-free on $\abs{z}\le R$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Polynomials
relations: []
review: draft
---

::: {.problem}
For $R>0$, show that there is $N_R$ such that for $n>N_R$,
$$
P_n(z)=1+z+\frac{z^2}{2!}+\cdots+\frac{z^n}{n!}\ne0
\qquad(\abs{z}\le R).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #lower}
$\abs{e^z}\ge e^{-R}$ for $\abs{z}\le R$.

::: pf-proof
$\abs{e^z}=e^{\Re z}$ and $\Re z\ge-\abs{z}\ge-R$.
:::

:::

::: {.pf-step #unif}
There is $N_R$ such that $\sup_{\abs{z}\le R}\abs{P_n(z)-e^z}<e^{-R}/2$ for $n>N_R$.

::: pf-proof
The $P_n$ are the partial sums of the power series of $e^z$, which has infinite radius of convergence, so they converge uniformly to $e^z$ on every closed disk.
:::

:::

::: pf-step
$P_n(z)\ne0$ for $\abs{z}\le R$ and $n>N_R$.

::: pf-proof
By steps [](#lower){.pf-ref} and [](#unif){.pf-ref}, $\abs{P_n(z)}\ge\abs{e^z}-\abs{P_n(z)-e^z}>e^{-R}-e^{-R}/2>0$.
:::

:::

:::

:::
