---
schema: qual/card@1
id: P-OK5P3
kind: problem
title: Line integral of $y\,dx+2x\,dy$ along a three-quarter circle closed by the axes
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
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: The paper (page render) sends the arc from (2,0) to (0,-2), not (0,2); statement and solution
    now follow the three-quarter disk.
---

::: {.problem}
Let $\gamma$ be the closed path which goes counterclockwise around the circle $C(0,2) = \{(x,y) \in \RR^2 : x^2+y^2 = 2^2\}$ from the point $(2,0)$ to the point $(0,-2)$, then goes to the origin along the y-axis, and then back to $(2,0)$ along the x-axis.

Compute $\int_\gamma 2x\,dy + y\,dx$ in one of two ways:

(a) Directly, using the definition of a line integral; or

(b) By using Green's theorem or the general Stokes' theorem.
:::

::: {.solution}

::: pf

::: pf-step
The path $\gamma$ is the positively oriented boundary of the three-quarter disk
$$
D=\{(x,y):x^2+y^2\le4\}\setminus\{(x,y):x>0,\ y<0\}.
$$

::: pf-proof
The circular arc runs counterclockwise from $(2,0)$ through $(0,2)$ and $(-2,0)$ to $(0,-2)$, so it is the part of the circle outside the open fourth quadrant. The path then follows the negative $y$-axis up to the origin, with the third quadrant on its left, and the positive $x$-axis out to $(2,0)$, with the first quadrant on its left. Thus $D$ lies to the left of every piece of the traversal.
:::

:::

::: pf-step
Write the integrand as
$$
P\,dx+Q\,dy
\quad\text{with}\quad
P(x,y)=y,\qquad Q(x,y)=2x.
$$
Then
$$
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=2-1=1.
$$

:::

::: {.pf-step #s3}
By Green's theorem,
$$
\int_\gamma y\,dx+2x\,dy
=\iint_D 1\,dA.
$$

:::

::: pf-step
Therefore
$$
\boxed{\int_\gamma y\,dx+2x\,dy=3\pi}.
$$

::: pf-proof
The region $D$ is three quarters of a disk of radius $2$, so
$$
\operatorname{area}(D)=\frac34\pi(2)^2=3\pi.
$$
Combining this with step [](#s3){.pf-ref} gives the result.
:::

:::

:::

:::
