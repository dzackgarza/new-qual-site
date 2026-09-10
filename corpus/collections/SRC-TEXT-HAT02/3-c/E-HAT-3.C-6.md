---
schema: qual/card@1
id: E-HAT-3.C-6
kind: problem
title: "Spheres as H-spaces via $J_2(S^n)$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 6; repaired the local statement to restore the source's “if and only if”.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $S^n$ is an H-space if and only if the attaching map of the $2n$-cell of $J_2(S^n)$ is homotopically trivial.

::: {.solution}
Let
\[
S^n\vee S^n\hookrightarrow S^n\times S^n
\]
be the standard inclusion. The product has a CW structure obtained from the wedge by attaching one $2n$-cell. Let
\[
\omega:S^{2n-1}\to S^n\vee S^n
\]
be its attaching map, and let
\[
\nabla:S^n\vee S^n\to S^n
\]
be the fold map, equal to the identity on each summand.

A multiplication
\[
\mu:S^n\times S^n\to S^n
\]
with $e$ as a strict two-sided identity is exactly an extension of $\nabla$ across the $2n$-cell. Such an extension exists if and only if
\[
\nabla\circ\omega:S^{2n-1}\to S^n
\]
is nullhomotopic.

By the definition of the second James stage
\[
J_2(S^n)=S^n\times S^n/\bigl((x,e)\sim x\sim(e,x)\bigr),
\]
its $n$-skeleton is the single copy of $S^n$ obtained from the wedge by the fold map, and its unique $2n$-cell is attached precisely by
\[
\nabla\circ\omega.
\]
Hence the attaching map of the $2n$-cell of $J_2(S^n)$ is nullhomotopic if and only if the fold map extends over $S^n\times S^n$.

If it is nullhomotopic, choose such an extension $\mu$; then $\mu(x,e)=x=\mu(e,x)$, so $S^n$ is an H-space. Conversely, if $S^n$ is an H-space, Exercise 1 allows its multiplication to be homotoped to one with strict identity, hence to an extension of the fold map, forcing the attaching map to be nullhomotopic. Therefore
\[
\boxed{S^n\text{ is an H-space}\iff
\text{the }2n\text{-cell of }J_2(S^n)\text{ is attached trivially}.}
\]
:::
