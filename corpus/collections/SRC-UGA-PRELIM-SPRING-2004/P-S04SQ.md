---
schema: qual/card@1
id: P-S04SQ
kind: problem
title: The sequence $x_{n+1}=\frac14 x_n^2+1$ with $x_1=1$ is increasing and bounded
  by $2$
classification:
  areas:
  - prelim
  topics:
  - Sequences of Numbers
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Define a sequence $(x_n)$ by $x_1 = 1$ and $x_{n+1} = \frac{1}{4}x_n^2 + 1$ for $n \in \mathbb{N}$.

a) Give an inductive proof that $x_n \leq 2$ for all $n \in \mathbb{N}$.

b) Prove that $x_{n+1} \geq x_n$ for each $n \in \mathbb{N}$.
[Hint: Consider $x_{n+1} - x_n$.]
:::

::: {.solution}
<1>1. For every $n\ge1$,
\[
1\le x_n\le2.
\]
::: {.proof}
We prove this by induction. For $n=1$, $x_1=1$, so the claim holds. Assume $1\le x_n\le2$. Then
\[
x_{n+1}=1+\frac{x_n^2}{4}\ge1,
\]
and, since $0\le x_n\le2$,
\[
x_{n+1}=1+\frac{x_n^2}{4}\le1+\frac{4}{4}=2.
\]
Thus $1\le x_{n+1}\le2$, completing the induction. In particular, $x_n\le2$ for all $n$.
:::

<1>2. For every $n\ge1$,
\[
x_{n+1}-x_n=\frac{(x_n-2)^2}{4}.
\]
::: {.proof}
Using the recurrence,
\[
x_{n+1}-x_n
=1+\frac{x_n^2}{4}-x_n
=\frac{x_n^2-4x_n+4}{4}
=\frac{(x_n-2)^2}{4}.
\]
:::

<1>3. Hence $x_{n+1}\ge x_n$ for every $n\ge1$.
::: {.proof}
The square in <1>2 is nonnegative.
:::
:::
