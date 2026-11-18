---
schema: qual/card@1
id: E-ISSIW
kind: problem
title: The dictionary order plane is locally euclidean and metrizable but not a manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Order Topology
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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 4 of §50, printed p. 317, with the order
    topology of a product of two ordered sets (§14) and Theorem 30.2. Locally 1-euclidean: the interval between
    (a,b-1) and (a,b+1) is exactly the fibre {a} x (b-1,b+1), on which the order is the usual one of R. Not a
    manifold: the fibres {a} x (0,1) are pairwise disjoint nonempty open sets, and a second countable space has
    only countably many pairwise disjoint nonempty open sets, since each contains a point of a fixed countable
    basis. Metrizability is cited from the card of §24 Exercise 6, where the dictionary order plane is shown to
    be metrizable (the space is the topological sum of continuum many copies of R). Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats supplementary Exercise 4 of §50 (printed
    p. 317). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub
    repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by
    Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with
    its formulas lost. The Stack Exchange query "dictionary order plane not second countable" returned nothing.
    The card's two claims are its own: the interval $((a,b-1),(a,b+1))$ of the dictionary order is the vertical
    segment $\theset{a}\times(b-1,b+1)$, which makes the space locally $1$-euclidean, and the uncountably many
    pairwise disjoint open sets $\theset{a}\times(0,1)$ defeat second countability, which is what condition
    (ii) of Exercise 2 requires. Nothing needed correction.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the card against the printed exercise (the
    Supplementary Exercises on locally euclidean spaces, Exercise 4) and the conditions of
    Exercise 2 there: the interval ((a,b-1),(a,b+1)) computed to be the slice {a} x
    (b-1,b+1), the projection to the second coordinate shown to be a homeomorphism onto that
    slice, metrizability through the identification with R_d x R (Section 16 Exercise 9,
    card E-KY2W7), and the uncountable family of disjoint basis elements {a} x (0,1)
    excluding a countable basis, so that the space is not a 1-manifold while being
    metrizable. Both wikilinks resolve to cards with the stated content. The argument is the
    card's own; no retained set covers this exercise. No repair needed.
---

::: {.exercise}

Show that $\RR \times \RR$ in the dictionary order topology is locally 1-euclidean and satisfies (iii) but not (ii) of Exercise 2.
:::

::: {.solution}
The argument is the card's own; no retained solution set covers this supplementary exercise, and the two results it leans on are cards of this corpus: the metrizability of the dictionary-order plane is [[E-KY2W7]], and the conditions (i)--(v) are those of [[E-OYPV7]], both from the Supplementary Exercises on locally euclidean spaces. Here (ii) is "is an $m$-manifold" and (iii) is "is metrizable"; the exercise asks for a space that is locally $1$-euclidean, satisfies (iii), and does not satisfy (ii).

Let $X=\RR\times\RR$ carry the dictionary order topology, whose basis is the collection of open intervals $\big((a,b),(c,d)\big)$.

::: pf

::: {.pf-step #slice}
For $(a,b)\in X$ the open interval $\big((a,b-1),(a,b+1)\big)$ is a neighbourhood of $(a,b)$ equal to the slice $\{a\}\times(b-1,b+1)$.

::: pf-proof
In the dictionary order a point $(x,y)$ satisfies $(a,b-1)<(x,y)<(a,b+1)$ exactly when $x=a$ and $b-1<y<b+1$: if $x=a$ this is immediate from the definition of the dictionary order, and if $x\ne a$ then $(x,y)$ lies below both or above both of the two points. The interval is a basis element, hence open, and it contains $(a,b)$ because $b-1<b<b+1$.
:::

:::

::: {.pf-step #euclidean}
$X$ is locally $1$-euclidean.

::: pf-proof
Let $(a,b)\in X$. The map $y\mapsto(a,y)$ of $(b-1,b+1)$ onto the subspace $\{a\}\times(b-1,b+1)$ is a bijection, and it carries the basis element $(c,d)$ of $(b-1,b+1)$ to $\{a\}\times(c,d)=\big((a,c),(a,d)\big)$, a basis element of $X$; so it is a homeomorphism onto that subspace. By step [](#slice){.pf-ref} the subspace is a neighbourhood of $(a,b)$, so each point of $X$ has a neighbourhood homeomorphic to an open subset of $\RR^{1}$, which is the definition of locally $1$-euclidean.
:::

:::

::: {.pf-step #metrizable}
$X$ satisfies (iii): it is metrizable.

::: pf-proof
The dictionary order topology on $\RR\times\RR$ is the product topology $\RR_{d}\times\RR$, with $\RR_{d}$ the discrete line (Munkres §16 Exercise 9), and $\RR_{d}\times\RR$ is metrizable: the discrete metric induces the topology of $\RR_{d}$, the usual metric that of $\RR$, and $\rho\big((x,y),(w,z)\big)=\max\{d(x,w),\abs{y-z}\}$ is a metric inducing the product topology. This is [[E-KY2W7]].
:::

:::

::: {.pf-step #not-second-countable}
$X$ is not second countable.

::: pf-proof
For each $a\in\RR$ the set $U_{a}=\{a\}\times(0,1)=\big((a,0),(a,1)\big)$ is a basis element of $X$, hence a nonempty open set, and $U_{a}\cap U_{a'}=\varnothing$ for $a\ne a'$. If $\mathcal{B}$ were a countable basis, then each $U_{a}$ would contain a member of $\mathcal{B}$, and distinct $U_{a}$ would contain distinct members, since they are disjoint; that would inject the uncountable set $\RR$ into $\mathcal{B}$, which is impossible.
:::

:::

::: {.pf-step #not-manifold}
$X$ does not satisfy (ii): it is not a $1$-manifold.

::: pf-proof
A $1$-manifold is a Hausdorff locally $1$-euclidean space with a countable basis, and step [](#not-second-countable){.pf-ref} shows that $X$ has no countable basis. So $X$ fails (ii) while satisfying (iii) by step [](#metrizable){.pf-ref}; by [[E-OYPV7]] the implication (ii) $\Rightarrow$ (iii) holds, so this is the failure of its converse.
:::

:::

::: {.pf-step}
$X$ is locally $1$-euclidean, satisfies (iii), and does not satisfy (ii).

::: pf-proof
Steps [](#euclidean){.pf-ref}, [](#metrizable){.pf-ref} and [](#not-manifold){.pf-ref} are the three assertions.
:::

:::

:::
:::
