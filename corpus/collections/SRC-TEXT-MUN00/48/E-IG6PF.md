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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the shrinking step the two
    constructions use and the card only asserted: in the product topology a point of an open set
    has a basic neighbourhood whose closure, a product of finitely many closed intervals and R
    elsewhere, still lies in it, which is what makes the recursion possible without invoking
    regularity of R^J as a theorem. The coordinatewise assembly is now its own step, with the
    nested-interval argument recorded for restricted coordinates and the free choice for
    unrestricted ones. In the box topology the diameter 1/n shrinking is now attached to
    completeness of R coordinate by coordinate. The uniform case is split into completeness of the
    uniform metric and the Baire theorem applied to it. What was not checked: the printed page of
    Theorem 43.5, which the card's earlier note cites without one; the citation now names the
    theorem and says its page is not recorded here. The exercise page, 300, and Theorem 48.2 on
    printed p. 296 are as the card and the §48 cards beside it record.
---

::: {.exercise}

Show that $\RR^J$ is a Baire space in the box, product, and uniform topologies.
:::

::: {.solution}
The argument is the card's own: no published solution set is transcribed. Math StackExchange 2344060 states this exercise and proves it through Frolík's countably complete spaces, resting on two theorems of a paper the card does not cite, so it is recorded in the audit and not used here. The book's §48 Exercise 12 is printed on p. 300, and the numbered results cited are Theorem 48.2, that a complete metric space is Baire, and Theorem 43.5 of §43, the completeness of the uniform metric on the function space, whose page is not recorded here.

::: pf

::: {.pf-step #shrinking}
Given a nonempty open set $V$ and a point $x\in V$, there is a basic open set $U$ with $x\in U\subset\overline{U}\subset V$ whose closure in $\RR^{J}$ is a product of closed intervals, restricted in finitely many coordinates.

::: pf-proof
Write $V=\bigcup_{k}V_{k}$ with $V_{k}$ basic open, and pick $k$ with $x\in V_{k}$. Then $V_{k}=\prod_{j}W_{j}$, where each $W_{j}$ is an open interval of $\RR$ or all of $\RR$, and $W_{j}=\RR$ for all but finitely many $j$. For each of the finitely many other $j$ choose a closed interval $[a_{j},b_{j}]$ with $x_{j}\in[a_{j},b_{j}]\subset W_{j}$, which is possible because $W_{j}$ is an open interval containing $x_{j}$; set $[a_{j},b_{j}]=\RR$ in the remaining coordinates. Then $U=\prod_{j}(a_{j},b_{j})$ is a basic open set containing $x$, and $\overline{U}=\prod_{j}[a_{j},b_{j}]$ is a closed subset of $V_{k}\subset V$: a product of closed sets is closed in the product topology, and each factor lies in $W_{j}$.
:::
:::

::: {.pf-step #product-recursion}
Let $G_{1},G_{2},\ldots$ be dense open subsets of $\RR^{J}$ with the product topology and $U_{0}$ a nonempty basic open set. There are nonempty basic open sets $U_{1},U_{2},\ldots$ with $\overline{U_{n}}\subset U_{n-1}\cap G_{n}$ for every $n$, each $U_{n}$ obtained from $U_{n-1}$ by restricting finitely many further coordinates to bounded open intervals.

::: pf-proof
Inductively, $U_{n-1}\cap G_{n}$ is nonempty and open: $G_{n}$ is dense, so it meets the nonempty open set $U_{n-1}$. Pick a point of it and apply step [](#shrinking){.pf-ref} inside $U_{n-1}\cap G_{n}$, taking as the finitely many coordinates to restrict those already restricted in $U_{n-1}$ together with those the new basic set restricts; the resulting $U_{n}$ is contained in $U_{n-1}$, so a coordinate restricted at an earlier stage stays restricted, with its interval nested in the earlier one.
:::
:::

::: {.pf-step #product-point}
There is a point $x\in U_{0}\cap\bigcap_{n}G_{n}$.

::: pf-proof
For each coordinate $j$ let $I_{n,j}$ be the closure of the projection of $U_{n}$ to the $j$-th coordinate, so that $\overline{U_{n}}=\prod_{j}I_{n,j}$. If $j$ is restricted at some stage $n_{0}$, then $I_{n_{0},j}$ is a closed bounded interval, the intervals $I_{n,j}$ for $n\geq n_{0}$ are closed, bounded and nested inside it, so their intersection is nonempty by compactness of $I_{n_{0},j}$, and the intervals for $n<n_{0}$ contain $I_{n_{0},j}$ because the $U_{n}$ decrease with $n$; choose $x_{j}$ in the intersection over all $n$. If $j$ is never restricted, every $I_{n,j}$ is $\RR$ and any real number will do. The point $x=(x_{j})$ then lies in $\overline{U_{n}}$ for every $n$, hence in $U_{n-1}\cap G_{n}$ for every $n\geq1$, hence in $U_{0}\cap\bigcap_{n}G_{n}$.
:::
:::

::: {.pf-step #product-baire}
$\RR^{J}$ is a Baire space in the product topology.

::: pf-proof
A nonempty open set $U_{0}$ meets $\bigcap_{n}G_{n}$ by step [](#product-point){.pf-ref}, so $\bigcap_{n}G_{n}$ is dense; that is the defining property of a Baire space.
:::
:::

::: {.pf-step #box-baire}
$\RR^{J}$ is a Baire space in the box topology.

::: pf-proof
Let $G_{1},G_{2},\ldots$ be dense open and $U_{0}$ nonempty open in the box topology, which is finer, so $U_{0}$ contains a box-basic set. Recursively choose nonempty box-basic $U_{n}=\prod_{j}(a_{n,j},b_{n,j})$ with $\overline{U_{n}}\subset U_{n-1}\cap G_{n}$ and $b_{n,j}-a_{n,j}<1/n$ for every $j$: step [](#shrinking){.pf-ref} applies in every coordinate at once, since a box-basic open set restricts all of them. For each $j$ the intervals $[a_{n,j},b_{n,j}]$ are closed, nested and of diameter tending to $0$, so $\bigcap_{n}[a_{n,j},b_{n,j}]$ is a single point $x_{j}$ by completeness of $\RR$. Then $x\in\overline{U_{n}}$ for every $n$, so $x\in U_{0}\cap\bigcap_{n}G_{n}$, and $\bigcap_{n}G_{n}$ is dense.
:::
:::

::: {.pf-step #uniform-complete}
$\RR^{J}$ is complete in the uniform metric $\bar\rho(x,y)=\sup_{j\in J}\min\{\abs{x_{j}-y_{j}},1\}$.

::: pf-proof
Let $(x^{k})$ be $\bar\rho$-Cauchy. For each $j$ one has $\min\{\abs{x^{k}_{j}-x^{l}_{j}},1\}\leq\bar\rho(x^{k},x^{l})$, so the coordinate sequence is Cauchy in $\RR$ and converges to some $x_{j}$. Given $\varepsilon\in(0,1)$ choose $K$ with $\bar\rho(x^{k},x^{l})<\varepsilon/2$ for $k,l\geq K$; then for $k\geq K$ and every $j$, $\abs{x^{k}_{j}-x_{j}}=\lim_{l}\abs{x^{k}_{j}-x^{l}_{j}}\leq\varepsilon/2$, so $\bar\rho(x^{k},x)<\varepsilon$ and $x^{k}\to x$.
:::
:::

::: {.pf-step #uniform-baire}
$\RR^{J}$ is a Baire space in the uniform topology.

::: pf-proof
The uniform topology is the topology of the complete metric $\bar\rho$ by step [](#uniform-complete){.pf-ref}, and a complete metric space is a Baire space (Theorem 48.2).
:::
:::

::: {.pf-step #conclusion}
$\RR^{J}$ is a Baire space in the box, product and uniform topologies.

::: pf-proof
Steps [](#product-baire){.pf-ref}, [](#box-baire){.pf-ref} and [](#uniform-baire){.pf-ref} are the three cases.
:::
:::
:::

:::
