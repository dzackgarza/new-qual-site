---
schema: qual/card@1
id: P-5YTY5
kind: problem
title: The line integral $\int_\Delta y\,dx+2x\,dy$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Fourteen steps asserted their claim with no justification; the card is now six steps each deriving its
    claim. Green's theorem is applied in one step, with the components $P = y$ and $Q = 2x$, the partials
    $\partial Q/\partial x = 2$ and $\partial P/\partial y = 1$, and the identification of $\iint_D 1\,dA$
    with the area, and the orientation is now stated as the reason $D$ lies to the left of the traversal.
    The area is one step: $AC$ horizontal of length $2$, $BC$ vertical of length $1$, a right angle at $C$,
    and half the product. The direct computation keeps one step per edge, each with its parametrization,
    the differentials and the integral, and the last step computes the third edge, sums the three to
    $I = 1$, and records that this agrees with the area from Green's theorem. The "Goal" paragraph
    restating the problem is gone, the label-claims ("Setting up Green's Theorem", "Computation of the
    Area", "Alternative Direct Line Integral Computation", "Conclusion") are replaced by the assertions
    their proofs establish, and the terminal step that only repeated the value is gone. Sources are cited
    by numbered statement: Green's theorem, and additivity of the path integral over concatenation. No
    page reference is written in the body of this card or in the event above. The statement is unchanged.
    The collection retains the UGA prelim Fall 2007 paper and no solution sheet, so the argument is the
    card's own.
---

::: {.problem}
Let $\Delta$ be the triangular boundary in $\RR^2$ with vertices $(0,1)$, $(2,0)$, and $(2,1)$, traversed counterclockwise.
Evaluate the line integral:
$$I = \oint_{\Delta} y \, dx + 2x \, dy.$$
:::

::: {.solution}
**Goal:** Evaluate the closed line integral $\oint_\Delta y\,dx + 2x\,dy$ around the oriented triangle using Green's Theorem.

::: pf

::: {.pf-step #green}
$I = \operatorname{Area}(D)$.

::: pf-proof
Let $D$ be the filled triangle and $\Delta = \partial D$ its boundary, traversed counterclockwise, so $D$ lies to the left of the traversal. The components are $P(x,y) = y$ and $Q(x,y) = 2x$, with $\partial Q/\partial x = 2$ and $\partial P/\partial y = 1$ continuous on $\RR^2$. Green's theorem then gives
$$\oint_{\Delta} P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA = \iint_D (2-1)\,dA = \iint_D 1\,dA = \operatorname{Area}(D),$$
the last equality being the definition of the area of a plane region as the integral of $1$ over it.
:::

:::

::: {.pf-step #area}
$\operatorname{Area}(D) = 1$.

::: pf-proof
The vertices are $A = (0,1)$, $B = (2,0)$ and $C = (2,1)$. The segment $AC$ runs from $(0,1)$ to $(2,1)$, so it is horizontal of length $2$, and $BC$ runs from $(2,0)$ to $(2,1)$, so it is vertical of length $1$. A horizontal and a vertical segment meeting at $C$ are perpendicular, so the triangle is right-angled at $C$ with legs $2$ and $1$, and its area is $\tfrac{1}{2}\cdot 2 \cdot 1 = 1$.
:::

:::

::: {.pf-step #direct}
The integral over $\Delta$ is the sum of the integrals over the three edges.

::: pf-proof
The boundary is traversed in the three edges $A \to B$, $B \to C$, $C \to A$ in that order. A path integral is additive over concatenation of paths, so $\oint_\Delta y\,dx + 2x\,dy$ is the sum of the three edge integrals, which the next three steps evaluate.
:::

:::

::: {.pf-step #edge-ab}
$\int_{C_1} y\,dx + 2x\,dy = -1$ along the segment from $(0,1)$ to $(2,0)$.

::: pf-proof
The parametrization $r_1(t) = (2t, 1-t)$ for $t \in [0,1]$ runs from $(0,1)$ to $(2,0)$, so $dx = 2\,dt$ and $dy = -dt$, giving
$$\int_0^1 \left((1-t)\cdot 2 + 2(2t)\cdot(-1)\right) dt = \int_0^1 (2 - 6t)\,dt = 2 - 3 = -1.$$
:::

:::

::: {.pf-step #edge-bc}
$\int_{C_2} y\,dx + 2x\,dy = 4$ along the segment from $(2,0)$ to $(2,1)$.

::: pf-proof
The parametrization $r_2(t) = (2,t)$ for $t \in [0,1]$ has $dx = 0$ and $dy = dt$, and $2x = 4$ on this segment, so the integral is $\int_0^1 4\,dt = 4$.
:::

:::

::: {.pf-step #edge-ca}
$I = \boxed{1}$.

::: pf-proof
Along the segment from $(2,1)$ to $(0,1)$ the parametrization $r_3(t) = (2-2t, 1)$ for $t \in [0,1]$ has $dx = -2\,dt$ and $dy = 0$, and $y = 1$ there, so $\int_{C_3} y\,dx + 2x\,dy = \int_0^1 (-2)\,dt = -2$. Adding the three edge integrals of the preceding steps gives $I = -1 + 4 - 2 = 1$, which agrees with the value $\operatorname{Area}(D) = 1$ that Green's theorem gave in step [](#green){.pf-ref}.
:::

:::

:::
:::
