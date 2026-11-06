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
Let $K$ be a simplicial complex and, for each vertex $v$, let $\operatorname{st}^{\circ}(v)$ be its open star. The nerve of this cover has one vertex for each vertex of $K$.

A finite collection of open stars
$$
\operatorname{st}^{\circ}(v_0),\ldots,
\operatorname{st}^{\circ}(v_q)
$$
has nonempty intersection exactly when the vertices $v_0,\ldots,v_q$ span a simplex of $K$. (This is the identification used in the proof of Lemma 2C.2, p. 178: the open stars of the vertices form a cover of $|K|$ by sets whose intersections are controlled by the simplices.) Indeed, if they span a simplex $\sigma$, the barycenter of $\sigma$ lies in every one of these open stars. Conversely, if a point lies in all the stars, it lies in the interior of some simplex $\tau$ containing every $v_i$, so the $v_i$'s span a face of $\tau$.

Thus a set of vertices spans a simplex in the nerve if and only if it spans the corresponding simplex in $K$. Therefore the identification on vertices extends to a canonical simplicial isomorphism
$$
\boxed{N(\{\operatorname{st}^{\circ}(v)\})\cong K.}
$$
:::
