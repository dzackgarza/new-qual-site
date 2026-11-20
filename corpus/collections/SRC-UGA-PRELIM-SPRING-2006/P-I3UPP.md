---
schema: qual/card@1
id: P-I3UPP
kind: problem
title: The line integral $\int_\tau x\,dy+y\,dx$ along the unit-circle arc from $(1,0)$
  to $(3/5,4/5)$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight steps asserted their claim with no justification and the card is now three steps each deriving its
    claim: exactness of $y\,dx + x\,dy$, with the product rule giving $d(xy)$ and the fundamental theorem
    for line integrals giving $f(B) - f(A)$, together with the remark that the value depends only on the
    endpoints, which is what licenses computing it on any path; the evaluation $\frac{12}{25}$ from the two
    endpoint values; and the independent check by parametrizing the arc, where $\sin(2t_0) = 2\sin t_0\cos
    t_0$ is now written out rather than left implicit. The three label-claims are replaced by the assertions
    their proofs establish, and the closing pf-qed, which only restated the value, is gone. Sources are cited
    by numbered statement: the fundamental theorem for line integrals, and the product rule for
    differentials; no page reference is written in the body of this card or in the event above. The
    statement is unchanged. The collection retains the UGA prelim Spring 2006 paper and no solution sheet,
    so the argument is the card's own.
---

::: {.problem}
Let $\tau$ be the arc of the unit circle in the first quadrant, from $(1,0)$ to $(3/5, 4/5)$.
Compute $$\int_\tau x\,dy + y\,dx.$$
:::

::: {.solution}

::: pf

::: {.pf-step #potential}
$\omega = y\,dx + x\,dy$ equals $d(xy)$, so $\int_\tau \omega = f(B) - f(A)$ for $f(x,y) = xy$ and every piecewise smooth path from $A$ to $B$.

::: pf-proof
The product rule for differentials gives $d(xy) = y\,dx + x\,dy = \omega$, so $\omega$ is exact on $\RR^2$ with potential $f(x,y) = xy$. The fundamental theorem for line integrals then says that for a piecewise smooth path $\tau$ from $A$ to $B$, $\int_\tau \omega = \int_\tau df = f(B) - f(A)$; in particular the value depends only on the endpoints, not on the path, which is why the arc of the circle may be replaced by any path with the same endpoints.
:::

:::

::: {.pf-step #value}
$\int_\tau x\,dy + y\,dx = \frac{12}{25}$.

::: pf-proof
With $f(x,y) = xy$ and the endpoints $A = (1,0)$ and $B = (3/5, 4/5)$ one has $f(A) = 1 \cdot 0 = 0$ and $f(B) = \frac35 \cdot \frac45 = \frac{12}{25}$. The preceding step gives $\int_\tau (x\,dy + y\,dx) = f(B) - f(A) = \frac{12}{25} - 0 = \frac{12}{25}$.
:::

:::

::: pf-step

$\int_\tau x\,dy + y\,dx = \frac{12}{25}$ by direct parametrization, agreeing with the potential computation.

::: pf-proof
Parametrize the arc by $x(t) = \cos t$ and $y(t) = \sin t$ for $t \in [0, t_0]$, where $\cos t_0 = 3/5$ and $\sin t_0 = 4/5$; then $dx = -\sin t\,dt$ and $dy = \cos t\,dt$, so the integrand is
$$x\,dy + y\,dx = \cos^2 t\,dt - \sin^2 t\,dt = \cos(2t)\,dt.$$
Integrating, $\int_0^{t_0}\cos(2t)\,dt = \left[\frac{\sin(2t)}{2}\right]_0^{t_0} = \frac{\sin(2t_0)}{2} = \sin t_0\cos t_0 = \frac45\cdot\frac35 = \frac{12}{25}$, using $\sin(2t_0) = 2\sin t_0\cos t_0$. This agrees with step [](#value){.pf-ref}.
:::

:::

:::
:::
