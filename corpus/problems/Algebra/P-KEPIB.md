---
schema: qual/card@1
id: P-KEPIB
kind: problem
title: Finite field extensions are algebraic
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that every finite field extension is algebraic.
:::

::: {.solution}

::: pf

::: pf-step

If $[L:K]=n<\infty$, then every $\alpha\in L$ is algebraic over $K$.

::: pf-proof

The $n+1$ elements $1,\alpha,\ldots,\alpha^n$ of the $n$-dimensional $K$-vector space $L$ are linearly dependent, so there are $c_0,\ldots,c_n\in K$, not all zero, with $c_0+c_1\alpha+\cdots+c_n\alpha^n=0$. Thus $\alpha$ is a root of the nonzero polynomial $c_0+c_1x+\cdots+c_nx^n\in K[x]$.

:::

:::

:::

:::
