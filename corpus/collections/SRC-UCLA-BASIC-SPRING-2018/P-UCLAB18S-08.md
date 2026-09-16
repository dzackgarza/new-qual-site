---
schema: qual/card@1
id: P-UCLAB18S-08
kind: problem
title: Asymptotics of the sine iteration
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Define $x_1=1$ and $x_{n+1}=\sin x_n$.
Prove that
\[
\lim_{n\to\infty}\sqrt n\,x_n
\]
exists and compute its value.

Hint: show that $x_{n+1}^{-2}-x_n^{-2}$ converges to a constant.
:::
