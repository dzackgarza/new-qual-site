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
---

::: {.exercise}

Let $p: E \to B$ be a covering map, with $E$ path connected.
Show that if $B$ is simply connected, then $p$ is a homeomorphism.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §54 Exercise 4, printed p. 341, with the homotopy lifting theorem (§54) and the lifting correspondence.

::: pf

::: {.pf-step #transitive}
Every fibre of $p$ is a single point.

::: pf-proof
Fix $e_{0}\in E$ and put $b_{0}=p(e_{0})$; let $e_{1}\in p^{-1}(\{b_{0}\})$. Since $E$ is path connected there is a path $\widetilde\alpha$ in $E$ from $e_{0}$ to $e_{1}$, and $\alpha=p\circ\widetilde\alpha$ is a loop in $B$ at $b_{0}$. Because $B$ is simply connected, $\alpha$ is path homotopic to the constant loop at $b_{0}$. The constant loop at $b_{0}$ lifts, from the point $e_{0}$, to the constant path at $e_{0}$, while $\widetilde\alpha$ is the lift of $\alpha$ from $e_{0}$; by the homotopy lifting theorem, lifts of path homotopic paths that start at the same point have the same terminal point (Munkres §54). Hence $e_{1}=e_{0}$ and $p^{-1}(\{b_{0}\})=\{e_{0}\}$. The same argument applies with $e_{0}$ replaced by any point of $E$, so every fibre is a single point.
:::

:::

::: {.pf-step #bijective}
$p$ is bijective.

::: pf-proof
$p$ is surjective, being a covering map. It is injective, since two points with the same image lie in a common fibre, which step [](#transitive){.pf-ref} shows to be a single point.
:::

:::

::: {.pf-step #homeomorphism}
$p$ is a homeomorphism.

::: pf-proof
A covering map is a local homeomorphism, hence an open map: every point of $E$ has a neighbourhood mapped homeomorphically onto an open set of $B$, so the image of any open set of $E$ is a union of open sets of $B$. Thus $p$ is a continuous open bijection, and its set-theoretic inverse is continuous; so $p$ is a homeomorphism.
:::

:::

:::
:::
