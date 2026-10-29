---
schema: qual/card@1
id: E-NT2T3
kind: problem
title: Singularities of $\frac{1}{e^z - 1}$
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Residues
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Classify the singularities and compute the residues at any poles of the following function:
$$
f(z) \coloneqq \frac{1}{e^z - 1}.
$$
:::

::: {.solution}

For $k\in\ZZ$ let $z_k \coloneqq 2\pi i k$.

::: pf

::: {.pf-step #zeros}
The singularities of $f$ are exactly the points $z_k$, $k\in\ZZ$, and each is isolated.

::: pf-proof
$f$ is holomorphic wherever $e^z\neq 1$, and $e^z=1$ if and only if $z\in 2\pi i\ZZ$, a discrete set.
:::

:::

::: pf-step
Each $z_k$ is a simple pole of $f$ with $\Res_{z=z_k} f = \boxed{1}$.

::: pf-proof
The derivative of $e^z-1$ at $z_k$ is $e^{z_k}=1\neq 0$, so $e^z-1$ has a simple zero at $z_k$ and $f$ has a simple pole there.
By L'Hôpital's rule,
$$
\Res_{z=z_k} f = \lim_{z\to z_k}\frac{z-z_k}{e^z-1} = \lim_{z\to z_k}\frac{1}{e^z} = e^{-z_k} = 1.
$$
:::

:::

:::

:::
