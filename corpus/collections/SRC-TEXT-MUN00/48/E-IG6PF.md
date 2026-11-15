---
schema: qual/card@1
id: E-IG6PF
kind: problem
title: Powers of the line are Baire spaces in the box, product, and uniform topologies
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 12 (printed p. 300) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: in the product
    topology the standard nested-basic-open construction works because a basic open set restricts finitely many
    coordinates, each coordinate sequence of closed intervals is nested and eventually constant, and the point
    assembled coordinatewise lies in every closure, hence in every G_n; in the box topology the same
    construction shrinks every coordinate with diameter below 1/n, so each coordinate intersection is a single
    point and the point lies in every closure; in the uniform topology R^J is complete in the uniform metric by
    Theorem 43.5 and so Baire by Theorem 48.2, which is the exercise's point that the box and product topologies
    need a different argument. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 2344060, "The arbitrary product of Reals is
    Baire" (2017-07-02), asks this exercise and has two answers, the text kept at
    tmp/sources/mse-2344060-munkres-48-12.md. The accepted answer, by Henno Brandsma (2017-07-03), proves it
    through Frolík's countably complete spaces: a space is countably complete when it has a sequence of bases
    such that a nested family of closures of sets taken from them has a point in common, such a space is Baire
    by the argument of Theorem 48.2, $\RR$ is countably complete for the bases of intervals of diameter at most
    $1/n$, and the theorems 2.10 and 2.12 of that paper carry countable completeness to arbitrary products in
    both the product and the box topology. That is a correct proof, but it rests on two theorems of a paper the
    card does not cite, so it is not transcribed. The other answer, by Petra Axolotl (2023-11-02), says that the
    proof of Theorem 48.2 "simply goes through" and that it needs regularity and the non-emptiness of a nested
    sequence of closures of basis elements $\prod_\alpha(a_\alpha,b_\alpha)$; that is true, and near the end of
    this pass the claim was misread as failing in the product topology, so that the sentence recorded it as
    failing; the event of the same date below corrects that reading. The card's coordinatewise construction is
    what supplies the non-emptiness: the coordinates are restricted one finite
    set at a time, so each coordinate is either never restricted, where any value lies in every projection, or
    restricted from some stage on, where the closed bounded intervals are nested from then on, and in both cases
    the assembled point lies in every closure. The post by Yougi, *Munkres Topology Solution: Chapter 8*
    (2025-07-10, https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/), answers the exercise
    at its Ex. 48.12 with one line for the uniform topology and "the same applies to box topology" for the
    other two, which is a gap.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The note above had said that Petra Axolotl's claim that the proof of Theorem 48.2
    "simply goes through" fails in the product topology, because there the closure of a basic open set is
    $\RR$ in all but finitely many coordinates and so is not compact. That objection is wrong: what the
    argument needs of a nested family of closures of basic open sets is a common point, not compactness, and in
    the product topology the family has one, because a coordinate once restricted stays restricted — a basic
    open set is a bounded open interval in finitely many coordinates and $\RR$ in the others, and
    $U_n\subseteq U_{n-1}$ forces the projection at a coordinate already restricted to lie inside the interval
    chosen there — so at such a coordinate the closed bounded intervals are nested and meet, while a coordinate
    never restricted admits every value. The product case of the solution now states the restricted-coordinate
    fact it uses. Nothing else on the card changed, and the other answer's Frolik-based proof still is not
    transcribed.
---

::: {.exercise}

Show that $\RR^J$ is a Baire space in the box, product, and uniform topologies.
:::

::: {.solution}
For the product topology, let $G_1, G_2, \ldots$ be dense open sets and $U_0$ a nonempty basic open set. Recursively choose nonempty basic opens $U_n$ with
$$
\overline{U_n}\subset U_{n-1}\cap G_n,
$$
changing only finitely many coordinates at stage $n$ and choosing closed bounded coordinate intervals there. A coordinate once restricted stays restricted from then on: $U_n$ is contained in $U_{n-1}$, so at a coordinate where $U_{n-1}$ is a bounded interval the projection of $U_n$ lies inside that interval. In a coordinate that is ever restricted, the closure of the first interval chosen there is compact, and all later closed intervals are nested inside it, so their intersection is nonempty. Choose any real number in every coordinate never restricted. The resulting point lies in $U_0\cap\bigcap G_n$.

For the box topology, perform the same construction coordinatewise, now shrinking every coordinate interval at stage $n$ and arranging diameter $<1/n$. Completeness of $\RR$ gives a point in every coordinate intersection, hence a point of $U_0\cap\bigcap G_n$.

For the uniform topology, the uniform metric
$$
\bar\rho(x,y)=\sup_{j\in J}\min\{\abs{x_j-y_j},1\}
$$
is complete: a Cauchy sequence is uniformly Cauchy in every coordinate, has coordinatewise limits, and the same uniform estimate gives convergence in $\bar\rho$. Hence the uniform topology is Baire by the complete-metric Baire theorem.

Thus $\RR^J$ is Baire in all three topologies.
:::
