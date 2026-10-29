---
schema: qual/card@1
id: P-HQXCX
kind: problem
title: Positive integers $n$ with $(1+i)^n=(1-i)^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Geometry
relations: []
review: draft
---

::: {.problem}
Characterize positive integers $n$ such that $(1+i)^{n}=(1-i)^{n}$
:::
::: {.solution}
::: pf

::: {.pf-step #ratio}
$\dfrac{1+i}{1-i}=i$.

::: pf-proof
$(1+i)^2 = 2i$ and $(1-i)(1+i)=2$, so $\frac{1+i}{1-i} = \frac{(1+i)^2}{2} = i$.
:::

:::

::: pf-step
$(1+i)^n=(1-i)^n$ exactly when $\boxed{4\mid n}$, that is, $n=4,8,12,\ldots$.

::: pf-proof
Since $1-i\neq 0$, the equation is equivalent to $\qty(\frac{1+i}{1-i})^n=1$, which by step [](#ratio){.pf-ref} is $i^n=1$. The powers of $i$ have period $4$, and $i^n=1$ exactly when $4\mid n$.
:::

:::

:::

:::
