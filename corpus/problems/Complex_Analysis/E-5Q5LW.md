---
schema: qual/card@1
id: E-5Q5LW
kind: problem
title: Nonvanishing holomorphic functions of modulus one on the circle are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Schwarz Reflection
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is continuous and nonvanishing on $\bar \DD$, and holomorphic in $\DD$.
Prove that if $\abs{z} = 1 \implies \abs{f(z)} = 1$, then $f$ is constant.
:::

::: {.hint}
Extend $f$ to all of $\CC$ by $f(z) = 1/ \bar{f(1/\bar z)}$ for any $\abs{z} > 1$, and argue as in the Schwarz reflection principle.
:::

::: {.solution}
Define $F:\CC\to \CC$ by $F(z)=f(z)$ for $\abs z\le1$ and $F(z) = 1/\bar{f(1/\bar{z})}$ for $\abs z>1$; this is defined because $f$ is nonvanishing on $\bar\DD$.

::: pf

::: {.pf-step #outside}
$F$ is holomorphic on $\abs z>1$.

::: pf-proof
$F$ is the composite of the holomorphic map $w\mapsto 1/f(w)$ on $\DD$ with the two antiholomorphic maps $z\mapsto1/\bar z$ and $w\mapsto\bar w$.
:::

:::

::: {.pf-step #continuous}
$F$ is continuous on $\CC$.

::: pf-proof
For $\abs{z_0}=1$ we have $1/\bar{z_0}=z_0$ and $\abs{f(z_0)}=1$, so $1/\bar{f(z_0)}=f(z_0)$; by continuity of $f$ on $\bar\DD$ both formulas tend to $f(z_0)$ as $z\to z_0$.
:::

:::

::: {.pf-step #entire}
$F$ is entire.

::: pf-proof
By steps [](#outside){.pf-ref} and [](#continuous){.pf-ref}, $F$ is continuous on $\CC$ and holomorphic off the circle $S^1$.
As in the proof of the Schwarz reflection principle, Morera's theorem shows that such a function is entire.
:::

:::

::: {.pf-step #bounded}
$F$ is bounded.

::: pf-proof
With $M=\max_{\bar\DD}\abs f$ and $m=\min_{\bar\DD}\abs f>0$, we have $\abs F\le M$ on $\bar\DD$ and $\abs F\le 1/m$ outside it.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By steps [](#entire){.pf-ref} and [](#bounded){.pf-ref} and Liouville's theorem, $F$ is constant, and $f=F|_{\bar\DD}$.
:::

:::

:::

:::
