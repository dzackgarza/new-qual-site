---
schema: qual/card@1
id: P-BERK95S-11
kind: problem
title: Extend an isometry of a finite subset fixing the origin to a linear map
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
---

:::{.problem}
Let $S\subset\mathbb R^n$ be finite with $0\in S$. Suppose $\varphi:S\to S$ satisfies
\[
\varphi(0)=0
\]
and
\[
d(\varphi(s),\varphi(t))=d(s,t)
\]
for all $s,t\in S$, where $d$ is the Euclidean metric. Prove that there is a linear map
\[
F:\mathbb R^n\to\mathbb R^n
\]
whose restriction to $S$ is $\varphi$.
:::
