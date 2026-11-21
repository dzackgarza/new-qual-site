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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read as a second reader against the retained text; the statement matches Hoffman and Kunze
    Exercise 1.3.7, printed p. 11. The four operations were composed: (Ri,Rj) -> (Ri+Rj,Rj) ->
    (Ri+Rj,-Ri) -> (Rj,-Ri) -> (Rj,Ri), so the interchange is effected by two additions of a
    multiple of one row to another and one scaling by -1. Every scalar used is -1 or 1, so the
    argument is valid over any field, including characteristic 2, where -1 = 1. The solution now
    cites the retained text; no proof step changed.
---

::: {.exercise}
Prove that the interchange of two rows of a matrix can be accomplished by a finite sequence of elementary row operations of the other two types.
:::

::: {.solution}
No retained solution set covers this exercise; the book's text is retained as `assets/attachments/Hoffman-Kunze-Linear-Algebra.pdf` (Hoffman and Kunze, *Linear Algebra*, 2nd ed., 1971), where it is §1.3 Exercise 7. The argument is the card's own.

Suppose the two rows to be interchanged are $R_i$ and $R_j$.

::: pf

::: pf-step
Replace $R_i$ by $R_i+R_j$.

::: pf-proof
This is an elementary operation of the type “add a scalar multiple of one row
to another.” The pair becomes
$$
(R_i+R_j,\ R_j).
$$
:::

:::

::: pf-step
Replace $R_j$ by $R_j-R_i$, where $R_i$ now denotes the new first row.

::: pf-proof
The pair becomes
$$
(R_i+R_j,\ -R_i).
$$
:::

:::

::: pf-step
Replace $R_i$ by $R_i+R_j$.

::: pf-proof
The pair becomes
$$
(R_j,\ -R_i).
$$
:::

:::

::: pf-step
Multiply $R_j$ by $-1$.

::: pf-proof
This is an elementary row scaling, and the pair becomes
$$
(R_j,R_i).
$$
Thus the original rows have been interchanged using only the other two kinds of
elementary row operations.
:::

:::

:::

:::
