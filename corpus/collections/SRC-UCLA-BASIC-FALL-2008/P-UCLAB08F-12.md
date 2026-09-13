---
schema: qual/card@1
id: P-UCLAB08F-12
kind: problem
title: Nonuniqueness in least squares comes from the nullspace
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Consider
\[
\min_{\mathbf x\in\mathbb R^n}\|A\mathbf x-\mathbf b\|_2,
\qquad A\in\mathbb R^{m\times n},\quad m\ge n.
\]
Prove that if $\mathbf x$ and $\mathbf x+\alpha\mathbf z$ are both minimizers for some $\alpha\ne0$, then $\mathbf z\in\ker A$.
:::
