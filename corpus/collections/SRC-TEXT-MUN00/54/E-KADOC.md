---
schema: qual/card@1
id: E-KADOC
kind: problem
title: Coverings over simply connected bases are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 54: Problem 8 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-8-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-8-solution.txt), and against Munkres,
    Topology (2000), Section 54 Exercise 8, printed p. 348. dbFin's route is Theorem 54.4, whose lifting correspondence is surjective onto the fibre because $E$ is path connected, so the fibre over $b$ has one point; the card's route is the homotopy lifting theorem directly: a path in $E$ from $e_0$ to another point of the fibre projects to a loop that is nullhomotopic, and the nullhomotopy lifts with the constant loop at $e_0$ on the other side. Both are correct. Nothing needed repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the homotopy lifting theorem forces one
    point in a fibre over a simply connected base, that a covering map is therefore
    bijective and open, and hence a homeomorphism. The argument is the card's own; no
    retained set is cited. Munkres §54 Exercise 4, printed p. 341. The printed statement
    needed no repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Three corrections on 2026-11-19. The rendered preamble said "The argument is
    the card's own; no retained solution set is cited on the card", which is
    false, since the event of 2026-11-11 cites dbFin's Section 54 Problem 8
    solution; it gave the exercise as "§54 Exercise 4, printed p. 341", as the
    event of 2026-11-18 does, where the exercise is Exercise 8 on printed p. 348
    (PDF p. 363, folio 348, printed page = PDF page - 15), and printed p. 341 is
    the exercise page of §53; and its proof was the card's own route through the
    homotopy lifting lemma. The solution is now dbFin's route, transcribed:
    Theorem 54.4 makes the lifting correspondence onto the fibre a bijection, so
    the fibre over a point of a simply connected base is a single point,
    Exercise 3 of §53 spreads that to every fibre, and an open bijection is a
    homeomorphism. Cited with pages: Theorem 54.4 on printed p. 345 (PDF p. 360),
    Exercise 3 of §53 on printed p. 341 (PDF p. 356), and the exercise on printed
    p. 348. The events of 2026-11-11 and 2026-11-18 are left as written; the
    second's "Exercise 4, printed p. 341" is superseded by this one. The
    statement of the exercise is unchanged.

---

::: {.exercise}

Let $p: E \to B$ be a covering map, with $E$ path connected.
Show that if $B$ is simply connected, then $p$ is a homeomorphism.
:::

::: {.solution}
The argument is that of the published solution of dbFin, "Section 54: Problem 8 Solution": Theorem 54.4 makes the lifting correspondence a bijection onto the fibre, so the fibre over a point of a simply connected base has one element, and a covering map that is an open bijection is a homeomorphism. The exercise is Munkres, *Topology* (2000), Section 54, Exercise 8, printed p. 348; Theorem 54.4 is on printed p. 345, and Exercise 3 of §53, which makes the fibre cardinality the same over every point of a connected base, is on printed p. 341.

::: pf

::: {.pf-step #fibre}
For every $b\in B$ the fibre $p^{-1}(b)$ has exactly one point.

::: pf-proof
Fix $e_0\in E$ and put $b_0=p(e_0)$. Since $E$ is path connected, the lifting correspondence $\phi\colon\pi_1(B,b_0)\to p^{-1}(b_0)$ is surjective (Theorem 54.4, printed p. 345); since $B$ is simply connected, $\pi_1(B,b_0)$ is the trivial group, so $\phi$ takes a single value and $p^{-1}(b_0)=\{e_0\}$. The base $B$ is path connected, being simply connected, so Exercise 3 of §53, printed p. 341, gives the same cardinality over every point of $B$; every fibre is a single point.
:::

:::

::: {.pf-step #bijective}
$p$ is a bijection.

::: pf-proof
$p$ is surjective, being a covering map, and injective by step [](#fibre){.pf-ref}, since two points with the same image lie in one fibre.
:::

:::

::: {.pf-step #open}
$p$ is an open map.

::: pf-proof
A covering map is a local homeomorphism: each point of $E$ has an open neighbourhood carried homeomorphically onto an open set of $B$. The image of an open set of $E$ is therefore a union of open sets of $B$, hence open.
:::

:::

::: {.pf-step #homeomorphism}
$p$ is a homeomorphism.

::: pf-proof
By steps [](#bijective){.pf-ref} and [](#open){.pf-ref} it is a continuous open bijection. The inverse of such a map is continuous, because the preimage of an open set under the inverse is its image under $p$, which is open; so $p$ is a homeomorphism.
:::

:::

:::

:::
