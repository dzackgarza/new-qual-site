---
schema: qual/card@1
id: P-F05DM
kind: problem
title: 'De Morgan: complement of an intersection is the union of complements'
classification:
  areas:
  - prelim
  topics:
  - Set Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $Z$ be a set and let $X_1, X_2, \dots$ be subsets of $Z$.
Prove the formula $\bigl(\bigcap_i X_i\bigr)^c = \bigcup_i X_i^c$, where $(\cdot)^c$ denotes complement.
:::

::: solution
For any $z\in Z$,
\[
\begin{aligned}
z\in\left(\bigcap_iX_i\right)^c
&\Longleftrightarrow z\notin\bigcap_iX_i\\
&\Longleftrightarrow \text{there exists }i\text{ such that }z\notin X_i\\
&\Longleftrightarrow \text{there exists }i\text{ such that }z\in X_i^c\\
&\Longleftrightarrow z\in\bigcup_iX_i^c.
\end{aligned}
\]
Since the two sets have exactly the same elements,
\[
\left(\bigcap_iX_i\right)^c=\bigcup_iX_i^c.
\]
:::
