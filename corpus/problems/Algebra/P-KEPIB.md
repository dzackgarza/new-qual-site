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
- Show that every finite field extension is algebraic.
:::

::: {.solution}
Assume $[L:K]=n<\infty$ and let $\alpha\in L$. The $n+1$ vectors
\[
1,\alpha,\alpha^2,\dots,\alpha^n
\]
lie in the $n$-dimensional $K$-vector space $L$, so they are linearly dependent. Hence there exist $c_0,\dots,c_n\in K$, not all zero, such that
\[
c_0+c_1\alpha+\cdots+c_n\alpha^n=0.
\]
Thus $\alpha$ is a root of the nonzero polynomial
\[
c_0+c_1x+\cdots+c_nx^n\in K[x].
\]
Since $\alpha$ was arbitrary, every element of $L$ is algebraic over $K$. Therefore every finite field extension is algebraic.
:::
