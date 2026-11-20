---
schema: qual/card@1
id: P-PRACT20-W4-03
kind: problem
title: Salt in a tank with equal inflow and outflow rates
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the retained Week 4 solutions at assets/attachments/Week4_solns.pdf, page 1,
    Problem 3: a tank with 3 grams of salt in 100 liters, inflow 0.02 grams per liter at 4 liters per
    minute, outflow 4 liters per minute, ask the content after 100 minutes. The card's statement is
    that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the retained solution's argument. The rates are written out
    (0.08 grams per minute in, S/25 grams per minute out) and the constancy of the volume is
    attributed to the equality of the two rates, which is what fixes the concentration at S/100.
    The retained solution writes the general solution as 2 - C e^{-t/25} with C = -1, the card as
    2 + e^{-t/25}; the two agree, and the card now says so rather than leaving the reader to reconcile
    them. Value checked: S(100) = 2 + e^{-4}, about 2.018 grams. No page of the retained set was
    guessed: the salt problem was located on PDF page 1 by searching the pages.
---

::: {.problem}
A tank initially contains a salt solution of 3 grams of salt dissolved in 100 liters of water.
A salt solution containing 0.02 grams of salt per liter is pumped into the tank at 4 liters per minute.
The tank is also draining at 4 liters per minute.
Assuming the mixing is instantaneous, how many grams of salt are in the tank after 100 minutes?
:::

::: {.solution}
This is Problem 3 of the retained Week 4 preliminary-practice solutions (`assets/attachments/Week4_solns.pdf`), and the argument is that solution's, with its sign convention made explicit: it writes $S(t)=2-Ce^{-t/25}$ with $C=-1$, which is the same function as $S(t)=2+e^{-t/25}$ below.

::: pf

::: {.pf-step #model}
The volume stays at $100$ liters, so with $t$ in minutes and $S(t)$ the salt content in grams,
$$\frac{dS}{dt}=0.02\cdot4-4\cdot\frac{S}{100}=\frac{2}{25}-\frac{S}{25},\qquad S(0)=3.$$

::: pf-proof
Inflow brings $0.02$ grams per liter at $4$ liters per minute, that is $0.08$ grams per minute; outflow removes the tank concentration $S/100$ grams per liter at $4$ liters per minute, that is $S/25$ grams per minute. The volume is constant because the two rates agree, so the concentration depends only on the present content $S$, and mixing is instantaneous by hypothesis. The initial content is the $3$ grams stated.
:::
:::

::: {.pf-step #solve}
The solutions of this equation are $S(t)=2+Ce^{-t/25}$.

::: pf-proof
The equation is linear with constant coefficients. A constant solution solves $0=\frac{2}{25}-\frac{S}{25}$ exactly when $S=2$, and the homogeneous equation $\dot S=-S/25$ has the solutions $Ce^{-t/25}$; a particular solution plus the general homogeneous solution is the general solution.
:::
:::

::: {.pf-step #initial}
$S(t)=2+e^{-t/25}$.

::: pf-proof
$S(0)=2+C=3$ gives $C=1$.
:::
:::

::: {.pf-step #value}
$S(100)=2+e^{-4}$ grams.

::: pf-proof
Substituting $t=100$ in step [](#initial){.pf-ref} gives $S(100)=2+e^{-100/25}=2+e^{-4}$, which is about $2.018$ grams.
:::
:::
:::

:::
