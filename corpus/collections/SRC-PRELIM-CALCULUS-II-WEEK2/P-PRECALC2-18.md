---
schema: qual/card@1
id: P-PRECALC2-18
kind: problem
title: Convergence and divergence of infinite products
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 18 on page 6 of Week2_solns.pdf and added an erratum remark that the first two factors of product (c) are undefined or negative.
---

::: {.problem}
Let $(a_n)$ be a sequence of positive numbers.
The infinite product
\[
\prod_{n=1}^{\infty}a_n=a_1a_2a_3\cdots
\]
is said to converge if there is $L\in(0,\infty)$ such that
\[
\lim_{N\to\infty}\prod_{n=1}^{N}a_n=L.
\]
Otherwise the product is said to diverge to zero or diverge to $+\infty$ if the limit is zero or $+\infty$, respectively.
Consider the infinite products
\[
\text{(a) }\prod_{n=1}^{\infty}\left(1+\frac1{n^2}\right),\qquad
\text{(b) }\prod_{n=1}^{\infty}\left(1+\frac1n\right),\qquad
\text{(c) }\prod_{n=1}^{\infty}\left(1-\frac1{\log n}\right).
\]
Show that (a) converges, (b) diverges to $+\infty$, and (c) diverges to $0$.
:::

::: {.remark}
Erratum: product (c) does not satisfy the source's standing hypothesis that the factors are positive. At $n = 1$ the factor $1 - \frac{1}{\log 1}$ is undefined, and at $n = 2$ it is $1 - \frac{1}{\log 2} \approx -0.44 < 0$. For $n \ge 3$ we have $\log n > 1$, so every factor lies in $(0,1)$; the intended claim is that $\prod_{n=3}^{\infty}\left(1 - \frac{1}{\log n}\right)$ diverges to $0$.
:::
