---
schema: qual/card@1
id: E-PBG3W
kind: problem
title: Composites of covering maps with finite fibers
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 53: Problem 4 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-4-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-53-covering-spaces/problem-4-solution.txt), and against Munkres, Topology (2000), Section 53
    Exercise 4, printed p. 341, with the definition of a covering map on printed p. 336. dbFin's argument shrinks the evenly covered neighbourhood of $z$ to a finite intersection of images of evenly covered neighbourhoods upstairs; the card does the same. One step is implicit in both and is now stated on the card: with $W_i$ evenly covered by $q$ and $W_i\subseteq V_i$, the slice $W_i'=W_i\cap r^{-1}(U')$ equals $V_i\cap r^{-1}(U')$, because $r$ restricted to $V_i$ is injective, so the slices over $U'$ really are the sets $W_i'$. Nothing else needed repair.
---

::: {.exercise}

Let $q: X \to Y$ and $r: Y \to Z$ be covering maps; let $p = r \circ q$.
Show that if $r^{-1}(z)$ is finite for each $z \in Z$, then $p$ is a covering map.
:::

::: {.solution}
Fix $z\in Z$. Since $r:Y\to Z$ is a covering map, choose an evenly covered neighborhood $U$ of $z$:
$$
r^{-1}(U)=\bigsqcup_{i=1}^m V_i,
$$
where $m=\cardinality{r^{-1}(z)}<\infty$ and each $r\restrict_{V_i}:V_i\to U$ is a homeomorphism.

Let $y_i\in V_i$ be the unique point over $z$. Since $q:X\to Y$ is a covering map, for each $i$ choose an evenly covered neighborhood $W_i\subset V_i$ of $y_i$. Because $r\restrict_{V_i}$ is a homeomorphism, $r(W_i)$ is an open neighborhood of $z$ in $U$. Set
$$
U'=\bigcap_{i=1}^m r(W_i).
$$
This is open because the intersection is finite. Replace each $W_i$ by
$$
W_i'=W_i\cap r^{-1}(U').
$$
Then $q^{-1}(W_i')$ is a disjoint union of open slices, each mapped homeomorphically by $q$ onto $W_i'$; composing with $r\restrict_{W_i'}$ maps each such slice homeomorphically onto $U'$.

Moreover
$$
p^{-1}(U')=q^{-1}(r^{-1}(U'))=\bigsqcup_{i=1}^m q^{-1}(W_i'),
$$
so these slices partition $p^{-1}(U')$. Hence $U'$ is evenly covered by $p=r\circ q$, and $p$ is a covering map.
:::
