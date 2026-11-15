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
    pp. 316--317). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub
    repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by
    Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with
    its formulas lost. The Stack Exchange query "dictionary order plane not second countable" returned nothing.
    The card's two claims are its own: the interval $((a,b-1),(a,b+1))$ of the dictionary order is the vertical
    segment $\theset{a}\times(b-1,b+1)$, which makes the space locally $1$-euclidean, and the uncountably many
    pairwise disjoint open sets $\theset{a}\times(0,1)$ defeat second countability, which is what condition
    (ii) of Exercise 2 requires. Nothing needed correction.
---

::: {.exercise}

Show that $\RR \times \RR$ in the dictionary order topology is locally 1-euclidean and satisfies (iii) but not (ii) of Exercise 2.
:::

::: {.solution}
Let $X=\RR\times\RR$ with the dictionary order. For $(a,b)\in X$, the order interval
$$
((a,b-1),(a,b+1))
$$
is exactly $\{a\}\times(b-1,b+1)$, and projection onto the second coordinate is an order-preserving homeomorphism with $(b-1,b+1)$. Thus $X$ is locally $1$-euclidean.

The dictionary-order plane is metrizable by [[E-KY2W7]], so it satisfies condition (iii) of [[E-OYPV7]].

It does not satisfy condition (ii). Indeed the sets
$$
U_a=\{a\}\times(0,1)\qquad(a\in\RR)
$$
form an uncountable family of pairwise disjoint nonempty open subsets. A second-countable space cannot have such a family: each member would contain a distinct element of a fixed countable basis. Hence $X$ is not second-countable, so it is not a $1$-manifold. Thus it satisfies (iii) but not (ii).
:::
