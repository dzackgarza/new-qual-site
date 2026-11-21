---
schema: qual/card@1
id: P-L3LHW
kind: problem
title: $\lim_{x\to 2}\frac{1}{3+x}=\frac{1}{5}$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the epsilon-delta limit. The choice of delta = min{1, 20 epsilon} is now justified (positive because both entries are), the lower bound on |5(3+x)| is derived from 1 < x < 3 rather than asserted, and the algebraic identity is displayed before it is bounded. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the bound delta = min{1, 20 epsilon} is the one the prose already used and it is correct.
---

::: {.problem}
Give an $\varepsilon$-$\delta$ proof that
$$
\lim_{x\to2}\frac1{3+x}=\frac15.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #choice}
Let $\varepsilon>0$ and put $\delta=\min\{1,20\varepsilon\}$. Then $\delta>0$.

::: pf-proof
$1>0$ and $20\varepsilon>0$ because $\varepsilon>0$, so their minimum is positive.
:::

:::

::: {.pf-step #bound}
If $\abs{x-2}<\delta$ then $\abs{5(3+x)}>20$, and in particular $3+x\ne0$.

::: pf-proof
$\abs{x-2}<\delta\le1$ gives $-1<x-2<1$, so $1<x<3$ and $4<3+x<6$. Hence $5(3+x)$ lies strictly between $20$ and $30$, so its absolute value exceeds $20$ and it is nonzero.
:::

:::

::: {.pf-step #estimate}
If $\abs{x-2}<\delta$ then $\abs{\dfrac1{3+x}-\dfrac15}<\varepsilon$.

::: pf-proof
Putting the difference over a common denominator,
$$
\frac1{3+x}-\frac15=\frac{5-(3+x)}{5(3+x)}=\frac{2-x}{5(3+x)},
$$
so by step [](#bound){.pf-ref}
$$
\abs{\frac1{3+x}-\frac15}=\frac{\abs{x-2}}{\abs{5(3+x)}}<\frac{\abs{x-2}}{20}<\frac{20\varepsilon}{20}=\varepsilon,
$$
the last inequality because $\abs{x-2}<\delta\le20\varepsilon$.
:::

:::

::: {.pf-step}
$\lim_{x\to2}\dfrac1{3+x}=\dfrac15$.

::: pf-proof
Given $\varepsilon>0$, step [](#choice){.pf-ref} supplies $\delta>0$ such that step [](#estimate){.pf-ref} holds for every $x$ with $0<\abs{x-2}<\delta$; the function $x\mapsto1/(3+x)$ is defined near $2$ by step [](#bound){.pf-ref}. This is the definition of the limit.
:::

:::

:::
:::
