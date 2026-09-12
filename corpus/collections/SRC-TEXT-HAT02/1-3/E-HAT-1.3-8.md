---
schema: qual/card@1
id: E-HAT-1.3-8
kind: problem
title: "Simply-connected covers of homotopy equivalent spaces"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Lifted homotopy inverse maps to the simply connected covers and lifted the base homotopies to prove the two composites are homotopic to the identities.
---

Let $\tilde{X}$ and $\tilde{Y}$ be simply-connected covering spaces of the path-connected, locally path-connected spaces $X$ and $Y$.
Show that if $X \simeq Y$ then $\tilde{X} \simeq \tilde{Y}$.

::: {.solution}
Let
\[
p_X:\widetilde X\to X,
\qquad
p_Y:\widetilde Y\to Y
\]
be the given simply connected covering spaces.
Choose homotopy inverse maps
\[
f:X\to Y,
\qquad
g:Y\to X
\]
with
\[
g f\simeq\operatorname{id}_X,
\qquad
f g\simeq\operatorname{id}_Y.
\]

<1>1. The composite
\[
f\circ p_X:\widetilde X\to Y
\]
lifts to a map
\[
\widetilde f:\widetilde X\to\widetilde Y.
\]
::: {.proof}
Since $\widetilde X$ is simply connected,
\[
(f p_X)_*\pi_1(\widetilde X)=0.
\]
This subgroup is contained in
\[
(p_Y)_*\pi_1(\widetilde Y)=0.
\]
The covering-space lifting criterion therefore gives a lift after choosing compatible basepoints.
:::

<1>2. Similarly, $g\circ p_Y$ lifts to a map
\[
\widetilde g:\widetilde Y\to\widetilde X.
\]
::: {.proof}
The same lifting criterion applies because $\widetilde Y$ is simply connected.
:::

<1>3. The composite $\widetilde g\widetilde f$ is homotopic to $\operatorname{id}_{\widetilde X}$.
::: {.proof}
Let
\[
H:X\times I\to X
\]
be a homotopy from $g f$ to $\operatorname{id}_X$.
Then
\[
H\circ(p_X\times\operatorname{id}_I):\widetilde X\times I\to X
\]
is a homotopy from
\[
g f p_X=p_X\widetilde g\widetilde f
\]
to $p_X$.

By the homotopy lifting property of the covering $p_X$, lift this homotopy starting at the map $\widetilde g\widetilde f$.
Its terminal map $u:\widetilde X\to\widetilde X$ satisfies
\[
p_Xu=p_X.
\]
Choose the lifts $\widetilde f,\widetilde g$ and the lifted homotopy so that one chosen basepoint is fixed at the terminal time.
Then $u$ and $\operatorname{id}_{\widetilde X}$ are two lifts of $p_X$ agreeing at that basepoint.
Uniqueness of lifts gives
\[
u=\operatorname{id}_{\widetilde X}.
\]
Hence
\[
\widetilde g\widetilde f\simeq\operatorname{id}_{\widetilde X}.
\]
:::

<1>4. Likewise,
\[
\widetilde f\widetilde g\simeq\operatorname{id}_{\widetilde Y}.
\]
::: {.proof}
Apply the same argument to a homotopy
\[
f g\simeq\operatorname{id}_Y
\]
and the covering $p_Y$.
:::

<1>5. Therefore
\[
\boxed{\widetilde X\simeq\widetilde Y.}
\]
::: {.proof}
The maps $\widetilde f$ and $\widetilde g$ are homotopy inverses by <1>3--<1>4.
:::
:::
