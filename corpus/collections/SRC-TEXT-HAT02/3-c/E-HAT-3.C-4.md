---
schema: qual/card@1
id: E-HAT-3.C-4
kind: problem
title: "Lifting H-space structure to universal covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that an H-space or topological group structure on a path-connected, locally path-connected space can be lifted to such a structure on its universal cover.
[For the group $SO(n)$ considered in the next section, the universal cover for $n > 2$ is a 2-sheeted cover, a group called $\operatorname{Spin}(n)$.]
:::

::: {.solution}
Let
\[
p:\widetilde X\to X
\]
be the universal covering and choose $\widetilde e\in p^{-1}(e)$.

For an H-space multiplication $\mu:X\times X\to X$, consider
\[
\mu\circ(p\times p):\widetilde X\times\widetilde X\to X.
\]
The domain is simply connected, so this map has a unique lift
\[
\widetilde\mu:\widetilde X\times\widetilde X\to\widetilde X
\]
with $\widetilde\mu(\widetilde e,\widetilde e)=\widetilde e$.
The homotopies expressing the left and right identity laws for $\mu$ lift uniquely, starting from the corresponding restrictions of $\widetilde\mu$, and end at the identity map of $\widetilde X$. Hence $\widetilde X$ is an H-space.

If $X$ is a topological group, apply the same construction to multiplication. The inversion map
\[
\iota:X\to X,
\qquad x\mapsto x^{-1},
\]
also lifts uniquely to a map $\widetilde\iota:\widetilde X\to\widetilde X$ fixing $\widetilde e$. Associativity of $\widetilde\mu$ follows from uniqueness of lifts: the two maps
\[
\widetilde\mu(\widetilde\mu(-,-),-),
\qquad
\widetilde\mu(-,\widetilde\mu(-,-))
\]
are lifts of the same map $\widetilde X^3\to X$ and agree at $(\widetilde e,\widetilde e,\widetilde e)$, so they are equal. The strict identity and inverse laws follow in exactly the same way by comparing the relevant lifts. Thus $\widetilde X$ is a topological group and $p$ is a homomorphism.
:::
