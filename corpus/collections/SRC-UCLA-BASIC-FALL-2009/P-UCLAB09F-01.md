---
schema: qual/card@1
id: P-UCLAB09F-01
kind: problem
title: Pointwise subsequences and iterated limits
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
<1>1. For each $n\in\mathbb N$, let $f_n\colon\mathbb N\to\mathbb R$ satisfy $|f_n(m)|\le 1$ for all $m,n\in\mathbb N$.
Prove that there is an infinite subsequence of distinct positive integers $(n_i)$ such that, for each $m\in\mathbb N$, the sequence $f_{n_i}(m)$ converges.

<1>2. For $(n_i)$ as in <1>1, assume in addition that
\[
\lim_{m\to\infty}\lim_{i\to\infty} f_{n_i}(m)=0.
\]
Prove or disprove that the reverse iterated limit
\[
\lim_{i\to\infty}\lim_{m\to\infty} f_{n_i}(m)
\]
also exists and equals $0$.
:::
