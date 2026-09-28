---
schema: qual/card@1
id: P-UCLAB17F-09
kind: problem
title: A fixed point from summable iterate Lipschitz constants
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $(X,\rho)$ be complete and $f:X\to X$. For $n\ge1$ set
\[
c_n=\sup_{x\ne y}\frac{\rho(f^n(x),f^n(y))}{\rho(x,y)}.
\]
If $\sum_{n=1}^\infty c_n<\infty$, prove that $f$ has a unique fixed point.
:::
