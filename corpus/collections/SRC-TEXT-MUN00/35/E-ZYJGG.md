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
    extension property through an imbedding in a cube (Theorem 34.3, Tychonoff), a
    retraction of the cube, and coordinatewise Tietze extension. The argument is the card's
    own; no retained set is cited. Munkres §35 Exercise 6, printed p. 223. The printed
    statement needed no repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Source line repaired: the exercise checked against is Section 35 Exercise 6 of Munkres
    (parts (a) and (b), part (b) hypothesising that Y is compact), not Exercise 2, as the
    earlier note on this card said. The proof is unchanged and does prove exactly parts (a)
    and (b).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Review repair, three findings, all confirmed against the book: the exercise is on
    printed p. 223 (PDF p. 238, where Exercises 1 through 6 of Section 35 appear, item 6
    with the compactness hypothesis in part (b)), not p. 224, which begins with Figure 35.2
    and item 7(b); the cube characterization of complete regularity used for the imbedding
    is Theorem 34.3, not Theorem 34.2, which is the imbedding theorem for a separating
    family of functions; and the closing step claimed an equivalence, which the compactness
    hypothesis of (b) does not support. The closing step now says that parts (a) and (b) are
    what is proved and that the unrestricted converse is starred Exercise 35.8 of the same
    page set, proved on E-Z964O.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The reviewer finding of 2026-11-18 14:52Z, routed to this card, is verified closed, on the
    card and against the book. Re-read in the retained Munkres PDF: printed p. 223 (PDF p. 238)
    carries Section 35 Exercises 5 and 6, item 6 being the absolute-retract exercise with the
    compactness hypothesis in part (b), so the card's "printed p. 223" is right; printed p. 224
    (PDF p. 239) carries Exercise 7(b) and the starred Exercise 8, which states as a Theorem that
    a normal space is an absolute retract if and only if it has the universal extension property,
    with the adjunction-space hint — so the card's closing step is right to restrict itself to (a)
    and (b) and to name the unrestricted converse as the starred Exercise 35.8 of p. 224. The
    cube characterization of complete regularity used for the imbedding is Theorem 34.3, which is
    what the card cites. No change to the solution was needed.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The solution section said "the argument is the card's own; no retained solution set is cited",
    contradicting the card's own solution-written event of 2026-11-10, which records part (b) as
    transcribed from Möller's S35 set, Exercise 35.6, page 2 of the file, and records the one place
    the card departs from it (Möller's citation of Exercise 31.5 for the retract step, replaced by
    Exercise 35.5(b)). The retained file was re-read and does contain Ex. 35.6. The solution section
    now names the set, which part is transcribed and which is the card's, and the departure. The
    2026-11-18 note above is left as written; this event is the correction.
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
Part (b) is transcribed from the retained solution of Jesper Michael Moller, *Solutions to exercises in Munkres*, file S35.pdf, Exercise 35.6, page 2 of the file (`tmp/sources/munkres-solutions-poulsen-S35.pdf`, Internet Archive snapshot 20220130234235); part (a) is the card's, since a homeomorphism from the closed copy $Y_0$ extends to $Z$ and postcomposition with its inverse retracts $Z$ onto $Y_0$. It is checked against Munkres, Topology (2000), §35 Exercise 6, printed p. 223, with the Tietze theorem (§35), the Tychonoff theorem (§37) and Theorem 32.3. Where the card departs from Moller: he cites Exercise 31.5 for the retract step, which is the equalizer exercise, and the card cites Exercise 35.5(b) instead.

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
$Y$ is compact Hausdorff, hence normal (Theorem 32.3), hence completely regular (§33), so there is an imbedding $e:Y\to[0,1]^{J}$ for some set $J$ (Theorem 34.3, the cube characterization of complete regularity). The cube is compact by the Tychonoff theorem and Hausdorff, so the compact set $e(Y)$ is closed in it (Theorem 26.3).
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
Parts (a) and (b) hold, and only those two implications are proved here.

::: pf-proof
Step [](#a){.pf-ref} proves (a) for every normal $Y$, and step [](#b){.pf-ref} proves (b) for a compact absolute retract $Y$. These are the two assertions of the exercise. They are not the two halves of an equivalence for an arbitrary normal $Y$: the converse of (a) without the compactness hypothesis is the starred Exercise 35.8, printed p. 224, and is proved on [[E-Z964O]] by the adjunction-space argument, not here.
:::

:::

:::
:::
