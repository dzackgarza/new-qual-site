---
schema: qual/card@1
id: E-HK-SHA8
kind: problem
title: $AB$ not invertible when $n < m$
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
  note: Checked against Hoffman--Kunze Exercise 1.6.10.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise and no printed copy of
    Hoffman and Kunze is retained, so the card cites it by section and number, read from the
    collection index because the card id is coded: it is §1.6 Exercise 10. Each step re-read: the
    columns of AB are A applied to the columns of B and so lie in the column space of A; the rank
    of an m x n matrix is at most n; and an invertible m x m matrix has rank m. The card now notes
    explicitly that BA is not covered, since it is n x n and may be invertible. Not claimed: any
    statement about BA or about the case n >= m.
---

::: {.exercise}
Prove the following generalization of Exercise 6. If $A$ is an $m \times n$ matrix, $B$ is an $n \times m$ matrix and $n < m$, then $AB$ is not invertible.
:::


::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and no printed copy of Hoffman and Kunze is retained in `tmp/sources`, so the exercise is cited by section and number, read from the collection index because the card id is coded: it is §1.6 Exercise 10.

::: pf

::: {.pf-step #columns}
Every column of $AB$ is $A$ times the corresponding column of $B$, hence lies in the column space of $A$.

::: pf-proof
The $j$th column of $AB$ is $A$ applied to the $j$th column of $B$, by the definition of matrix multiplication; the column space of $A$ consists of all vectors $Av$.
:::

:::

::: {.pf-step #rank}
$\operatorname{rank}(AB)\le\operatorname{rank}(A)\le n$.

::: pf-proof
The column space of $AB$ is contained in that of $A$ by step [](#columns){.pf-ref}, and the rank is the dimension of the column space, so the first inequality holds. The matrix $A$ has $n$ columns, so its rank is at most $n$.
:::

:::

::: {.pf-step #notinvertible}
$AB$ is not invertible.

::: pf-proof
$AB$ is an $m\times m$ matrix of rank at most $n<m$, whereas an invertible $m\times m$ matrix has rank $m$, its columns forming a basis. So the rank is too small:
$$
\boxed{n<m\implies AB\text{ is not invertible}.}
$$
Nothing is assumed about $BA$, which is an $n\times n$ matrix and may well be invertible; the asymmetry is the point of the exercise.
:::

:::

:::
:::
