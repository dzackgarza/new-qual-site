---
schema: qual/card@1
id: P-UGAP09F-05
kind: problem
title: Existing partial derivatives need not imply continuity, and a sufficient differentiability criterion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
(a) Let
\[
f(x,y)=
\begin{cases}
\dfrac{xy}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
Show that
\[
\frac{\partial f}{\partial x}(0,0)=
\frac{\partial f}{\partial y}(0,0)=0,
\]
but $f$ is not continuous at $(0,0)$.

(b) Give a sufficient condition, stated in terms of the partial derivatives, for a function $g:\mathbb R^2\to\mathbb R$ to be differentiable at a point $P$.
:::
