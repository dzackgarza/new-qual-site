---
schema: qual/card@1
id: P-BERK87S-05
kind: problem
title: Periodization of a decaying continuous function and integration against periodic functions
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
Let $f:\mathbb R\to\mathbb R$ be continuous and satisfy
\[
|f(x)|\le\frac{C}{1+x^2}
\]
for some $C>0$. Define
\[
F(x)=\sum_{n=-\infty}^{\infty}f(x+n).
\]

1. Prove that $F$ is continuous and $1$-periodic.
2. If $G$ is continuous and $1$-periodic, prove that
   \[
   \int_0^1F(x)G(x)\,dx
   =\int_{-\infty}^{\infty}f(x)G(x)\,dx.
   \]
:::
