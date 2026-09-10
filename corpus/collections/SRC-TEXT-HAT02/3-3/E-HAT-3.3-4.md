---
schema: qual/card@1
id: E-HAT-3.3-4
kind: problem
title: "Quotients by orientation-preserving actions"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Given a covering space action of a group $G$ on an orientable manifold $M$ by orientation-preserving homeomorphisms, show that $M/G$ is also orientable.

::: {.solution}
Let $q:M\to M/G$ be the quotient map. Since the action is a covering-space action, $q$ is a covering map and $M/G$ is a manifold.

Fix $y\in M/G$ and choose an evenly covered neighborhood $U$ of $y$. Let $\widetilde U$ be one sheet over $U$. Because $M$ is oriented, $\widetilde U$ inherits a local orientation. Transport this orientation to $U$ using the homeomorphism
\[
q|_{\widetilde U}:\widetilde U\xrightarrow{\cong}U.
\]
We must show this does not depend on the chosen sheet. Any two sheets over $U$ differ by a unique deck transformation coming from an element $g\in G$. By hypothesis every such $g$ preserves the orientation of $M$, so the two transported orientations on $U$ agree.

Hence every sufficiently small $U\subset M/G$ has a well-defined orientation, and these local orientations agree on overlaps. Thus $M/G$ is orientable.
:::
