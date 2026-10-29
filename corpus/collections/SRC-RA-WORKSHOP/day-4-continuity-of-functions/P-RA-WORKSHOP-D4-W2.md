---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W2
kind: problem
title: A continuous self-map of an interval has a fixed point
classification:
  areas:
  - real-analysis
  topics:
  - Fixed Points
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
If $f:[0,1]\to[0,1]$ is continuous, show that $f(x)=x$ for some $x\in[0,1]$.
:::

::: {.solution}
Set $g:[0,1]\to\RR$ by $g(t)=f(t)-t$.

::: pf

::: {.pf-step #s1}

The function $g$ is continuous and satisfies $g(0)\geq0\geq g(1)$.

::: pf-proof

The difference of the continuous functions $f$ and $t\mapsto t$ is continuous. Since $f$ maps into $[0,1]$, one has $g(0)=f(0)\geq0$ and $g(1)=f(1)-1\leq0$.

:::

:::

::: pf-step

There exists $x\in[0,1]$ such that $f(x)=x$.

::: pf-proof

By step [](#s1){.pf-ref}, zero lies between the endpoint values $g(0)$ and $g(1)$. The intermediate value theorem gives $x\in[0,1]$ with $g(x)=0$. By definition of $g$, this is equivalent to $f(x)=x$.

:::

:::

:::

:::
