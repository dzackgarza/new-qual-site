---
schema: qual/card@1
id: P-3OH6H
kind: problem
title: $\lim_{x\to 2}(x+1/x)=5/2$
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
    Restructured the prose solution into a Lamport proof and checked it: the identity
    x + 1/x - 5/2 = (2x-1)(x-2)/(2x), the three properties of delta = min(1, 2eps/5)
    including (5/2)delta <= eps, the window 1 < x < 3 giving |2x-1| < 5 and 2x > 2, and
    the resulting estimate. The bounds |2x-1| < 5 and |x| > 1 were one line of the prose
    each and are now derived. The collection's provenance is the examination paper only,
    so no retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Use the $\varepsilon$-$\delta$ definition to prove that
$$
\lim_{x\to2}\left(x+\frac1x\right)=\frac52.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #identity}
For every $x\ne0$,
$$
x+\frac1x-\frac52=\frac{2x^2-5x+2}{2x}=\frac{(2x-1)(x-2)}{2x}.
$$

::: pf-proof
Put the left side over the common denominator $2x$ and factor the numerator, whose roots are $\frac12$ and $2$.
:::

:::

::: {.pf-step #delta}
For every $\varepsilon>0$ the number $\delta\coloneqq\min\left\{1,\frac{2\varepsilon}{5}\right\}$ is positive, satisfies $\delta\le1$, and satisfies $\frac52\delta\le\varepsilon$.

::: pf-proof
Both entries of the minimum are positive, so $\delta>0$ and $\delta\le1$. Also $\delta\le\frac{2\varepsilon}{5}$, and multiplying by $\frac52>0$ gives the last claim.
:::

:::

::: {.pf-step #window}
If $0<\abs{x-2}<\delta$ then $1<x<3$, hence $x>0$ and $\abs{2x-1}<5$.

::: pf-proof
Step [](#delta){.pf-ref} gives $\abs{x-2}<\delta\le1$, so $x\in(2-1,2+1)=(1,3)$. Then $2x-1\in(1,5)$, which is positive, so $\abs{2x-1}=2x-1<5$; and $x>1>0$, so the denominator in step [](#identity){.pf-ref} does not vanish.
:::

:::

::: {.pf-step #estimate}
If $\varepsilon>0$ and $0<\abs{x-2}<\delta$ for the $\delta$ of step [](#delta){.pf-ref}, then
$$
\abs{x+\frac1x-\frac52}<\varepsilon .
$$

::: pf-proof
By steps [](#identity){.pf-ref} and [](#window){.pf-ref},
$$
\abs{x+\frac1x-\frac52}=\frac{\abs{2x-1}\,\abs{x-2}}{2\abs{x}}=\frac{\abs{2x-1}\,\abs{x-2}}{2x}<\frac{5\abs{x-2}}{2}<\frac52\delta\le\varepsilon,
$$
using $\abs{2x-1}<5$ and $2x>2$ in the second inequality, $\abs{x-2}<\delta$ in the third, and step [](#delta){.pf-ref} in the last.
:::

:::

::: {.pf-step}
$\lim_{x\to2}\left(x+\frac1x\right)=\frac52$.

::: pf-proof
Steps [](#delta){.pf-ref} and [](#estimate){.pf-ref} give, for every $\varepsilon>0$, a $\delta>0$ such that every $x$ with $0<\abs{x-2}<\delta$ satisfies the estimate; that is the $\varepsilon$-$\delta$ definition of the limit.
:::

:::

:::
:::
