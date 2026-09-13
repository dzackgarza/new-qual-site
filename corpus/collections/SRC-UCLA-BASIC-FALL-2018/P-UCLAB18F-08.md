---
schema: qual/card@1
id: P-UCLAB18F-08
kind: problem
title: Resolvent row norm identity for a symmetric matrix
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $X$ be a real symmetric $n\times n$ matrix and let $z\in\mathbb C$ with $\operatorname{Im}z>0$. Put
\[
G=(X-zI)^{-1}.
\]
Show that for each $i$,
\[
\sum_{j=1}^n|G_{ij}|^2=\frac{\operatorname{Im}G_{ii}}{\operatorname{Im}z}.
\]
:::
