---
schema: qual/card@1
id: P-BERK81S-10
kind: problem
title: Shift eigenvectors, Fibonacci recurrence, and Binet's formula
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $S$ be the vector space of complex sequences and define the left-shift operator
\[
T(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots).
\]

1. Describe the eigenvectors of $T$.

2. Consider the recurrence
   \[
   x_{n+2}=x_{n+1}+x_n.
   \]
   Show that its solutions form a two-dimensional subspace $E\subset S$ with $T(E)\subset E$, and find an explicit basis for $E$.

3. The Fibonacci numbers satisfy $f_1=f_2=1$ and $f_{n+2}=f_{n+1}+f_n$.
   Find an explicit formula for $f_n$.
:::
