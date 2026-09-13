---
schema: qual/card@1
id: P-BKF07-8A
kind: problem
title: Construct sparse spikes with vanishing Cesaro mean
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
Suppose \((b_n)_{n\ge1}\) is a sequence of positive real numbers with
\[
b_n\to\infty,
\qquad
\frac{b_n}{n}\to0.
\]
Must there exist a sequence \((a_n)_{n\ge1}\) such that
\[
\frac{a_1+\cdots+a_n}{n}\to0
\]
and
\[
\limsup_{n\to\infty}\frac{a_n}{b_n}=\infty?
\]
Give a proof or counterexample.
:::
