---
schema: qual/card@1
id: P-BKF05-9A
kind: problem
title: Convolution preserves rapid decrease on the integers
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
A doubly infinite real sequence \((a_j)*{j\in\mathbb Z}\) is rapidly decreasing if, for every positive integer \(n\), the sequence \((j^na_j)*{j\in\mathbb Z}\) is bounded.
Let \((a_j)\) and \((b_j)\) be rapidly decreasing and define
\[
c_j=\sum_{k\in\mathbb Z}a_kb_{j-k}.
\]
Prove that the series defining every \(c_j\) converges and that \((c_j)\) is rapidly decreasing.
:::
