---
schema: qual/card@1
id: P-PRACT20-W3-19
kind: problem
title: Volume between the paraboloids $z=6-x^2-2y^2$ and $z=-2+x^2+2y^2$
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
    Read against page 5-6 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for an area integral representing the volume between the same two paraboloids, and the printed solution gives the same ellipse and the same integrand
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's computation of the intersection ellipse and its integral are transcribed, with the region described slice by slice and the positivity of the height verified.
---

::: {.problem}
Set up an area integral (i.e. an integral in $xy$-space) which represents the volume of the solid bounded above by the graph of $z = 6 - x^{2} - 2y^{2}$ and below by the graph of $z = -2 + x^{2} + 2y^{2}$.
:::

::: {.solution}

Set up an iterated integral in the $xy$-plane for the volume between
$z=6-x^2-2y^2$ above and $z=-2+x^2+2y^2$ below.

::: pf

::: {.pf-step #region}

The two graphs meet where $x^2+2y^2=4$, an ellipse bounding the region $D$ in
which the upper graph lies above the lower.

::: pf-proof

Equating $6-x^2-2y^2=-2+x^2+2y^2$ gives $2x^2+4y^2=8$, that is $x^2+2y^2=4$;
this is an ellipse with $-2\le x\le2$. Inside it, $x^2+2y^2<4$, and the
difference $(6-x^2-2y^2)-(-2+x^2+2y^2)=8-2x^2-4y^2=2(4-x^2-2y^2)$ is positive,
so the first graph is above the second.

:::

:::

::: {.pf-step #height}

The height of the solid over a point of $D$ is $8-2x^2-4y^2$.

::: pf-proof

The height is the difference of the two $z$-values at $(x,y)$, computed in
step [](#region){.pf-ref}; it is positive on $D$ and vanishes on the boundary
ellipse, which is what makes the solid a region under one graph and above the
other.

:::

:::

::: {.pf-step #integral}

$\displaystyle\text{volume}=\int_{-2}^{2}\int_{-\sqrt{(4-x^2)/2}}^{\sqrt{(4-x^2)/2}}\big(8-2x^2-4y^2\big)\,dy\,dx$.

::: pf-proof

For fixed $x\in[-2,2]$ the ellipse condition $x^2+2y^2\le4$ is
$y^2\le\frac{4-x^2}{2}$, so the section of $D$ at $x$ is the interval
$\big[-\sqrt{(4-x^2)/2},\sqrt{(4-x^2)/2}\big]$. Integrating the height of step
[](#height){.pf-ref} over that interval and then over $x$ gives the volume by
Fubini, the integrand being continuous on the compact region; the printed
solution writes the same integral with the bounds in exactly this form.

:::

:::

:::


:::
