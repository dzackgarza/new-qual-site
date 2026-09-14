---
schema: qual/card@1
id: P-BKF88-3
kind: problem
title: Decay in a triangular system of linear differential equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let real-valued functions $f_1,\ldots,f_{n+1}$ on $\mathbb R$ satisfy
\[
f_{k+1}'+f_k'=(k+1)f_{k+1}-kf_k,
\qquad k=1,\ldots,n,
\]
and
\[
f_{n+1}'=-(n+1)f_{n+1}.
\]
Prove that for every $k$,
\[
\lim_{t\to\infty}f_k(t)=0.
\]
:::
