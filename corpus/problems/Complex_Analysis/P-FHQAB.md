---
schema: qual/card@1
id: P-FHQAB
kind: problem
title: A holomorphic function on $\DD\setminus\{0\}$ with $|f(z)|\le\log(1/|z|)$ is
  identically zero
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Maximum Modulus Principle
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic on $\DD\smz$ and $\abs{f(z)} \leq \log\qty{1\over \abs{z}}$, then $f\equiv 0$.
:::

::: {.solution}
::: pf

::: {.pf-step #removable}
$f$ extends to a holomorphic function $F$ on $\DD$.

::: pf-proof
For $0<\abs z<1$ we have $\abs{z f(z)} \leq \abs z \log\qty{1\over\abs z}$, which tends to $0$ as $z\to 0$.
Hence $zf(z)\to 0$, and by Riemann's removable singularity theorem $0$ is a removable singularity of $f$.
:::

:::

::: {.pf-step #small-circles}
For $0<r<1$, $\max_{\abs z\leq r}\abs{F(z)} \leq \log\qty{1\over r}$.

::: pf-proof
By the maximum modulus principle, the maximum of $\abs F$ on the closed disk $\abs z\leq r$ is attained on the circle $\abs z = r$, where $\abs{F(z)} = \abs{f(z)} \leq \log(1/r)$.
:::

:::

::: pf-step
$f\equiv 0$.

::: pf-proof
Fix $z\in\DD$. For every $r$ with $\abs z\leq r<1$, step [](#small-circles){.pf-ref} gives $\abs{F(z)}\leq\log(1/r)$.
Letting $r\to 1$ gives $F(z)=0$. Hence $F\equiv 0$ on $\DD$, and $f = F$ on $\DD\smz$ by step [](#removable){.pf-ref}.
:::

:::

:::

:::
