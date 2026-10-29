---
schema: qual/card@1
id: E-WE7UT
kind: problem
title: Singularities of $\frac{z^3+1}{z^2(z+1)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Residues
  - Poles
  - Removable Singularities
relations: []
review: draft
---

::: {.exercise}
Classify the singularities of
$$
f(z) = {z^3+1\over z^2(z+1)}.
$$

:::

::: {.hint}
A point $z_0$ is a pole of order $n$ of $f$ when $1/f = (z-z_0)^n h(z)$ with $h$ holomorphic and nonvanishing near $z_0$. Look for a common factor first.
:::

::: {.solution}
::: pf

::: {.pf-step #simplify}
$f(z) = \frac{z^2-z+1}{z^2} = 1 - \frac1z + \frac{1}{z^2}$ for $z\neq0,-1$.

::: pf-proof
$z^3+1 = (z+1)(z^2-z+1)$.
:::

:::

::: pf-step
$z=-1$ is a removable singularity, and $f$ extends there with value $3$.

::: pf-proof
By step [](#simplify){.pf-ref}, $f$ agrees near $-1$ with $1 - \frac1z + \frac1{z^2}$, which is holomorphic at $-1$ with value $1+1+1 = 3$.
:::

:::

::: pf-step
$z=0$ is a pole of order $2$ with $\Res_{z=0}f = -1$.

::: pf-proof
Step [](#simplify){.pf-ref} is the Laurent expansion of $f$ on $0<\abs{z}<1$: its principal part $\frac{1}{z^2} - \frac1z$ has lowest power $z^{-2}$, and the coefficient of $z^{-1}$ is $-1$.
:::

:::

:::

:::
