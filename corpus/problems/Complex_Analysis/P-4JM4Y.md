---
schema: qual/card@1
id: P-4JM4Y
kind: problem
title: Unique fixed points
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Compactness
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic on $\DD$ and continuous on $\bar\DD$ with $f(\bar \DD) \subseteq \DD$, then $f$ has a unique fixed point in $\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #radius}
There is $r<1$ with $\abs{f(z)}\leq r$ for all $z\in\bar\DD$.

::: pf-proof
$f(\bar\DD)$ is a compact subset of the open disc $\DD$, so $\abs{f}$ attains a maximum $r<1$ on $\bar\DD$.
:::

:::

::: {.pf-step #rouche}
For every $r'\in(r,1)$, $z-f(z)$ has exactly one zero, counted with multiplicity, in $\abs{z}<r'$.

::: pf-proof
On $\abs{z}=r'$, step [](#radius){.pf-ref} gives $\abs{f(z)}\leq r<r'=\abs{z}$.
By Rouché's theorem, $z-f(z)$ and $z$ have the same number of zeros in $\abs{z}<r'$, namely one.
:::

:::

::: pf-step
$f$ has exactly one fixed point in $\DD$.

::: pf-proof
Every fixed point $z\in\DD$ satisfies $\abs{z}=\abs{f(z)}\leq r$, so all fixed points in $\DD$ lie in $\abs{z}<r'$ for any $r'\in(r,1)$.
By step [](#rouche){.pf-ref}, there is exactly one.
:::

:::

:::

:::

::: {.remark}
The compactness of $\bar\DD$ is what gives the margin $r<1$; for a map that is only holomorphic on $\DD$ with $f(\DD)\subseteq\DD$, the conclusion can fail, as $f(z)=(z+1)/2$ shows.
:::
