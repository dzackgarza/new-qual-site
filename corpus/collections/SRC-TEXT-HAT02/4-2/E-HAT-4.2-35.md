---
schema: qual/card@1
id: E-HAT-4.2-35
kind: problem
title: "Quotient fiber bundle from quaternionic Hopf bundle"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 35; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the fiber bundle $S^3 \to S^{4n+3} \to \mathbb{HP}^n$ gives rise to a quotient fiber bundle $S^2 \to \mathbb{CP}^{2n+1} \to \mathbb{HP}^n$ by factoring out the action of $S^1$ on $S^{4n+3}$ by complex scalar multiplication.

::: {.solution}
View
\[
S^{4n+3}\subset\mathbb H^{n+1}.
\]
The quaternionic Hopf bundle is the quotient by right multiplication of unit quaternions:
\[
S^3\longrightarrow S^{4n+3}\longrightarrow\mathbb{HP}^n.
\]
Inside \(S^3\) is the subgroup
\[
S^1=\{e^{i\theta}\}\subset\mathbb C\subset\mathbb H.
\]
Its action on \(S^{4n+3}\) is precisely complex scalar multiplication after identifying
\[
\mathbb H^{n+1}\cong\mathbb C^{2n+2}.
\]
Therefore
\[
S^{4n+3}/S^1\cong\mathbb{CP}^{2n+1}.
\]

Although \(S^1\subset S^3\) is not a normal subgroup, the quotient is taken fiberwise by the right \(S^1\)-action: over a quaternionic line \(L\), the Hopf fiber is \(S^3\), and dividing that fiber by the right \(S^1\)-action gives
\[
S^3/S^1\cong S^2.
\]
The original local trivializations of the quaternionic Hopf bundle are \(S^3\)-equivariant, hence descend after quotienting by \(S^1\). Thus we obtain a locally trivial bundle
\[
\boxed{S^2\longrightarrow\mathbb{CP}^{2n+1}\longrightarrow\mathbb{HP}^n.}
\]
:::
