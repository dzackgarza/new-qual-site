---
schema: qual/card@1
id: E-KS2BT
kind: problem
title: Completeness of the compact convergence topology over $\sigma$-compact domains
classification:
  areas:
  - topology
  topics:
  - Function Spaces
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 10 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the definition of sigma-compactness
    given in the exercise, Theorem 43.5 and Theorem 43.6 (completeness of the uniform function space over a
    complete target), the metric for a countable product of metric spaces (§20, Exercise 20.3) and the
    description of compact convergence by Theorem 46.2. Part (a) is the standard countability argument: each
    point has a basis element inside an open set with compact closure, and only countably many basis elements
    occur. Part (b) is the exercise's hint carried out: take compact A_i with interiors covering X and closed
    under finite unions so that they increase; the sum of the bounded uniform metrics on the Y^{A_i}, weighted
    by 2^{-i}, induces compact convergence because every compact subset of X lies in some A_i (its interiors
    form a cover) and each A_i is compact; the restriction map is an isometry onto the closed compatibility
    subspace of the product, each factor is complete when Y is, the product metric is complete, and a closed
    subspace of a complete space is complete. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 431747, "Construct a metric for the
    topology of compact convergence on Y^X so that Y^X is complete when (Y,d) is complete and X is
    sigma-compact" (2013-06-28), is this exercise. Answer 432280 by Daniel Fischer builds the metric
    sup_n eps_n min{1, sup_{K_n} d(f,g)} on an exhaustion of X by compact sets, proves that it
    induces the topology of compact convergence in both directions and that its Cauchy sequences
    converge compactly, and answer 3353044 by tadejsv shows that a space sigma-compact in Munkres'
    sense is hemicompact, so that the exhaustion catches every compact set: with A_i the compact sets
    of the definition, K_n the union of the first n, every compact subset of X lies in some K_n
    because it is covered by finitely many interiors. The card's part (b) is the same construction by
    the exercise's hint, the embedding into the closed compatibility subspace of the product of the
    uniform spaces Y^{A_i}, and it uses that hemicompactness step; its part (a) is not in either
    answer. Nothing needed correction. The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter
    7 | Day 17" (2025-09-10, https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), also answers the exercise at its item 10 of
    §46 with its formulas lost; the queries of this pass are in the COMPLAINTS.md entry for
    §43--§50.
---

::: {.exercise}

A space is locally compact if it can be covered by open sets each of which is contained in a compact subspace of $X$.
It is said to be $\sigma$-compact if it can be covered by countably many such open sets.

(a) Show that if $X$ is locally compact and second-countable, it is $\sigma$-compact.

(b) Let $(Y, d)$ be a metric space.
Show that if $X$ is $\sigma$-compact, there is a metric for the topology of compact convergence on $Y^X$ such that if $(Y, d)$ is complete, $Y^X$ is complete in this metric.
[Hint: Let $A_1, A_2, \ldots$ be a countable collection of compact subspaces of $X$ whose interiors cover $X$. Let $Y_i$ denote the set of all functions from $A_i$ to $Y$, in the uniform topology. Define a homeomorphism of $Y^X$ with a closed subspace of the product space $Y_1 \times Y_2 \times \cdots$.]
:::

::: {.solution}
(a) Let $\mathcal B$ be a countable basis for the locally compact space $X$. For each $x$, choose an open $U_x$ and compact $K_x$ with $x\in U_x\subset K_x$. Choose a basis element $B_x$ with $x\in B_x\subset U_x$. Only countably many distinct $B_x$ occur; choosing one compact $K_x$ for each such basis element gives countably many compact sets whose interiors cover $X$. Thus $X$ is $\sigma$-compact.

(b) Choose compact $A_1,A_2,\dots$ whose interiors cover $X$, and replace them by finite unions so that $A_i\subset A_{i+1}$. Put on $Y_i=Y^{A_i}$ the bounded uniform metric
$$
\rho_i(u,v)=\min\{1,\sup_{A_i}d(u,v)\}.
$$
Define
$$
\rho(f,g)=\sum_{i=1}^\infty2^{-i}\rho_i(f\restrict_{A_i},g\restrict_{A_i}).
$$
This induces exactly compact convergence: every compact $C\subset X$ is covered by finitely many $\operatorname{Int}A_i$, hence lies in some $A_N$, while each $A_i$ itself is compact.

The restriction map
$$
R:Y^X\to\prod_iY_i,\qquad f\mapsto(f\restrict_{A_i})
$$
identifies $Y^X$ with the closed compatibility subspace $u_{i+1}\restrict_{A_i}=u_i$. If $Y$ is complete, each uniform function space $Y_i$ is complete (pointwise limits of uniform Cauchy families exist and convergence is uniform), so the metric $\sum_i 2^{-i}\rho_i$ on $\prod_iY_i$ is complete, and $R$ is an isometry from $(Y^X,\rho)$ onto the compatibility subspace. A closed subspace is complete, so $(Y^X,\rho)$ is complete.
:::
