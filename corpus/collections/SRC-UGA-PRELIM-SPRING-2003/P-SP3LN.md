---
schema: qual/card@1
id: P-SP3LN
kind: problem
title: $x > \ln x$ for all $x > 0$
classification:
  areas:
  - prelim
  topics:
  - Inequalities
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Prove that $x > \ln x$ for all $x > 0$.
:::

::: {.solution}

::: pf

::: pf-step
Define $f:(0,\infty)\to\mathbb R$ by
\[
f(x)=x-\ln x.
\]
:::

::: {.pf-step #s2}
The function $f$ has a global minimum at $x=1$.

::: pf-proof
We have
\[
f'(x)=1-\frac1x=\frac{x-1}{x}.
\]
Thus $f'(x)<0$ for $0<x<1$, $f'(1)=0$, and $f'(x)>0$ for $x>1$. Hence $f$ decreases on $(0,1]$ and increases on $[1,\infty)$, so its global minimum occurs at $1$.
:::

:::

::: pf-step
Therefore $f(x)\ge f(1)=1>0$ for every $x>0$.

::: pf-proof
This follows from step [](#s2){.pf-ref} and $\ln 1=0$.
:::

:::

::: pf-step
Hence $x>\ln x$ for every $x>0$.

::: pf-proof
The inequality $f(x)>0$ is exactly $x-\ln x>0$.
:::

:::

:::
:::
