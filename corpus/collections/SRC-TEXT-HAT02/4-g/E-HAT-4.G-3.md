---
schema: qual/card@1
id: E-HAT-4.G-3
kind: problem
title: "Nerve of the open star cover"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
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
---

What is the nerve of the cover of a simplicial complex by the open stars of its vertices?

::: {.solution}
Let \(K\) be a simplicial complex and, for each vertex \(v\), let \(\operatorname{st}^{\circ}(v)\) be its open star. The nerve of this cover has one vertex for each vertex of \(K\).

A finite collection of open stars
\[
\operatorname{st}^{\circ}(v_0),\ldots,
\operatorname{st}^{\circ}(v_q)
\]
has nonempty intersection exactly when the vertices \(v_0,\ldots,v_q\) span a simplex of \(K\). Indeed, if they span a simplex \(\sigma\), the barycenter of \(\sigma\) lies in every one of these open stars. Conversely, if a point lies in all the stars, it lies in the interior of some simplex \(\tau\) containing every \(v_i\), so the \(v_i\)'s span a face of \(\tau\).

Thus a set of vertices spans a simplex in the nerve if and only if it spans the corresponding simplex in \(K\). Therefore the identification on vertices extends to a canonical simplicial isomorphism
\[
\boxed{N(\{\operatorname{st}^{\circ}(v)\})\cong K.}
\]
:::
