---
schema: qual/card@1
id: P-UCLAB12W-09
kind: problem
title: Matrix recurrence and exponential growth rate
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let
\[
a_1=1,\qquad a_2=4,\qquad a_{n+2}=4a_{n+1}-3a_n\quad(n\ge1).
\]
Find a $2\times2$ matrix $A$ such that
\[
A^n\binom10=\binom{a_{n+1}}{a_n}
\]
for all $n\ge1$. Compute the eigenvalues of $A$ and use them to determine
\[
\lim_{n\to\infty}a_n^{1/n}.
\]
:::
