---
schema: qual/card@1
id: P-LF4NL
kind: problem
title: $\lim_{x\to 1}\frac{x^2+1}{x}=2$
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
    Restructured the prose solution into a Lamport proof and checked it: the algebraic
    identity (x^2+1)/x - 2 = (x-1)^2/x, the properties of delta = min(1/2, sqrt(eps/2)),
    the lower bound |x| > 1/2 on the delta-neighbourhood, and the estimate 2|x-1|^2 <
    2 delta^2 <= eps. Each of those was a single line of the prose; they are now
    separate steps with their justifications. The collection's provenance is the
    examination paper only, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
Use the $\varepsilon$-$\delta$ definition of the limit to prove that
$$
\lim_{x\to1}\frac{x^2+1}{x}=2.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #identity}
For every $x\ne0$,
$$
\frac{x^2+1}{x}-2=\frac{x^2-2x+1}{x}=\frac{(x-1)^2}{x}.
$$

::: pf-proof
Put the left side over the common denominator $x$.
:::

:::

::: {.pf-step #delta}
For every $\varepsilon>0$ the number $\delta\coloneqq\min\left\{\frac12,\sqrt{\frac\varepsilon2}\right\}$ is positive and satisfies $\delta\le\frac12$ and $\delta^2\le\frac\varepsilon2$.

::: pf-proof
Both entries of the minimum are positive, and $\delta$ is at most each of them; squaring the second bound, which is between positive numbers, gives $\delta^2\le\varepsilon/2$.
:::

:::

::: {.pf-step #lower-bound}
If $\abs{x-1}<\delta$ then $x\ne0$ and $\abs{x}>\frac12$.

::: pf-proof
By step [](#delta){.pf-ref}, $\abs{x-1}<\delta\le\frac12$, so $x\in\left(\frac12,\frac32\right)$ and in particular $\abs{x}=x>\frac12$.
:::

:::

::: {.pf-step #estimate}
If $0<\varepsilon$ and $\abs{x-1}<\delta$ for the $\delta$ of step [](#delta){.pf-ref}, then
$$
\abs{\frac{x^2+1}{x}-2}<\varepsilon .
$$

::: pf-proof
By steps [](#identity){.pf-ref} and [](#lower-bound){.pf-ref}, $x\ne0$ and
$$
\abs{\frac{x^2+1}{x}-2}=\frac{\abs{x-1}^2}{\abs{x}}<2\abs{x-1}^2<2\delta^2\le\varepsilon,
$$
the second inequality using $\abs{x}>\frac12$ and the last step [](#delta){.pf-ref}.
:::

:::

::: {.pf-step}
$\lim_{x\to1}\frac{x^2+1}{x}=2$.

::: pf-proof
Steps [](#delta){.pf-ref} and [](#estimate){.pf-ref} say exactly this: for every $\varepsilon>0$ there is $\delta>0$ such that every $x$ with $0<\abs{x-1}<\delta$ satisfies the estimate.
:::

:::

:::
:::
