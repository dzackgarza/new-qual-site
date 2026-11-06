---
schema: qual/card@1
id: P-PRACT20-W3-22
kind: problem
title: Integrating $e^{y^2}$ over a triangle by reversing the order of integration
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Multiple Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 6 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem integrates the same function over the same triangle, and the printed solution gives e^4 - 1
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's choice of order of integration is transcribed, with the region described as a triangle and the substitution u = y squared carried out.
---

::: {.problem}
Find the integral of $f(x, y) = e^{y^{2}}$ over the triangular region bounded by the graph of $y = \abs{x}$ for $x \in [-2, 2]$ and the line $y = 2$.
:::

::: {.solution}

The region is $T=\{(x,y):0\le y\le2,\ -y\le x\le y\}$, a triangle with
vertices $(-2,2),(2,2),(0,0)$; integrate in the order $x$ then $y$, since
$e^{y^2}$ has no elementary antiderivative in $y$ but its $x$-integral is
elementary.

::: pf

::: {.pf-step #region}

$T=\{(x,y):0\le y\le2,\ \abs x\le y\}$.

::: pf-proof

The conditions $y=\abs x$ for $x\in[-2,2]$ and $y\le2$ describe the set of
$(x,y)$ with $\abs x\le y\le2$; since $y\ge\abs x\ge0$ this is exactly the
triangle with the three stated vertices, and for each $y\in[0,2]$ the section
is the interval $[-y,y]$.

:::

:::

::: {.pf-step #inner}

$\displaystyle\int_{-y}^{y}e^{y^2}\,dx=2y\,e^{y^2}$ for each fixed $y$.

::: pf-proof

The integrand does not depend on $x$, so the integral over an interval of
length $2y$ is $2y\,e^{y^2}$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\iint_T e^{y^2}\,dx\,dy=\int_0^22y\,e^{y^2}\,dy=e^4-1}$.

::: pf-proof

By Fubini for the continuous integrand on the compact triangle, the double
integral is the iterated integral $\int_0^2\Big(\int_{-y}^ye^{y^2}dx\Big)dy$,
which by step [](#inner){.pf-ref} is $\int_0^22y\,e^{y^2}dy$. Substituting
$u=y^2$, $du=2y\,dy$ gives $\int_0^4e^u\,du=e^4-1$. So the value is $e^4-1$,
which is the printed answer; integrating in the other order would leave $\int
e^{y^2}dy$, which is why the order matters.

:::

:::

:::


:::
