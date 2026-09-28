---
schema: qual/card@1
id: P-UGAP08S-06
kind: problem
title: Zeros of every derivative from zeros at all integers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops x after “integer” and mangles the reference to the nth derivative; the surrounding Rolle-theorem statement uniquely determines the restored notation.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ have derivatives of all orders, and suppose
\[
f(x)=0
\]
for every integer $x$. Prove that for each $n\in\mathbb N$, the $n$th derivative $f^{(n)}$ has at least one root.
:::
