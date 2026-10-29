---
schema: qual/card@1
id: E-4TDW7
kind: problem
title: $K(a)=K(a^{2})$ when $a$ is algebraic of odd degree over $K$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $F/K$ be a field extension, and let $a \in F$ be algebraic over $K$ of odd degree $[K(a) : K] = 2m + 1$.
Prove that $a^2$ is algebraic over $K$, that $[K(a^2) : K]$ is odd, and that $K(a) = K(a^2)$.
:::

::: {.solution}

::: pf

::: {.pf-step #tower}
$a^2$ is algebraic over $K$, and $[K(a):K]=[K(a):K(a^2)]\,[K(a^2):K]$.

::: pf-proof
$a^2\in K(a)$, and $K(a)/K$ is finite, so $a^2$ is algebraic over $K$ and $K\subseteq K(a^2)\subseteq K(a)$. The tower law gives the product formula.
:::

:::

::: {.pf-step #top-degree}
$K(a)=K(a^2)$.

::: pf-proof
$a$ is a root of $x^2-a^2\in K(a^2)[x]$, so $[K(a):K(a^2)]\le2$. By step [](#tower){.pf-ref}, this degree divides the odd integer $2m+1$, so it is $1$.
:::

:::

::: pf-step
$[K(a^2):K]=2m+1$ is odd.

::: pf-proof
This follows from step [](#top-degree){.pf-ref}: $[K(a^2):K]=[K(a):K]$.
:::

:::

:::

:::
