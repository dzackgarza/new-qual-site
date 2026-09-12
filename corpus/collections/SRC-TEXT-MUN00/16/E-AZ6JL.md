---
schema: qual/card@1
id: E-AZ6JL
kind: problem
title: Three topologies on the unit square
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $I = [0, 1]$.
Compare the product topology on $I \times I$, the dictionary order topology on $I \times I$, and the topology $I \times I$ inherits as a subspace of $\mathbb{R} \times \mathbb{R}$ in the dictionary order topology.
:::

::: {.solution}
Let $\mathcal P$ be the product topology on $I^2$, $\mathcal D$ the dictionary order topology on $I^2$, and $\mathcal S$ the topology inherited from the dictionary order topology on $\mathbb R^2$.

The product and dictionary-order topologies are incomparable. The set
\[
I\times(1/2,1]
\]
is product-open (since $(1/2,1]$ is open in the subspace $I$), but it is not dictionary-order open at $(0,1)$: every dictionary-order neighborhood of $(0,1)$ contains points whose first coordinate is positive. Conversely,
\[
\{0\}\times(0,1)
\]
is dictionary-order open, but is not product-open.

The subspace topology $\mathcal S$ is finer than the product topology because, by the preceding exercise, the ambient dictionary topology on $\mathbb R^2$ is $\mathbb R_d\times\mathbb R$; restricting to $I^2$ gives the product of discrete $I$ in the first coordinate with the usual subspace topology in the second, which contains the ordinary product topology.

It is also finer than the dictionary order topology $\mathcal D$: the order topology induced on a subset by the restricted order is always contained in the topology inherited from the ambient order topology. Both inclusions are strict. Strictness over $\mathcal P$ follows from the open set $\{0\}\times(0,1)$. Strictness over $\mathcal D$ follows, for example, from
\[
\{1/2\}\times(1/2,1],
\]
which is open in $\mathcal S$ but not in the dictionary order topology on the ordered square. Hence
\[
\mathcal P\not\subseteq\mathcal D,\qquad
\mathcal D\not\subseteq\mathcal P,
\qquad
\mathcal P,\mathcal D\subsetneq\mathcal S.
\]
:::
