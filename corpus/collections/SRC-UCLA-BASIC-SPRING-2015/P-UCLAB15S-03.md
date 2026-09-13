---
schema: qual/card@1
id: P-UCLAB15S-03
kind: problem
title: A Lipschitz function with vanishing forward difference quotients
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be Lipschitz. Suppose that for every $x\in\mathbb R$,
\[
\lim_{n\to\infty}n\left[f\left(x+\frac1n\right)-f(x)\right]=0.
\]
Prove that $f$ is differentiable.
:::
