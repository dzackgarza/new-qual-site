---
schema: qual/card@1
id: E-HK-D0GP
kind: problem
title: Row interchange from other elementary operations
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze, Section 1.3, Exercise 7.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Prove that the interchange of two rows of a matrix can be accomplished by a finite sequence of elementary row operations of the other two types.
:::

::: solution
Suppose the two rows to be interchanged are $R_i$ and $R_j$.

<1>1. Replace $R_i$ by $R_i+R_j$.
::: proof
This is an elementary operation of the type “add a scalar multiple of one row
to another.” The pair becomes
\[
(R_i+R_j,\ R_j).
\]
:::

<1>2. Replace $R_j$ by $R_j-R_i$, where $R_i$ now denotes the new first row.
::: proof
The pair becomes
\[
(R_i+R_j,\ -R_i).
\]
:::

<1>3. Replace $R_i$ by $R_i+R_j$.
::: proof
The pair becomes
\[
(R_j,\ -R_i).
\]
:::

<1>4. Multiply $R_j$ by $-1$.
::: proof
This is an elementary row scaling, and the pair becomes
\[
(R_j,R_i).
\]
Thus the original rows have been interchanged using only the other two kinds of
elementary row operations.
:::
:::
