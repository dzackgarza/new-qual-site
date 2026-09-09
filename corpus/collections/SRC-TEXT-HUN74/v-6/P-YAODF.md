---
schema: qual/card@1
id: P-YAODF
kind: problem
title: Division by integers prime to the characteristic stays in the base field
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction of the Hungerford exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $F/K$ be a field extension.
Let $\mathrm{char} K = p \neq 0$ and let $n\geq 1$ be an integer such that $(p, n) = 1$.
If $v\in F$ and $nv \in K$, then $v\in K$.
:::

::: solution
<1>1. The element $n\cdot1_K$ is nonzero in $K$.
::: proof
Since $\operatorname{char}K=p$, one has
\[
n\cdot1_K=0
\quad\Longleftrightarrow\quad
p\mid n.
\]
The hypothesis $(p,n)=1$ excludes this, so $n\cdot1_K\ne0$.
:::

<1>2. The element $n\cdot1_K$ is invertible in $K$.
::: proof
Every nonzero element of a field is invertible. Apply this to <1>1.
:::

<1>3. If $nv\in K$, then $v\in K$.
::: proof
Interpreting multiplication by the integer $n$ as scalar multiplication by
$n\cdot1_K$, we have
\[
nv=(n\cdot1_K)v.
\]
By hypothesis the left side belongs to $K$, and by <1>2 the inverse
$(n\cdot1_K)^{-1}$ belongs to $K$. Therefore
\[
v=(n\cdot1_K)^{-1}(nv)\in K.
\]
:::
:::
