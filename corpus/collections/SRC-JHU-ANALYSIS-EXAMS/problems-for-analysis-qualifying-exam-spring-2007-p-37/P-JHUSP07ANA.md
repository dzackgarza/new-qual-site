---
schema: qual/card@1
id: P-JHUSP07ANA
kind: problem
title: "Zeros of a sextic in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
1) How many zeros does the polynomial $z ^ { 6 } - 2 z ^ { 5 } + 7 z ^ { 4 } + z ^ { 3 } - z + 1$ have in the open unit disc $D = \{ z : | z | < 1 \} ?$
:::

::: {.solution}
Let $p(z)=z^6-2z^5+7z^4+z^3-z+1$.

<1>1. On $\abs z=1$, $\abs{p(z)-7z^4}<\abs{7z^4}$.

::: {.proof}
$\abs{z^6-2z^5+z^3-z+1}\le1+2+1+1+1=6<7$.
:::

<1>2. Q.E.D.

::: {.proof}
By step <1>1 and Rouché's theorem, $p$ has as many zeros in $\abs z<1$ as $7z^4$, namely $\boxed{4}$, counted with multiplicity.
:::
:::
