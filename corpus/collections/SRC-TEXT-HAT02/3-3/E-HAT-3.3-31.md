---
schema: qual/card@1
id: E-HAT-3.3-31
kind: problem
title: "Boundary map sends fundamental class to fundamental class"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.

::: {.solution}
Let
\[
[M,\partial M]\in H_n(M,\partial M;R)
\]
be a fundamental class, and let
\[
\delta:H_n(M,\partial M;R)\to H_{n-1}(\partial M;R)
\]
be the boundary homomorphism.

Fix $x\in\partial M$ and choose an oriented collar half-ball neighborhood of $x$. Naturality of the long exact sequence of a pair gives a commutative diagram from the global boundary map to the local boundary map. The image of $[M,\partial M]$ in the local relative group is the local fundamental class of the half-ball, and its local boundary is precisely the generator of
\[
H_{n-1}(\partial M,\partial M-\{x\};R)
\]
that defines the induced boundary orientation from Exercise 30.

Therefore $\delta[M,\partial M]$ maps to the chosen local orientation generator at every $x\in\partial M$. A fundamental class is characterized by this property. Hence
\[
\boxed{\delta[M,\partial M]=[\partial M]}
\]
for the induced orientation on $\partial M$ (with the usual global sign convention).
:::
