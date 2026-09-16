---
schema: qual/card@1
id: P-BERK95S-10
kind: problem
title: A decreasing sequence of nonnegative continuous functions has an attained limiting supremum
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f_n:[0,1]\to[0,\infty)$ be continuous and suppose
\[
f_1(x)\ge f_2(x)\ge f_3(x)\ge\cdots
\]
for every $x\in[0,1]$. Set
\[
f(x)=\lim_{n\to\infty}f_n(x),
\qquad
M=\sup_{0\le x\le1}f(x).
\]

1. Prove that there is $t\in[0,1]$ such that $f(t)=M$.
2. Give an example showing that part 1 can fail if the monotonicity is only eventual pointwise: for each $x$ there is $n_x$ such that $f_n(x)\ge f_{n+1}(x)$ for all $n\ge n_x$.
:::
