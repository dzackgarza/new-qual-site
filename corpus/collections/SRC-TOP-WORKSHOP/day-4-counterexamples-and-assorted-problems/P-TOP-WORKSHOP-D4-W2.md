---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W2
kind: problem
title: A continuous bijective open (or closed) map is a homeomorphism
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the inverse shown continuous from the open-map
    hypothesis, then the same from the closed-map hypothesis, then the conclusion. No retained solution
    set covers this exercise (the collection retains the problem packets, not solutions), so the
    argument is the card's own; it was re-read for this pass.
---

::: {.problem}
Let $f:X\to Y$ be a continuous, bijective, open map.
Show that $f$ is a homeomorphism.
[Open map can be replaced with closed map and the same result holds.]
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. A homeomorphism is a continuous bijection whose inverse is continuous, so with bijectivity given, only the continuity of the inverse must be shown; continuity of a map $g$ can be checked on open sets, $g^{-1}(U)$ open for every open $U$, or equivalently on closed sets.

::: pf

::: {.pf-step #bijection}
$f$ has an inverse $f^{-1}:Y\to X$.

::: pf-proof
A bijective map has, for each $y\in Y$, exactly one preimage $x\in X$, and the assignment $y\mapsto x$ is a function $Y\to X$ with $f^{-1}\circ f=\mathrm{id}_{X}$ and $f\circ f^{-1}=\mathrm{id}_{Y}$.
:::

:::

::: {.pf-step #open-case}
If $f$ is open then $f^{-1}$ is continuous.

::: pf-proof
Let $U\subseteq X$ be open. The preimage of $U$ under $f^{-1}$ is
$$
(f^{-1})^{-1}(U)=\{y\in Y\mid f^{-1}(y)\in U\}=\{f(x)\mid x\in U\}=f(U),
$$
the middle equality because $f$ is bijective, and $f(U)$ is open in $Y$ because $f$ is an open map. So $f^{-1}$ pulls open sets back to open sets.
:::

:::

::: {.pf-step #closed-case}
If $f$ is closed then $f^{-1}$ is continuous.

::: pf-proof
Let $F\subseteq X$ be closed. As above, $(f^{-1})^{-1}(F)=f(F)$, and $f(F)$ is closed in $Y$ because $f$ is a closed map. So $f^{-1}$ pulls closed sets back to closed sets, which is the closed-set criterion for continuity.
:::

:::

::: {.pf-step}
A continuous bijection that is open, or closed, is a homeomorphism.

::: pf-proof
By steps [](#bijection){.pf-ref} the inverse exists; it is continuous by step [](#open-case){.pf-ref} in the open case and by step [](#closed-case){.pf-ref} in the closed case. So $f$ is a continuous bijection with continuous inverse, that is a homeomorphism, in either of the two hypotheses, which is the replacement the problem notes.
:::

:::

:::
:::
