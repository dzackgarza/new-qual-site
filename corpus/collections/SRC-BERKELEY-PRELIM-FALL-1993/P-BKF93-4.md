---
schema: qual/card@1
id: P-BKF93-4
kind: problem
title: A rectangular-matrix sandwich map cannot be invertible when the dimensions differ
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $F$ be a field. Fix positive integers $m,n$ and matrices $A,B\in M_{m\times n}(F)$. Define
\[
T:M_{n\times m}(F)\to M_{m\times n}(F),
\qquad
T(X)=AXB.
\]
Prove that if $m\ne n$, then $T$ is not invertible.
:::
