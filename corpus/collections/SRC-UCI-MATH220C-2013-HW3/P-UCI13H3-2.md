---
schema: qual/card@1
id: P-UCI13H3-2
kind: problem
title: Zeros of $\alpha e^z-z$ in the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $U=\{\abs z<1\}$.
Show that $f(z)=\alpha e^z-z$ has only one zero in $U$ if $\abs\alpha<\frac13$, and no zeros in $U$ if $\abs\alpha>3$.
:::

::: {.solution}
Write $f(z)=\alpha e^z-z$ and compare its two summands on the circle $\abs z=1$, where $\abs{-z}=1$ and $e^{-1}\le\abs{e^z}\le e$ because $\abs z=1$ gives $-1\le\operatorname{Re}z\le1$.

::: pf

::: {.pf-step #small-alpha}
If $\abs\alpha<\frac13$, then $f$ has exactly one zero in $U$.

::: pf-proof
On $\abs z=1$ we have $\abs{\alpha e^z}\le\abs\alpha\,e<\frac{e}{3}<1=\abs{-z}$.
By Rouché's theorem $f=\alpha e^z-z$ has as many zeros in $U$ as the dominating summand $-z$, namely one.
:::

:::

::: {.pf-step #large-alpha}
If $\abs\alpha>3$, then $f$ has no zero in $U$.

::: pf-proof
On $\abs z=1$ we have $\abs{\alpha e^z}\ge\abs\alpha\,e^{-1}>\frac{3}{e}>1=\abs{-z}$.
By Rouché's theorem $f$ has as many zeros in $U$ as the dominating summand $\alpha e^z$, namely none, since $e^z$ never vanishes.
:::

:::

:::
:::
