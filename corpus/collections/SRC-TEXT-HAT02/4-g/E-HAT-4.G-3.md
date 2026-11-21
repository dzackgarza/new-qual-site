---
schema: qual/card@1
id: E-HAT-4.G-3
kind: problem
title: Nerve of the open star cover
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.G, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps and added what it needed to be a proof rather than
    an identification: that the open stars really do cover the realization (each point lies in the open star of
    the vertices of the smallest simplex containing it in its interior), that the barycentre of a
    simplex lies in the open star of each of its vertices, and that a point lying in several open
    stars lies in the interior of a simplex containing all of those vertices, which is the converse
    direction the earlier text compressed into one clause. Then the nerve criterion is applied in
    both directions to conclude that the vertex bijection is an isomorphism of simplicial complexes.
    Not re-read this session: printed p. 178.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher §4.G Exercise 3 and the definition of the nerve in §4.G. The mathematics is
    right: the cover by open stars, the barycentre argument, the converse that a point in several
    open stars lies in the interior of one simplex containing all those vertices, and the resulting
    isomorphism with $K$. Two repairs. The first step justified openness of the open star by saying
    it is a union of interiors of simplices "which are open in $\realization{K}$", and that is false
    as soon as a simplex has a proper face: the interior of an edge of a triangle is not open. The
    star is now shown open as the complement of the closed simplices not having the vertex. The lead
    no longer locates the exercise by printed page, and no longer points at a file under `tmp`,
    which does not survive a VM reset; it names the exercise and says which retained sets stop
    before §4.G. No statement changed. Not checked: no certificate; nothing here was verified by
    computation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
What is the nerve of the cover of a simplicial complex by the open stars of its vertices?
[See Lemma 2C.2.]
:::

::: {.solution}

No retained solution set covers this exercise: Sam's set stops at §4.3, and the retained sets that reach further record no solution for §4.G. The argument is the card's own, and the identification of open stars with simplices is the one used in the proof of Lemma 2C.2.

Let $K$ be a simplicial complex with geometric realization $\realization{K}$; for a vertex $v$ let $\operatorname{st}^{\circ}(v)$ be its open star, the union of the interiors of the simplices containing $v$. The nerve $N(\mathcal{U})$ of a cover $\mathcal{U}$ has a vertex for each member $U$ and a $q$-simplex for each $(q+1)$-tuple of members with nonempty intersection.

::: pf

::: {.pf-step #cover}
$\{\operatorname{st}^{\circ}(v)\mid v\text{ a vertex of }K\}$ is an open cover of $\realization{K}$.

::: pf-proof
The complement of $\operatorname{st}^{\circ}(v)$ is the union of the closed simplices of $K$ that do not have $v$ as a vertex, a closed set, so the open star is open; the interiors of simplices are not themselves open in $\realization{K}$ when the simplex has faces. If $p\in\realization{K}$, then $p$ lies in the interior of a unique simplex $\sigma$; writing $p=\sum_{v\in\sigma}t_{v}v$ with all $t_{v}>0$, we have $p\in\operatorname{st}^{\circ}(v)$ for every vertex $v$ of $\sigma$, in particular for one. So every point lies in some member.
:::

:::

::: {.pf-step #barycentre}
If $v_{0},\dots,v_{q}$ are vertices spanning a simplex $\sigma$ of $K$, the barycentre of $\sigma$ lies in $\bigcap_{i}\operatorname{st}^{\circ}(v_{i})$.

::: pf-proof
The barycentre $b_{\sigma}=\frac{1}{q+1}\sum_{i=0}^{q}v_{i}$ has all barycentric coordinates positive on the vertices of $\sigma$ and zero elsewhere, so it lies in the interior of $\sigma$, hence in the open star of each of its vertices $v_{0},\dots,v_{q}$.
:::

:::

::: {.pf-step #converse}
If a point $p$ lies in $\operatorname{st}^{\circ}(v_{0})\cap\cdots\cap\operatorname{st}^{\circ}(v_{q})$, then $v_{0},\dots,v_{q}$ span a simplex of $K$.

::: pf-proof
Each open star is a union of interiors of simplices, and the interiors of distinct simplices are disjoint, so a point lies in the interior of exactly one simplex, say $\tau$. That $p\in\operatorname{st}^{\circ}(v_{i})$ means $v_{i}$ is a vertex of $\tau$. Hence all the $v_{i}$ are vertices of the single simplex $\tau$, so they span a face of $\tau$, which is a simplex of $K$.
:::

:::

::: {.pf-step #nerve}
A finite set $\{v_{0},\dots,v_{q}\}$ of vertices spans a simplex of $K$ if and only if the corresponding members of the cover have nonempty intersection.

::: pf-proof
If the vertices span a simplex, step [](#barycentre){.pf-ref} puts the barycentre of that simplex in every one of the stars, so the intersection is nonempty. If the intersection is nonempty, step [](#converse){.pf-ref} shows that the vertices all belong to one simplex, that is, they span a simplex.
:::

:::

::: {.pf-step}
The nerve of the cover by open stars is isomorphic to $K$.

::: pf-proof
The assignment $v\mapsto\operatorname{st}^{\circ}(v)$ is a bijection between the vertex sets, and by step [](#nerve){.pf-ref} a set of vertices spans a simplex of $K$ exactly when the corresponding set of cover members spans a simplex of the nerve. A bijection on vertices with this property is an isomorphism of simplicial complexes, so $N(\{\operatorname{st}^{\circ}(v)\})\cong K$.
:::

:::

:::

:::
