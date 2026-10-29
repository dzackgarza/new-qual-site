---
schema: qual/card@1
id: P-CALCPT3-27
kind: problem
title: "Surface of revolution of $z=f(y)$ about the $y$-axis"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 27 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
If the curve in the $yz$-plane with equation $z=f(y)$ is rotated around the $y$-axis, an equation of the resulting surface of revolution is

(A) $x^2+z^2=[f(y)]^2$
(B) $x^2+z^2=f(y)$
(C) $x^2+z^2=|f(y)|$
(D) $y^2+z^2=|f(y)|$
(E) $y^2+z^2=[f(x)]^2$
:::

::: {.solution}
The distance from a point $(x,y,z)$ to the $y$-axis is $\sqrt{x^2+z^2}$, and rotation about the $y$-axis preserves both $y$ and this distance.

::: pf

::: {.pf-step #orbit}
For fixed $y$, the rotation of the curve point $(0,y,f(y))$ sweeps out exactly the circle $\{(x,y,z): x^2+z^2=[f(y)]^2\}$ in the plane at height $y$.

::: pf-proof
The point $(0,y,f(y))$ is at distance $\abs{f(y)}$ from the $y$-axis.
Rotations about the $y$-axis act on the $(x,z)$ coordinates as all rotations of the plane about the origin, so the orbit of $(0,f(y))$ is the full circle of radius $\abs{f(y)}$ centred at the origin (a single point when $f(y)=0$).
:::

:::

::: pf-step
The surface is $\boxed{x^2+z^2=[f(y)]^2}$, choice (A).

::: pf-proof
The surface of revolution is the union over $y$ of the circles of step [](#orbit){.pf-ref}, which is the set of points with $x^2+z^2=[f(y)]^2$.
Choices (B) and (C) equate a squared distance with a quantity that is not squared, and (D) and (E) measure distance from the wrong axis.
:::

:::

:::

:::
