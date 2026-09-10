---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW2
kind: problem
title: Radial deformation retraction $\mathbb R^n\setminus\{0\}\to S^{n-1}$ (warm-up)
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Construct an explicit deformation retraction from $\mathbb R^n\setminus\{0\}$ onto $S^{n-1}$.
:::

::: {.solution}
Define
\[
H:(\mathbb R^n\setminus\{0\})\times[0,1]\to\mathbb R^n\setminus\{0\}
\]
by
\[
H(x,t)=\left((1-t)+\frac{t}{\|x\|}\right)x.
\]
The scalar factor is positive for every \(x\ne0\) and \(0\le t\le1\), so \(H(x,t)\ne0\). Also
\[
H(x,0)=x,
\qquad
H(x,1)=\frac{x}{\|x\|}\in S^{n-1}.
\]
If \(x\in S^{n-1}\), then \(\|x\|=1\), hence
\[
H(x,t)=x
\]
for all \(t\). Thus \(H\) is a deformation retraction of \(\mathbb R^n\setminus\{0\}\) onto \(S^{n-1}\).
:::
