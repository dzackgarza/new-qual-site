---
schema: qual/card@1
id: E-ZYJGG
kind: problem
title: Absolute retracts
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.6, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235),
    checked against Munkres, Topology (2000), Section 35 Exercise 6, printed p. 223, its hint, Theorem
    34.2, Theorem 37.3 and Theorem 35.1. Part (a) is the card's: a homeomorphism from the closed copy
    Y_0 extends to Z and postcomposition with its inverse retracts Z onto Y_0. Part (b) is Moller's:
    a compact Hausdorff space imbeds as a closed subspace of the cube [0,1]^J, the cube has the
    universal extension property with the Tychonoff theorem assumed, and by (a) and Exercise 35.5(b)
    a retract of it does too. What was corrected: Moller writes that the space "is a retract of the
    UEP space [0,1]^J, hence is itself a UEP space [Ex 31.5.(b)]", citing Exercise 31.5, which is
    about the equalizer of two maps; the retract argument is Exercise 35.5(b), and the card cites it.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the universal extension property retracts
    a normal space onto any closed copy of Y, and that a compact absolute retract has the
    extension property through an imbedding in a cube (Theorem 34.2, Tychonoff), a
    retraction of the cube, and coordinatewise Tietze extension. The argument is the card's
    own; no retained set is cited. Munkres §35 Exercise 6, printed p. 224. The printed
    statement needed no repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Source line repaired: the exercise checked against is Section 35 Exercise 6 of Munkres
    (parts (a) and (b), part (b) hypothesising that Y is compact), not Exercise 2, as the
    earlier note on this card said. The proof is unchanged and does prove exactly parts (a)
    and (b).
---

::: {.exercise}

Let $Y$ be a normal space.
Then $Y$ is said to be an absolute retract if for every pair of spaces $(Y_0, Z)$ such that $Z$ is normal and $Y_0$ is a closed subspace of $Z$ homeomorphic to $Y$, the space $Y_0$ is a retract of $Z$.

(a) Show that if $Y$ has the universal extension property, then $Y$ is an absolute retract.

(b) Show that if $Y$ is an absolute retract and $Y$ is compact, then $Y$ has the universal extension property.
[Hint: Assume the Tychonoff theorem, so you know $[0, 1]^J$ is normal.
Imbed $Y$ in $[0, 1]^J$.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §35 Exercise 6, printed p. 224, with the Tietze theorem (§35), the Tychonoff theorem (§37) and Theorem 32.3.

::: pf

::: {.pf-step #a}
(a) If $Y$ has the universal extension property, then $Y$ is an absolute retract.

::: pf-proof
Let $Y_{0}$ be a closed subspace of a normal space $Z$ and $h:Y_{0}\to Y$ a homeomorphism. By the universal extension property, applied to the closed subset $Y_{0}$ of the normal space $Z$ and the continuous map $h$, there is a continuous $H:Z\to Y$ with $H\restrict_{Y_{0}}=h$. Then $r=h^{-1}\circ H:Z\to Y_{0}$ is continuous, and for $y\in Y_{0}$ one has $r(y)=h^{-1}\big(h(y)\big)=y$; so $r$ is a retraction of $Z$ onto $Y_{0}$, which is the definition of $Y$ being an absolute retract.
:::

:::

::: {.pf-step #b}
(b) If $Y$ is compact and an absolute retract, then $Y$ has the universal extension property.

:::: pf-proof

::: {.pf-step #embedding}
$Y$ embeds in a cube and its image is closed there.

::: pf-proof
$Y$ is compact Hausdorff, hence normal (Theorem 32.3), hence completely regular (§33), so there is an imbedding $e:Y\to[0,1]^{J}$ for some set $J$ (Theorem 34.2, the imbedding theorem). The cube is compact by the Tychonoff theorem and Hausdorff, so the compact set $e(Y)$ is closed in it (Theorem 26.3).
:::

:::

::: {.pf-step #retraction}
There is a retraction $r:[0,1]^{J}\to e(Y)$.

::: pf-proof
The cube is compact Hausdorff, hence normal (Theorem 32.3). The set $e(Y)$ is a closed subspace of it and $Y$ is an absolute retract, so the homeomorphism $e:Y\to e(Y)$ extends to a retraction $r$ of the cube onto $e(Y)$.
:::

:::

::: {.pf-step #extension}
Let $A$ be closed in the normal space $X$ and $f:A\to Y$ continuous. Then $f$ extends to $X$.

::: pf-proof
Each coordinate of $e\circ f:A\to[0,1]^{J}$ is a continuous map into $[0,1]$, so by the Tietze theorem it extends to a continuous map $X\to[0,1]$; putting these together gives a continuous $F:X\to[0,1]^{J}$ with $F\restrict_{A}=e\circ f$ (continuity of $F$ from its coordinates, Theorem 18.4 and the definition of the product topology). Then $e^{-1}\circ r\circ F:X\to Y$ is continuous, and on $A$ it equals $e^{-1}\circ r\circ e\circ f=e^{-1}\circ e\circ f=f$.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Step [](#extension){.pf-ref} proves the universal extension property for $Y$: every continuous map on a closed subset of a normal space extends.
:::

:::

:::

:::

::: {.pf-step}
The equivalence holds.

::: pf-proof
Steps [](#a){.pf-ref} and [](#b){.pf-ref} are the two implications for a normal space $Y$.
:::

:::

:::
:::
