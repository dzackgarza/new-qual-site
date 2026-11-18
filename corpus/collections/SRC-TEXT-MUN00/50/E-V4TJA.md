---
schema: qual/card@1
id: E-V4TJA
kind: problem
title: Five points in general position and a linear $K_5$ in $\RR^3$
classification:
  areas:
  - topology
  topics:
  - Dimension
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
    Checked against Munkres, Topology (2000), §50 Exercise 4, printed p. 315, with the definition of general
    position in R^N on printed p. 313 (every subset of N+1 or fewer points is geometrically independent) and
    Example 7 for the linear imbedding of a finite graph. The five four-point subsets are checked by
    determinants: {0, e_1, e_2, e_3} has determinant 1, the three sets containing 0, (1,1,1) and two of the
    e_i have determinant 1, and {e_1, e_2, e_3, (1,1,1)} gives the matrix with rows (-1,1,0), (-1,0,1), (0,1,1)
    of determinant 2; three collinear points are excluded by the same determinants. Nothing needed correction,
    except that the card now states the book's definition of general position instead of a paraphrase of it.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 4 (printed p. 315),
    and the second half of it, the sketch of the linear imbedding of $K_5$, is a figure in the book that no
    written source reproduces. Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten
    GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post
    *Topology by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630)
    answers §50 with its formulas lost. The card's determinant checks of the five four-point subsets are its
    own; the Stack Exchange queries of this pass, listed in the COMPLAINTS.md entry for §43--§50, returned no
    question on the exercise. Nothing needed correction.
---

::: {.exercise}

Show that the points $\mathbf{0}, \epsilon_1, \epsilon_2, \epsilon_3$, and $(1, 1, 1)$ are in general position in $\RR^3$.
Sketch the corresponding imbedding into $\RR^3$ of the complete graph on five vertices.
:::

::: {.solution}

No complete published solution was located for Munkres §50 Exercise 4, printed p. 315; the argument below is the card's own, and the sets searched are recorded in its audit trail.

Let $p_{0}=\mathbf{0}$, $p_{1}=\epsilon_{1}$, $p_{2}=\epsilon_{2}$, $p_{3}=\epsilon_{3}$ and $p_{4}=(1,1,1)$ in $\RR^{3}$. A set of points of $\RR^{N}$ is in general position when every subset of $N+1$ or fewer points is geometrically independent (§50, printed p. 313), so for five points of $\RR^{3}$ the condition is that every four of them are affinely independent.

::: pf

::: {.pf-step #four-indep}
Every four of the five points are affinely independent.

::: pf-proof

::: {.pf-step #triple}
$\{p_{0},p_{1},p_{2},p_{3}\}$ is affinely independent.

::: pf-proof
The differences $p_{1}-p_{0}=\epsilon_{1}$, $p_{2}-p_{0}=\epsilon_{2}$, $p_{3}-p_{0}=\epsilon_{3}$ are the standard basis, whose determinant is $1\ne0$.
:::

:::

::: {.pf-step #with-four}
Each of the three sets $\{p_{0},p_{i},p_{j},p_{4}\}$ with $\{i,j\}$ a two-element subset of $\{1,2,3\}$ is affinely independent.

::: pf-proof
Let $k$ be the remaining index. Subtracting $p_{0}$ from the other three points gives $\epsilon_{i}$, $\epsilon_{j}$ and $(1,1,1)$, a matrix whose first two rows are distinct standard basis vectors and whose third row is $(1,1,1)$. Expanding along the two standard rows leaves the product of their two nonzero entries with the entry $1$ of the third row in the remaining coordinate, up to sign, so the determinant is $\pm1\ne0$, and the three difference vectors are linearly independent.
:::

:::

::: {.pf-step #last-four}
$\{p_{1},p_{2},p_{3},p_{4}\}$ is affinely independent.

::: pf-proof
Subtracting $p_{1}$ from the other three points gives
$$
p_{2}-p_{1}=(-1,1,0),\qquad p_{3}-p_{1}=(-1,0,1),\qquad p_{4}-p_{1}=(0,1,1),
$$
the determinant of whose matrix as rows is $-1-1+1\cdot 1=2$ by expansion along the third row: $0\cdot(\cdots)-1\cdot\big((-1)(1)-(-1)(0)\big)+1\cdot\big((-1)(0)-(-1)(1)\big)=-(-1)+1=2\ne0$.
:::

:::

::: {.pf-qed}
The five four-element subsets of $\{p_{0},\ldots,p_{4}\}$ are exactly the four of steps [](#triple){.pf-ref}, [](#with-four){.pf-ref} and [](#last-four){.pf-ref}, and each is affinely independent.
:::

:::

:::

::: {.pf-step #general-position}
The five points are in general position.

::: pf-proof
Let $S$ be a subset with at most four points. If $\abs{S}\le3$ then $S$ is contained in one of the affinely independent four-element subsets of step [](#four-indep){.pf-ref}, and a subset of an affinely independent set is affinely independent. If $\abs{S}=4$ then $S$ is one of those subsets. So every subset of four or fewer points is geometrically independent, which is general position in $\RR^{3}$.
:::

:::

::: {.pf-step #imbedding}
The ten straight segments joining the pairs of these points form an embedded copy of $K_{5}$ in $\RR^{3}$.

::: pf-proof

::: {.pf-step #no-crossing}
Two segments with no common endpoint do not meet.

::: pf-proof
Suppose the segments $p_{i}p_{j}$ and $p_{k}p_{\ell}$, with $\{i,j\}\cap\{k,\ell\}=\varnothing$, meet at a point $q$. If $q$ is an endpoint of one of them it is also an interior point of the other, so the four points are not distinct, contrary to the five points being distinct. Otherwise $q$ lies on two distinct lines, one through $p_{i},p_{j}$ and one through $p_{k},p_{\ell}$, and two intersecting lines span a plane, so $p_{i},p_{j},p_{k},p_{\ell}$ lie in one plane, hence are affinely dependent, contrary to step [](#four-indep){.pf-ref}.
:::

:::

::: {.pf-step #homeo}
The map $g$ of the graph $K_{5}$ sending the vertex $v_{m}$ to $p_{m}$ and the edge $v_{i}v_{j}$ linearly onto $p_{i}p_{j}$ is an imbedding.

::: pf-proof
The graph $K_{5}$ is the union of its finitely many closed edges, each a copy of $[0,1]$ and so compact; a finite union of compact subspaces is compact, since a finite subcover of each piece gathers to one of the union. A map on $K_{5}$ is continuous exactly when its restriction to each of these finitely many closed pieces is continuous (the pasting lemma, Theorem 18.3, printed p. 110), and a linear map on an interval is continuous, so $g$ is continuous. It is injective: distinct vertices go to distinct points, a vertex and an edge not incident with it are disjoint by step [](#no-crossing){.pf-ref}, its restriction to each edge is injective, and two edges with no common endpoint are disjoint there. A continuous injection from a compact space to a Hausdorff space is an imbedding onto its image (Theorem 26.6, printed p. 167). So $g(K_{5})$ is an embedded copy of $K_{5}$ in $\RR^{3}$ whose edges are those ten segments.
:::

:::

::: {.pf-qed}
Steps [](#no-crossing){.pf-ref} and [](#homeo){.pf-ref} show that the union of the ten segments is a homeomorphic copy of $K_{5}$, which is the required imbedding.
:::

:::

:::

:::
:::
