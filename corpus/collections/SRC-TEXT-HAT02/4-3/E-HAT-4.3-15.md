---
schema: qual/card@1
id: E-HAT-4.3-15
kind: problem
title: "Homotopy equivalence fibration is fiber homotopy trivial"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If the fibration $p: E \to B$ is a homotopy equivalence, show that $p$ is a fiber homotopy equivalence of $E$ with the trivial fibration $\mathbb{1}: B \to B$.
:::

::: {.solution}
The fibration \(p:E\to B\) and the identity fibration
\[
1_B:B\to B
\]
represent the same element of \(\mathcal M(B)\): the map
\[
p:E\to B
\]
is itself a homotopy equivalence and satisfies
\[
p=1_B\circ p.
\]
By the bijection of Exercise 14, equal classes in \(\mathcal M(B)\) correspond to the same class in \(\mathcal F(B)\). Thus
\[
\boxed{p:E\to B\text{ is fiber homotopy equivalent to }1_B:B\to B.}
\]
:::
