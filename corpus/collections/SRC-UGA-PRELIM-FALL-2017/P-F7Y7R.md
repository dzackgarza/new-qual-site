---
schema: qual/card@1
id: P-F7Y7R
kind: problem
title: Negation of two quantified statements
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: dzackgarza
  date: 2026-08-27
  note: written with the restored problem statement, replacing an imported one
---

::: problem
Negate the following statements without using the word “not.”

1. For every real number $x$, there is a real number $y$ such that $|x-y|\geq2017$.

2. The function $f:\mathbb R\to\mathbb R$ is continuous.
:::

::: solution
The first negation is:
\[
\text{There is an }x\in\mathbb R\text{ such that }|x-y|<2017
\text{ for every }y\in\mathbb R.
\]

Using the pointwise definition of continuity on $\mathbb R$, the second negation is:
\[
\exists x\in\mathbb R\ \exists\varepsilon>0\ \forall\delta>0\ \exists y\in\mathbb R:
|x-y|<\delta\ \text{ and }\ |f(x)-f(y)|\geq\varepsilon.
\]
:::
