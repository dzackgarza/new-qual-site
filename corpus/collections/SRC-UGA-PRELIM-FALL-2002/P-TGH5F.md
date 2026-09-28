---
schema: qual/card@1
id: P-TGH5F
kind: problem
title: A finite spanning set in $\RR^n$ contains a basis of its span
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $v_1, \dots, v_k$ be vectors in $\mathbb{R}^n$.
Define the span $V = \langle v_1, \dots, v_k \rangle$ of the vectors.
Prove that there is a subset of the vectors $v_1, \dots, v_k$ that forms a basis for $V$.
:::

::: {.solution}
The span of $v_1,\ldots,v_k$ is
\[
V=\langle v_1,\ldots,v_k\rangle
=\left\{\sum_{i=1}^k a_i v_i:a_i\in\mathbb R\right\}.
\]

Among all linearly independent subsets of the finite set $\{v_1,\ldots,v_k\}$, choose one of maximal cardinality, say
\[
\{v_{i_1},\ldots,v_{i_r}\}.
\]
It is linearly independent by construction. We claim that it spans $V$. If some $v_j$ were not in its span, then
\[
\{v_{i_1},\ldots,v_{i_r},v_j\}
\]
would still be linearly independent, contradicting maximality. Thus every $v_j$ lies in
\[
\operatorname{span}(v_{i_1},\ldots,v_{i_r}),
\]
so this span equals $V$. Hence the chosen subset is a basis of $V$.
:::
