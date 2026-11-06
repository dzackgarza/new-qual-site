---
schema: qual/card@1
id: P-PRACT20-W3-27
kind: problem
title: Line integral of $(xy,x^2y^3)$ around a triangle
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Green's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 8 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the path integral of the same field around the same triangle, and the printed solution evaluates it as 4/3 minus 2/3, that is 2/3
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's Green's theorem reduction and its iterated integral are transcribed, with the region described, the inner integral computed, and the value 2/3 obtained; the orientation is named as counterclockwise since neither document fixes it.
---

::: {.problem}
Let $C$ be the triangle with vertices $(0, 0)$, $(1, 0)$, $(1, 2)$. Find the path integral of $\mathbf{F}(x, y) = (xy, x^{2} y^{3})$ around this curve.
:::

::: {.solution}

Let $C$ be the triangle with vertices $(0,0),(1,0),(1,2)$ traversed
counterclockwise, bounding $D$, and let $F=(P,Q)=(xy,x^2y^3)$.

::: pf

::: {.pf-step #green}

$\displaystyle\oint_CF\cdot
dr=\iint_D\big(Q_x-P_y\big)\,dA=\iint_D\big(2xy^3-x\big)\,dA$.

::: pf-proof

$P$ and $Q$ are polynomials, hence continuously differentiable, so Green's
theorem applies to the positively oriented boundary: $\oint_C
P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA$. Here $Q_x=2xy^3$ and $P_y=x$, so the
integrand is $2xy^3-x$.

:::

:::

::: {.pf-step #iterate}

$\displaystyle\iint_D(2xy^3-x)\,dA=\int_0^1\int_0^{2x}(2xy^3-x)\,dy\,dx=\int_0^1\big(8x^5-2x^2\big)dx$.

::: pf-proof

The triangle with vertices $(0,0),(1,0),(1,2)$ is $\{(x,y):0\le x\le1,\ 0\le
y\le 2x\}$, since the hypotenuse joins $(0,0)$ to $(1,2)$. For fixed $x$,
$\int_0^{2x}2xy^3dy=2x\cdot\frac{(2x)^4}{4}=8x^5$ and $\int_0^{2x}x\,dy=2x^2$,
so the inner integral is $8x^5-2x^2$; Fubini applies as the integrand is
continuous on the compact triangle.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\oint_CF\cdot dr=\frac86-\frac23=\frac23}$.

::: pf-proof

$\int_0^1 8x^5dx=\frac86=\frac43$ and $\int_0^1 2x^2dx=\frac23$, so the
integral is $\frac43-\frac23=\frac23$. This is the printed value: the
booklet's displayed line reads $\int_0^1(8x^5-2x^2)dx$ with the evaluation
$\frac43-\frac23$ set in the type, which the extraction interleaves. The
orientation is not stated on either document; this is the counterclockwise
one, and the clockwise integral is $-\frac23$.

:::

:::

:::


:::
