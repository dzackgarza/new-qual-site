---
schema: qual/card@1
id: P-4KPQM
kind: problem
title: The fundamental theorem of algebra via the maximum modulus principle
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Polynomials
  - Zeros
relations: []
review: draft
---

::: {.problem}
Prove the fundamental theorem of Algebra using the maximum modulus principle.
:::

::: {.solution}

Let $p$ be a nonconstant complex polynomial, and suppose $p$ has no zero, so that $g\coloneqq1/p$ is entire.

::: pf

::: {.pf-step #decay}
There is $R>0$ with $\abs{g(z)}<\abs{g(0)}$ for $\abs{z}\geq R$.

::: pf-proof
Since $p$ is nonconstant, $\abs{p(z)}\to\infty$ as $\abs{z}\to\infty$, so $g(z)\to0$, and $g(0)\neq0$.
:::

:::

::: {.pf-step #interior-max}
$\abs{g}$ attains its maximum over $\CC$ at a point of the open disc $\abs{z}<R$.

::: pf-proof
On the compact disc $\abs{z}\leq R$, $\abs{g}$ attains a maximum at some $z_0$, and $\abs{g(z_0)}\geq\abs{g(0)}$.
By step [](#decay){.pf-ref}, $\abs{g}<\abs{g(0)}$ on $\abs{z}\geq R$, so $\abs{z_0}<R$ and $\abs{g(z_0)}$ is the maximum of $\abs{g}$ on $\CC$.
:::

:::

::: pf-step
$p$ has a zero.

::: pf-proof
By step [](#interior-max){.pf-ref} and the maximum modulus principle, $g$ is constant, so $p$ is constant, a contradiction.
:::

:::

:::

:::
