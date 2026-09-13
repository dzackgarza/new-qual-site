---
schema: qual/card@1
id: P-MFVEZ
kind: problem
title: Line integral of $2x\,dx+x^2y\,dy$ on the unit square
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Consider the line integral $\int_C 2x\,dx + x^2y\,dy$, where $C$ is the boundary of the unit square in the 1st quadrant.
Evaluate the line integral (a) directly and (b) by using Green's theorem.
:::

::: solution
<1>1. The value depends on the orientation of $C$. For the positive (counterclockwise) orientation,
\[
\int_C 2x\,dx+x^2y\,dy=\frac12.
\]
For the clockwise orientation the value is $-\frac12$.
:::

<1>2. Compute the positively oriented integral directly by traversing the four sides
\[
(0,0)\to(1,0)\to(1,1)\to(0,1)\to(0,0).
\]

<1>3. The bottom side contributes $1$.
::: {.proof}
Along $y=0$, parameterize by $(x,0)$ for $0\le x\le1$. Then $dy=0$, so
\[
\int_0^1 2x\,dx=1.
\]
:::

<1>4. The right side contributes $\frac12$.
::: {.proof}
Along $x=1$, parameterize by $(1,y)$ for $0\le y\le1$. Then $dx=0$, so
\[
\int_0^1 y\,dy=\frac12.
\]
:::

<1>5. The top side contributes $-1$, and the left side contributes $0$.
::: {.proof}
Along the top side, $y=1$ and $x$ runs from $1$ to $0$, hence
\[
\int_1^0 2x\,dx=-1.
\]
Along the left side, $x=0$, so both terms vanish.
:::

<1>6. Therefore the direct computation gives
\[
1+\frac12-1+0=\frac12.
\]

<1>7. Green's theorem gives the same value.
::: {.proof}
Set $P(x,y)=2x$ and $Q(x,y)=x^2y$. For the unit square $D=[0,1]^2$ with positively oriented boundary,
\[
\int_C P\,dx+Q\,dy
=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA
=\int_0^1\int_0^1 2xy\,dx\,dy
=\frac12.
\]
:::

<1>8. Reversing the orientation changes the sign of every line integral, giving $-\frac12$ for clockwise orientation.
