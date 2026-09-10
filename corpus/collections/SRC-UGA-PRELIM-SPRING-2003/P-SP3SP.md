---
schema: qual/card@1
id: P-SP3SP
kind: problem
title: Adjoining a vector already in a span does not change the span
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
(a) Define the span of vectors $v_1, \dots, v_k$ in $\mathbb{R}^n$.

(b) Prove that if $w$ lies in the span of $v_1, \dots, v_k$, then the span of $v_1, \dots, v_k, w$ is equal to the span of $v_1, \dots, v_k$.
:::

::: solution
<1>1. The span of $v_1,\dots,v_k$ is
\[
\operatorname{span}(v_1,\dots,v_k)
=\left\{\sum_{i=1}^k a_i v_i : a_1,\dots,a_k\in\mathbb R\right\}.
\]
:::

<1>2. Suppose $w\in\operatorname{span}(v_1,\dots,v_k)$. Then
\[
\operatorname{span}(v_1,\dots,v_k)
\subseteq
\operatorname{span}(v_1,\dots,v_k,w).
\]
::: {.proof}
Every linear combination of $v_1,\dots,v_k$ is also a linear combination of $v_1,\dots,v_k,w$, by taking the coefficient of $w$ to be $0$.
:::

<1>3. Conversely,
\[
\operatorname{span}(v_1,\dots,v_k,w)
\subseteq
\operatorname{span}(v_1,\dots,v_k).
\]
::: {.proof}
Because $w$ lies in the first span, there are $b_1,\dots,b_k\in\mathbb R$ such that
\[
w=\sum_{i=1}^k b_i v_i.
\]
Hence every element of the enlarged span has the form
\[
\sum_{i=1}^k a_i v_i+c w
=\sum_{i=1}^k (a_i+c b_i)v_i,
\]
which belongs to $\operatorname{span}(v_1,\dots,v_k)$.
:::

<1>4. Therefore
\[
\operatorname{span}(v_1,\dots,v_k,w)
=
\operatorname{span}(v_1,\dots,v_k).
\]
::: {.proof}
This follows from the two inclusions in <1>2 and <1>3.
:::
:::
