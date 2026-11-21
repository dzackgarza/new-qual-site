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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card opened with a verdict step — 'The value depends on the
    orientation ... = 1/2' — holding no proof, and closed with an unproved remark on reversing
    orientation. It is now three proved steps: the direct computation through the four sides
    with each contribution named, the Green's theorem computation with the partial derivatives
    and the separated double integral, and a closing step that records the agreement of the two
    methods and the sign under reversal. The answers are unchanged (1/2 counterclockwise, -1/2
    clockwise). Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Consider the line integral $\int_C 2x\,dx + x^2y\,dy$, where $C$ is the boundary of the unit square in the 1st quadrant.
Evaluate the line integral (a) directly and (b) by using Green's theorem.
:::

::: {.solution}
Throughout $C$ is the boundary of the unit square $[0,1]^{2}$, traversed counterclockwise unless stated otherwise, and the form is $\omega \coloneqq 2x\,dx + x^{2}y\,dy$, so that $P = 2x$ and $Q = x^{2}y$. The collection's `provenance` is the Spring 2003 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #direct}
(a) Directly, $\int_{C}2x\,dx + x^{2}y\,dy = \frac12$ for the counterclockwise orientation.

::: pf-proof
Split $C$ into its four sides. Bottom, $(0,0) \to (1,0)$: here $y = 0$ and $dy = 0$, so the integral is $\int_{0}^{1}2x\\,dx = 1$. Right side, $(1,0) \to (1,1)$: here $x = 1$ and $dx = 0$, so it is $\int_{0}^{1}1\cdot y\\,dy = \tfrac12$. Top, $(1,1) \to (0,1)$: here $y = 1$ and $dy = 0$, so it is $\int_{1}^{0}2x\\,dx = -1$. Left side, $(0,1) \to (0,0)$: here $x = 0$, $dx = 0$, and the form $x^{2}y\\,dy$ vanishes identically. The total is $1 + \tfrac12 - 1 + 0 = \tfrac12$.

:::

:::

::: {.pf-step #green}
(b) By Green's theorem the same value is $\iint_{D}2xy\\,dA = \frac12$.

::: pf-proof
$P = 2x$ and $Q = x^{2}y$ have continuous partial derivatives on the plane and $C$ is the positively oriented boundary of the square $D = [0,1]^{2}$, so Green's theorem applies: $\int_{C}P\\,dx + Q\\,dy = \iint_{D}\bigl(\partial Q/\partial x - \partial P/\partial y\bigr)dA$. Here $\partial Q/\partial x = 2xy$ and $\partial P/\partial y = 0$, so the integrand is $2xy$, and $\iint_{D}2xy\\,dA = 2\int_{0}^{1}x\\,dx\int_{0}^{1}y\\,dy = 2\cdot\tfrac12\cdot\tfrac12 = \tfrac12$ by separation of the variables.

:::

:::

::: pf-step
The two computations agree: $\int_{C}2x\,dx + x^{2}y\,dy = \boxed{\frac12}$ for the counterclockwise orientation, and $-\frac12$ for the clockwise one.

::: pf-proof
Step [](#direct){.pf-ref} gives the value from the parametrisation of the four sides and step [](#green){.pf-ref} from the double integral, and both give $\tfrac12$; this is the content of the exercise, that the two methods agree. Reversing the orientation of a closed curve reverses the sign of the integral, because the parametrisation $t \mapsto c(1-t)$ replaces $dx$ and $dy$ by their negatives, so the clockwise value is $-\tfrac12$; the source does not name an orientation, and the counterclockwise one is the orientation Green's theorem uses.

:::

:::

:::
:::
