---
schema: qual/card@1
id: E-KS2QC
kind: problem
title: The projective line and its covering
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
---

::: {.exercise}

The space $P^1$ and the covering map $p: S^1 \to P^1$ are familiar ones.
What are they?
:::

::: {.solution}
The real projective line \(P^1\) is the set of one-dimensional linear subspaces of \(\mathbb R^2\). A line through the origin is determined by either of the two antipodal unit vectors lying on it. Hence
\[
P^1=S^1/(x\sim -x).
\]

This quotient is itself homeomorphic to a circle. In complex notation, identify \(S^1\subset\mathbb C\). The map
\[
q:S^1\to S^1,\qquad q(z)=z^2,
\]
has exactly the antipodal pairs \(\{z,-z\}\) as its fibers, so it factors through a continuous bijection
\[
P^1\longrightarrow S^1.
\]
Since \(P^1\) is compact and \(S^1\) Hausdorff, this bijection is a homeomorphism.

Under this identification, the standard covering
\[
p:S^1\to P^1,
\qquad p(x)=\mathbb Rx,
\]
is exactly the familiar two-sheeted circle covering \(z\mapsto z^2\).
:::
