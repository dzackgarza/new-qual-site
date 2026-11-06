---
schema: qual/card@1
id: P-PRACT20-W3-21
kind: problem
title: Work done by a constant force along the twisted cubic $(t,t^2,t^3)$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Line Integrals
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
    source used for the statement. the printed problem states the same unit force direction, the same path and the same interval, and the printed solution obtains 0
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's computation of F dot r-prime and of the integral is transcribed; the card's statement says unit force, so the proof uses the normalised vector and records that the unnormalised one gives the same value because the integral vanishes.
---

::: {.problem}
Let $F$ be a constant unit force in the direction of $(-1, 0, 1)$. Find the work done by $F$ on a particle which moves along the path $r(t) = (t, t^{2}, t^{3})$ for $t \in [0, 1]$.
:::

::: {.solution}

The force is a constant vector; as a unit force in the direction of $(-1,0,1)$
it is $F=\frac{1}{\sqrt2}(-1,0,1)$, and the work along $r(t)=(t,t^2,t^3)$,
$0\le t\le1$, is $\int_0^1F\cdot r'(t)\,dt$.

::: pf

::: {.pf-step #data}

$r'(t)=(1,2t,3t^2)$ and $F\cdot r'(t)=\frac{1}{\sqrt2}\big(-1+3t^2\big)$.

::: pf-proof

Differentiating the components of $r$ gives $r'(t)=(1,2t,3t^2)$. Taking the
dot product with $F=\frac{1}{\sqrt2}(-1,0,1)$ gives
$\frac{1}{\sqrt2}\big(-1\cdot1+0\cdot2t+1\cdot3t^2\big)=\frac{1}{\sqrt2}(-1+3t^2)$.

:::

:::

::: {.pf-step #integral}

$\displaystyle W=\frac{1}{\sqrt2}\int_0^1(3t^2-1)\,dt=0$.

::: pf-proof

$\int_0^1 3t^2\,dt=\big[t^3\big]_0^1=1$ and $\int_0^1 1\,dt=1$, so the bracket
is $1-1=0$ and the work vanishes. The same number comes from the unnormalised
vector $(-1,0,1)$, which is what the printed solution differentiates against;
the two differ by the factor $\sqrt2$ of the force's magnitude, and since the
bracket is $0$ the work is $0$ under either normalisation. So the card's
answer does not depend on which of the two the statement means, and the
computation here uses the unit vector as the card states.

:::

:::

:::


:::
