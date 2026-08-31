---
schema: qual/card@1
id: E-AMD-ON37VIEN
kind: exercise
title: $\nilrad{R}=\rad(0)$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that the nilradical is given by $\nilrad{R} = \rad(0)$.
:::

::: solution
**Goal:** both sides collect the elements with a power in $(0)$, so the two descriptions of the nilradical agree.

<1>1. Write $\rad{I} = \ts{ x \in R \st x^n \in I \text{ for some } n \geq 1 }$ for the radical of an ideal $I$, and $\nilrad{R} = \ts{ x \in R \st x^n = 0 \text{ for some } n \geq 1 }$ for the nilradical.

<1>2. $\nilrad{R} \subseteq \rad{(0)}$.
::: {.proof}
If $x^n = 0$ then $x^n \in (0)$, since $(0) = \ts 0$.
:::

<1>3. $\rad{(0)} \subseteq \nilrad{R}$.
::: {.proof}
If $x^n \in (0)$ then $x^n = 0$, since $(0)$ has $0$ as its only element.
:::

<1>4. Q.E.D.
::: {.proof}
Steps <1>2 and <1>3 give the two inclusions, so $\nilrad{R} = \rad{(0)}$.
:::
:::
