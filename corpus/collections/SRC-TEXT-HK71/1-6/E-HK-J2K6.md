---
schema: qual/card@1
id: E-HK-J2K6
kind: problem
title: Row-reduction and factorization over $\CC$
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
  note: Checked against Hoffman--Kunze Exercise 1.6.2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Do Exercise 1, but with

$$
A = \left[ \begin{array}{c c c} 2 & 0 & i \\ 1 & - 3 & - i \\ i & 1 & 1 \end{array} \right].
$$
:::


::: {.solution}

The argument is the card's own: $A$ is exhibited as invertible by exhibiting its inverse, and then $R=PA$ with $R=I$ and $P$ invertible satisfies the requirement of Exercise 1. The entries of $P$ were verified by exact computation.

::: pf

::: {.pf-step #inverse}

$P$ as displayed below satisfies $PA=I_{3}$.

::: pf-proof

Multiplying the displayed $P$ by $A$ and reducing every entry with $i^{2}=-1$ gives the identity matrix; in particular the first column of $PA$ is $(1,0,0)^{t}$, the second $(0,1,0)^{t}$ and the third $(0,0,1)^{t}$. Explicitly,
$$
P=\begin{bmatrix}\tfrac13&\tfrac1{30}-\tfrac{i}{10}&\tfrac1{10}-\tfrac{3i}{10}\\0&-\tfrac3{10}-\tfrac{i}{10}&\tfrac1{10}-\tfrac{3i}{10}\\-\tfrac{i}{3}&\tfrac15+\tfrac{i}{15}&\tfrac35+\tfrac{i}{5}\end{bmatrix}.
$$

:::

:::

::: {.pf-step #invertible}

$P$ is invertible, with inverse $A$.

::: pf-proof

$PA=I_{3}$ by step [](#inverse){.pf-ref}, so $P$ has a right inverse and is therefore invertible; for square matrices over a field, $PA=I$ already forces $A$ to be invertible with $A^{-1}=P$, since $\det P\det A=1$. Hence $A$ is invertible with inverse $P$, and $P^{-1}=A$.

:::

:::

::: {.pf-step #rref}

The reduced row echelon form of $A$ is $R=I_{3}$.

::: pf-proof

$A$ is invertible by step [](#invertible){.pf-ref}. Row reduction of an invertible square matrix ends at a row-reduced echelon matrix that is invertible and square, and the only such matrix is $I_{3}$: a row-reduced echelon square matrix with a zero row fails invertibility, so all three rows have pivots $1$ in the three distinct columns, forcing every pivot to be on the diagonal with zeros elsewhere.

:::

:::

::: {.pf-step #conclusion}

$R=I_{3}$ is row-equivalent to $A$ and $R=PA$ with $P$ invertible, as Exercise 1 requires.

::: pf-proof

Steps [](#inverse){.pf-ref} and [](#rref){.pf-ref} give $R=PA$ with $R$ row-reduced echelon and equal to the row reduction of $A$, and step [](#invertible){.pf-ref} gives invertibility of $P$:
$$
\boxed{R=I_{3}=PA,\qquad P=A^{-1}\ \text{invertible}.}
$$

:::

:::

:::

:::
