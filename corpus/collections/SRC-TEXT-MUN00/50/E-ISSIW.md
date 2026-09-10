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
---

::: {.exercise}

Show that $\mathbb{R} \times \mathbb{R}$ in the dictionary order topology is locally 1-euclidean and satisfies (iii) but not (ii) of Exercise 2.
:::

::: {.solution}
Let \(X=\mathbb R\times\mathbb R\) with the dictionary order. For \((a,b)\in X\), the order interval
\[
((a,b-1),(a,b+1))
\]
is exactly \(\{a\}\times(b-1,b+1)\), and projection onto the second coordinate is an order-preserving homeomorphism with \((b-1,b+1)\). Thus \(X\) is locally \(1\)-euclidean.

Section 20 shows that the dictionary-order plane is metrizable, so it satisfies condition (iii).

It does not satisfy condition (ii). Indeed the sets
\[
U_a=\{a\}\times(0,1)\qquad(a\in\mathbb R)
\]
form an uncountable family of pairwise disjoint nonempty open subsets. A second-countable space cannot have such a family: each member would contain a distinct element of a fixed countable basis. Hence \(X\) is not second-countable, so it is not a \(1\)-manifold. Thus it satisfies (iii) but not (ii).
:::
