---
schema: qual/card@1
id: P-OK5P3
kind: problem
title: Line integral of $y\,dx+2x\,dy$ along a quarter circle closed by the axes
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\gamma$ be the closed path which goes counterclockwise around the circle $C(0,2) = \{(x,y) \in \mathbb{R}^2 : x^2+y^2 = 2^2\}$ from the point $(2,0)$ to the point $(0,2)$, then goes to the origin along the y-axis, and then back to $(2,0)$ along the x-axis.

Compute $\int_\gamma 2x\,dy + y\,dx$ in one of two ways:

a) Directly, using the definition of a line integral; or

b) By using Green's theorem or the general Stokes' theorem.
:::


::: solution
<1>1. The path $\gamma$ is the positively oriented boundary of the quarter disk
\[
D=\{(x,y):x\ge0,\ y\ge0,\ x^2+y^2\le4\}.
\]
::: {.proof}
The circular arc runs counterclockwise from $(2,0)$ to $(0,2)$, then the path follows the positive $y$-axis down to the origin and the positive $x$-axis back to $(2,0)$. Thus the enclosed region lies to the left of the traversal.
:::

<1>2. Write the integrand as
\[
P\,dx+Q\,dy
\quad\text{with}\quad
P(x,y)=y,\qquad Q(x,y)=2x.
\]
Then
\[
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=2-1=1.
\]
:::

<1>3. By Green's theorem,
\[
\int_\gamma y\,dx+2x\,dy
=\iint_D 1\,dA.
\]

<1>4. Therefore
\[
\boxed{\int_\gamma y\,dx+2x\,dy=\pi}.
\]
::: {.proof}
The region $D$ is one quarter of a disk of radius $2$, so
\[
\operatorname{area}(D)=\frac14\pi(2)^2=\pi.
\]
Combining this with <1>3 gives the result.
:::
