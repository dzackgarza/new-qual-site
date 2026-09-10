---
schema: qual/card@1
id: E-HAT-3.3-19
kind: problem
title: "Countability of homology of open subsets of $\\mathbb{R}^n$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a direct limit of countable abelian groups over a countable indexing set is countable.
Apply this to show that if $X$ is an open set in $\mathbb{R}^n$ then $H_i(X; \mathbb{Z})$ is countable for all $i$.

::: {.solution}
If the indexing set is countable and every $G_\alpha$ is countable, then the disjoint union
\[
\coprod_\alpha G_\alpha
\]
is countable. The direct limit is a quotient of this set, hence is countable.

Now let $X\subset\mathbb R^n$ be open. Choose an exhaustion
\[
K_1\subset\operatorname{int}K_2\subset\operatorname{int}K_3\subset\cdots,
\qquad
X=\bigcup_j K_j,
\]
where each $K_j$ is a finite cubical polyhedron contained in $X$. Such an exhaustion is obtained from a rational cubulation by taking finitely many cubes whose distance from $\mathbb R^n-X$ and from infinity is bounded below.

Every compact subset of $X$ lies in some $K_j$. In particular every singular simplex, and every finite singular chain or chain homotopy, is contained in some stage. Hence
\[
C_*(X)=\varinjlim_j C_*(K_j)
\]
and Exercise 17 gives
\[
H_i(X;\mathbb Z)\cong\varinjlim_j H_i(K_j;\mathbb Z).
\]
Each $K_j$ is a finite CW complex, so $H_i(K_j;\mathbb Z)$ is finitely generated and therefore countable. The indexing set is countable, so the first part implies
\[
\boxed{H_i(X;\mathbb Z)\text{ is countable for every }i.}
\]
:::
