---
schema: qual/card@1
id: E-SS3.EX-22
kind: problem
title: No holomorphic function on the disk can extend continuously with boundary values $1/z$
classification:
  areas:
    - complex-analysis
  topics: [Cauchy's Theorem, Holomorphic Extension, Unit Disc]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into numbered steps for issue #2: the function $zf(z)-1$, its vanishing on the boundary,
      the maximum modulus principle, and the contradiction at the origin. No retained solution set covers this
      exercise (the collection retains the textbook, not a solutions manual), so the argument is the card's
      own; it was re-read for this pass.
---

::: {.exercise}
Show that there is no holomorphic function $f$ in the unit disc $\DD$ that extends continuously to $\partial\DD$ such that $f(z) = 1/z$ for $z \in \partial\DD$.
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Suppose such an $f$ exists: holomorphic in $\DD$, continuous on $\overline{\DD}$, with $f(z)=1/z$ for $\abs{z}=1$.

::: pf

::: {.pf-step #h}
$h(z)=zf(z)-1$ is holomorphic in $\DD$ and continuous on $\overline{\DD}$.

::: pf-proof
$z\mapsto z$ and $f$ are holomorphic in $\DD$, so their product is, and subtracting the constant $1$ preserves holomorphy; continuity on the closed disc follows from continuity of $z$, $f$ and the constant there.
:::

:::

::: {.pf-step #boundary}
$h(z)=0$ for every $z$ with $\abs{z}=1$.

::: pf-proof
For such $z$ we have $f(z)=1/z$ by hypothesis, so $h(z)=z\cdot\frac{1}{z}-1=1-1=0$.
:::

:::

::: {.pf-step #max}
$h\equiv0$ on $\DD$.

::: pf-proof
$h$ is holomorphic in $\DD$ and continuous on the compact set $\overline{\DD}$, so by the maximum modulus principle $\abs{h(z)}\le\max_{\abs{\zeta}=1}\abs{h(\zeta)}$ for every $z\in\DD$. That maximum is $0$ by step [](#boundary){.pf-ref}, so $h(z)=0$ throughout $\DD$.
:::

:::

::: {.pf-step}
No such $f$ exists.

::: pf-proof
By step [](#max){.pf-ref} $h(0)=0$, but $h(0)=0\cdot f(0)-1=-1$ from the definition of $h$. A function continuous on the disc cannot take the value $0$ at every point and $-1$ at the origin, so the supposition fails: there is no holomorphic $f$ on $\DD$, continuous up to the boundary, agreeing with $1/z$ there.
:::

:::

:::
:::
