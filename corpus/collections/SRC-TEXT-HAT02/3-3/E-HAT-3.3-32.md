---
schema: qual/card@1
id: E-HAT-3.3-32
kind: problem
title: "Compact manifolds do not retract onto boundary"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 32; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a compact manifold does not retract onto its boundary.

::: {.solution}
It is enough to use $R=\mathbb Z_2$, over which every manifold is orientable. Suppose there were a retraction
\[
r:M\to\partial M
\]
with inclusion $i:\partial M\hookrightarrow M$. Then
\[
r\circ i=\operatorname{id}_{\partial M},
\]
so on homology
\[
r_*i_*=\operatorname{id}.
\]
Thus
\[
i_*:H_{n-1}(\partial M;\mathbb Z_2)\to H_{n-1}(M;\mathbb Z_2)
\]
would be injective.

On the other hand, Exercise 31 says that the boundary homomorphism in the long exact sequence of the pair sends the relative fundamental class to the nonzero boundary fundamental class:
\[
\delta[M,\partial M]=[\partial M]\ne0.
\]
Exactness of
\[
H_n(M,\partial M)\xrightarrow{\delta}H_{n-1}(\partial M)
\xrightarrow{i_*}H_{n-1}(M)
\]
therefore gives
\[
i_*[\partial M]=0.
\]
This contradicts injectivity of $i_*$. Hence a compact manifold cannot retract onto its boundary.
:::
