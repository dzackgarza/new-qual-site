---
schema: qual/card@1
id: P-3TOOU
kind: problem
title: The Möbius band is homotopy equivalent to $S^1\times I$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
  - Surfaces
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The problem block held a numbered solution sketch (deformation retract M = I x I/(x,0)~(1-x,1) onto {1/2} x I/~ by ((1-t)x+t/2, y), and compare with S^1 x I) instead of a question. The statement now asks for the homotopy equivalence; the solution carries the same argument."
---

::: {.problem}
Show that the Möbius band $M$ is homotopy equivalent to $S^1 \cross I$.
:::

::: {.solution}

Model the Möbius band as $M=[0,1]\times[-1,1]/{\sim}$, where $(0,t)\sim(1,-t)$, and write $C=\{[x,0]\}\cong S^1$ for its center circle.

::: pf

::: {.pf-step #mobius}

The homotopy $H_s([x,t])=[x,(1-s)t]$ is a strong deformation retraction of $M$ onto $C$.

::: pf-proof

It is compatible with the quotient relation because $(0,t)\sim(1,-t)$ implies $(0,(1-s)t)\sim(1,-(1-s)t)$. At $s=1$ every point lies on $C$, and points of $C$ are fixed throughout.

:::

:::

::: {.pf-step #cylinder}

The cylinder $S^1\times I$ strongly deformation retracts onto $S^1\times\{0\}\cong S^1$.

::: pf-proof

Use $(z,t,s)\mapsto(z,(1-s)t)$.

:::

:::

::: pf-step

$\boxed{M\simeq S^1\times I}$.

::: pf-proof

By steps [](#mobius){.pf-ref} and [](#cylinder){.pf-ref}, both spaces are homotopy equivalent to $S^1$.

:::

:::

:::

:::
