---
schema: qual/card@1
id: P-BKF85-6
kind: problem
title: Extreme eigenvalue bounds for a tridiagonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
Let $k\in\mathbb R$, let $n\ge2$, and let $A=(a_{ij})$ be the $n\times n$ matrix with
\[
a_{ii}=k,
\qquad
a_{i,i+1}=a_{i+1,i}=1,
\]
and all other entries equal to $0$.

Let $\lambda_{\min}$ and $\lambda_{\max}$ be the smallest and largest eigenvalues of $A$.
Show that
\[
\lambda_{\min}\le k-1
\qquad\text{and}\qquad
\lambda_{\max}\ge k+1.
\]
:::
