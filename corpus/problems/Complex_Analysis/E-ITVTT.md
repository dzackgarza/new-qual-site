---
schema: qual/card@1
id: E-ITVTT
kind: problem
title: The residue of $1/(z^n+1)$ at a root of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.exercise}
Find the residue at $\omega_n \coloneqq e^{\pi i \over n}$ of
$$
f(z) = {1\over z^n + 1}
.$$
:::

::: {.solution}

::: pf

::: {.pf-step #simple}
$\omega_n$ is a simple pole of $f$.

::: pf-proof
$\omega_n^n=e^{\pi i}=-1$, so $\omega_n$ is a zero of $q(z)\coloneqq z^n+1$, and $q'(\omega_n)=n\omega_n^{n-1}\neq0$.
:::

:::

::: pf-step
$\Res_{z=\omega_n}f(z)=\boxed{-{\omega_n\over n}}$.

::: pf-proof
By step [](#simple){.pf-ref}, the residue of $1/q$ at the simple zero $\omega_n$ is
$$
{1\over q'(\omega_n)}={1\over n\omega_n^{n-1}}={\omega_n\over n\omega_n^n}=-{\omega_n\over n}
.$$
:::

:::

:::

:::
