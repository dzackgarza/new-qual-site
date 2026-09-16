---
schema: qual/card@1
id: P-BERK92S-13
kind: problem
title: Jacobian determinant from infinitesimal volume distortion
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

::: {.problem}
Let $f:\mathbb R^3\to\mathbb R^3$ be one-to-one and $C^1$, and let $J$ be its Jacobian determinant. For $x_0\in\mathbb R^3$, let $Q_r(x_0)$ be the cube centered at $x_0$, of side length $r$, with edges parallel to the coordinate axes. Prove that
\[
|J(x_0)|
=\lim_{r\to0}r^{-3}\operatorname{vol}(f(Q_r(x_0)))
\le
\lim_{x\to x_0}
\frac{\|f(x)-f(x_0)\|^3}{\|x-x_0\|^3}.
\]
Here $\|\cdot\|$ is the Euclidean norm.
:::
