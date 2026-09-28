---
schema: qual/card@1
id: P-BERK80S-10
kind: problem
title: Hessian criteria for minima and uniqueness of critical points
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the malformed critical-point derivative notation from the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the positive-definite Taylor estimate and the strict-convexity argument along a line segment between critical points.
---

::: {.problem}
Let $f:\mathbb R^n\to\mathbb R$ be a function whose partial derivatives of order at most $2$ are everywhere defined and continuous.

1. Let $a\in\mathbb R^n$ be a critical point of $f$, i.e.
   \[
   \frac{\partial f}{\partial x_j}(a)=0,\qquad j=1,\ldots,n.
   \]
   Prove that $a$ is a local minimum provided the Hessian matrix
   \[
   \left(\frac{\partial^2f}{\partial x_i\partial x_j}\right)
   \]
   is positive definite at $x=a$.

2. Assume the Hessian matrix is positive definite at every $x\in\mathbb R^n$.
   Prove that $f$ has at most one critical point.
:::

::: {.solution}
Let $H_f(x)$ denote the Hessian matrix of $f$ at $x$.

<1>1. A critical point with positive-definite Hessian is a strict local minimum.
::: {.proof}
Because $H_f(a)$ is positive definite, there is a constant $c>0$ such that
\[
v^T H_f(a)v\ge 2c\|v\|^2
\qquad\text{for all }v\in\mathbb R^n.
\]
The Hessian depends continuously on $x$.
Hence, after shrinking to a neighborhood $U$ of $a$, we may arrange that
\[
v^T H_f(x)v\ge c\|v\|^2
\qquad\text{for all }x\in U,\ v\in\mathbb R^n.
\]

Let $h$ be small enough that the segment $a+th$, $0\le t\le1$, lies in $U$.
Define
\[
g(t)=f(a+th).
\]
Then
\[
g'(0)=\nabla f(a)\cdot h=0
\]
because $a$ is critical, while
\[
g''(t)=h^T H_f(a+th)h\ge c\|h\|^2.
\]
Taylor's formula with integral remainder gives
\[
\begin{aligned}
f(a+h)-f(a)
&=g(1)-g(0)\\
&=g'(0)+\int_0^1(1-t)g''(t)\,dt\\
&\ge c\|h\|^2\int_0^1(1-t)\,dt\\
&=\frac c2\|h\|^2.
\end{aligned}
\]
For $h\ne0$ this is strictly positive.
Thus $a$ is a strict local minimum.
:::

<1>2. If the Hessian is positive definite everywhere, there is at most one critical point.
::: {.proof}
Suppose, toward a contradiction, that $a\ne b$ are both critical points.
Put
\[
v=b-a\ne0
\]
and define
\[
g(t)=f(a+tv),\qquad 0\le t\le1.
\]
Then
\[
g'(t)=\nabla f(a+tv)\cdot v
\]
and
\[
g''(t)=v^T H_f(a+tv)v>0
\]
for every $t\in[0,1]$, because the Hessian is positive definite and $v\ne0$.
Therefore $g'$ is strictly increasing on $[0,1]$.
But criticality of $a$ and $b$ gives
\[
g'(0)=\nabla f(a)\cdot v=0,
\qquad
g'(1)=\nabla f(b)\cdot v=0,
\]
contradicting strict increase.
Hence $f$ has at most one critical point.
:::
:::
