---
schema: qual/card@1
id: P-F10IL
kind: problem
title: Independent images under a linear map imply independent preimages
classification:
  areas:
  - prelim
  topics:
  - Linear Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $V$ and $W$ are vector spaces and $T: V \to W$ is a linear transformation.
Suppose $v_1, \dots, v_k \in V$.
Prove that if $T(v_1), \dots, T(v_k)$ form a linearly independent set in $W$, then $v_1, \dots, v_k$ form a linearly independent set in $V$.
:::

::: {.solution}
Suppose
\[
a_1v_1+\cdots+a_kv_k=0.
\]
Applying $T$ and using linearity gives
\[
a_1T(v_1)+\cdots+a_kT(v_k)=0.
\]
Because $T(v_1),\ldots,T(v_k)$ are linearly independent, all $a_i=0$. Hence $v_1,\ldots,v_k$ are linearly independent.
:::
