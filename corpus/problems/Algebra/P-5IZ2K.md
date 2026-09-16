---
schema: qual/card@1
id: P-5IZ2K
kind: problem
title: A non-symmetric polynomial whose square is symmetric
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
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
Find a non-symmetric polynomial in several variables whose square is symmetric, and prove its properties.
:::

::: {.solution}
Over any field of characteristic different from $2$, take
\[
P(x,y)=x-y.
\]
It is not symmetric because
\[
P(y,x)=y-x=-P(x,y)\ne P(x,y).
\]
But
\[
P(x,y)^2=(x-y)^2
\]
is symmetric, since interchanging $x$ and $y$ leaves it unchanged.

More generally, the Vandermonde polynomial
\[
\Delta(x_1,\ldots,x_n)=\prod_{i<j}(x_i-x_j)
\]
is alternating:
\[
\Delta(x_{\sigma(1)},\ldots,x_{\sigma(n)})
=\operatorname{sgn}(\sigma)\Delta(x_1,\ldots,x_n).
\]
Hence $\Delta$ is nonsymmetric when the characteristic is not $2$, while
\[
\Delta^2=\prod_{i<j}(x_i-x_j)^2
\]
is invariant under every permutation of the variables and therefore symmetric.
:::
