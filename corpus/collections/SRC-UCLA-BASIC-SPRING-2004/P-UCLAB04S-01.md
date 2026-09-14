---
schema: qual/card@1
id: P-UCLAB04S-01
kind: problem
title: Injecting binary sequences into the real line by decimal expansion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Let $S$ be the set of sequences
\[
a=(a_1,a_2,\ldots),
\qquad a_k\in\{0,1\}.
\]
Show that the map $\theta:S\to\mathbb R$ defined by
\[
\theta(a)=\frac{a_1}{10}+\frac{a_2}{10^2}+\cdots
\]
is injective.
Include an explanation of why the infinite series converges.

Hint: if $a\ne b$, you may suppose their first differing coordinate is $n$ and write
\[
a=(a_1,\ldots,a_{n-1},0,a_{n+1},\ldots),
\qquad
b=(a_1,\ldots,a_{n-1},1,b_{n+1},\ldots).
\]
:::
