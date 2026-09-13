---
schema: qual/card@1
id: P-UCLAB15S-05
kind: problem
title: Convergence of the integral-sum discrepancy for a decreasing function
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
Let $f:[1,\infty)\to[0,\infty)$ be bounded and monotonically decreasing with $\lim_{x\to\infty}f(x)=0$. Show that
\[
\int_1^{N+1}f(x)\,dx-\sum_{n=1}^N f(n)
\]
converges to a finite limit as $N\to\infty$.
:::
