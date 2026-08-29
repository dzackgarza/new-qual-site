---
schema: qual/card@1
id: P-AMD-PGA3YVH7
kind: problem
title: $\langle x,y\mid xy^2=y^3,\, yx^2=x^3 y\rangle$ is trivial
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Commutators
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show: $\generators{x,y \mid xy^2 = y^3, yx^2 = x^3y} = \generators{e}$
:::

::: {.solution}
<1>1. From $xy^2 = y^3$, we get $x = y$ (multiplying on the right by $y^{-2}$).
Proof: $xy^2 = y^3 \Rightarrow x = y^3 y^{-2} = y$.

<1>2. Substituting $x = y$ into $yx^2 = x^3 y$ gives $y \cdot y^2 = y^3 \cdot y$, i.e. $y^3 = y^4$.
Proof: <1>1.

<1>3. Hence $y = e$ (multiplying by $y^{-3}$).
Proof: $y^3 = y^4 \Rightarrow e = y$.

<1>4. Therefore $x = y = e$, so the group is trivial.
Proof: <1>1 and <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
