---
schema: qual/card@1
id: E-HYPCI
kind: problem
title: Star-convex sets are simply connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

A subset $A$ of $\mathbb{R}^n$ is said to be star convex if for some point $a_0$ of $A$, all the line segments joining $a_0$ to other points of $A$ lie in $A$.

(a) Find a star convex set that is not convex.

(b) Show that if $A$ is star convex, $A$ is simply connected.
:::

::: {.solution}
(a) For example,
\[
A=\{(x,y)\in\mathbb R^2:0\le x\le1,\ |y|\le x\}\cup\{(x,0):1\le x\le2\}
\]
is star convex with respect to \((0,0)\): every radial segment from the origin to a point of \(A\) stays in \(A\). It is not convex, since \((1,1),(2,0)\in A\) but their midpoint \((3/2,1/2)\notin A\).

(b) Let \(a_0\) be a star center. Define
\[
H:A\times I\to A,\qquad H(x,t)=(1-t)x+t a_0.
\]
By star convexity the whole segment from \(x\) to \(a_0\) lies in \(A\), so \(H\) is well defined and continuous. Moreover
\[
H(x,0)=x,\qquad H(x,1)=a_0.
\]
Thus \(A\) is contractible. A contractible space is path connected, and every loop \(f:I\to A\) contracts by
\[
F(s,t)=H(f(s),t).
\]
Hence \(\pi_1(A,a_0)=0\), so \(A\) is simply connected.
:::
