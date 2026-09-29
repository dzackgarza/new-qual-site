---
schema: qual/card@1
id: P-AGXVARZARNOTSEP
kind: problem
title: The Zariski topology is never Hausdorff except on a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Separation Axioms
  - Irreducibility
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clause of Zaidenberg Exercises 2.7 in the recorded
    source. It follows immediately after the assertion that every nonempty
    Zariski open subset of an affine variety is dense and any two such opens
    intersect.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the source's topological word "separated" by "Hausdorff" on the
    standalone card. In modern algebraic geometry "separated" is a different
    scheme-theoretic property, and affine varieties are separated in that
    sense.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Used irreducibility to show that every pair of nonempty Zariski open sets
    intersects, contradicting the disjoint-neighborhood requirement for two
    distinct points in a Hausdorff space.
---

::: {.problem}
Let $X$ be an affine variety. Show that the Zariski topology on $X$ is
Hausdorff if and only if $X$ is a singleton.
:::

::: {.solution}

::: pf

::: {.pf-step #opens-intersect}
Every two nonempty Zariski-open subsets of $X$ intersect.

::: pf-proof
An affine variety is irreducible by definition. Let
$$
U,V\subseteq X
$$
be nonempty open subsets. If
$$
U\intersect V=\varnothing,
$$
then
$$
X
=
(X\sm U)
\union
(X\sm V).
$$
Both complements are proper closed subsets because $U$ and $V$ are
nonempty. This writes the irreducible space $X$ as the union of two proper
closed subsets, a contradiction.

Therefore
$$
U\intersect V\ne\varnothing.
$$
:::

:::

::: {.pf-step #not-hausdorff-if-two-points}
If $X$ contains two distinct points, then its Zariski topology is not
Hausdorff.

::: pf-proof
Suppose
$$
p,q\in X,
\qquad
p\ne q.
$$
If $X$ were Hausdorff, there would be disjoint open neighborhoods
$$
p\in U,
\qquad
q\in V,
\qquad
U\intersect V=\varnothing.
$$
Both $U$ and $V$ are nonempty, contradicting step [](#opens-intersect){.pf-ref}. Hence a variety with
at least two points is not Hausdorff.
:::

:::

::: {.pf-step #singleton-hausdorff}
A singleton variety is Hausdorff.

::: pf-proof
Every singleton topological space is Hausdorff: there are no two distinct
points whose neighborhoods must be separated.
:::

:::

::: {.pf-step #equivalence-statement}
Therefore
$$
\boxed{
X\text{ is Hausdorff in its Zariski topology}
\quad\Longleftrightarrow\quad
X\text{ is a point}.
}
$$

::: pf-proof
Step [](#not-hausdorff-if-two-points){.pf-ref} shows that Hausdorffness forces $X$ to contain at most one point.
A variety is nonempty, so it must then be a singleton. Step [](#singleton-hausdorff){.pf-ref} proves the
converse.
:::

:::

::: pf-qed
Step [](#equivalence-statement){.pf-ref} is the required conclusion.
:::

:::

:::
