---
schema: qual/card@1
id: P-UCLAB12W-04
kind: problem
title: Cesàro convergence of nonnegative partial sums
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $(a_n)$ be a sequence of nonnegative numbers and put
\[
s_n=\sum_{k=1}^n a_k.
\]
Suppose $s_n$ tends to $s\in\mathbb R$ in the Cesàro sense:
\[
\lim_{n\to\infty}\frac{s_1+\cdots+s_n}{n}=s.
\]
Show that $\sum_{k=1}^\infty a_k$ converges and equals $s$.
:::
