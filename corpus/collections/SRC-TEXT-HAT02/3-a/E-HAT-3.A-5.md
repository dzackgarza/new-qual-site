---
schema: qual/card@1
id: E-HAT-3.A-5
kind: problem
title: "Tor vanishes for torsionfree modules"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
From the fact that $\operatorname{Tor}(A, B) = 0$ if $A$ is free, deduce that $\operatorname{Tor}(A, B) = 0$ if $A$ is torsionfree by applying the previous problem to the directed system of finitely generated subgroups $A_\alpha$ of $A$.
:::

::: {.solution}
Write a torsionfree abelian group $A$ as the directed union of its finitely generated subgroups:
\[
A=\varinjlim_\alpha A_\alpha.
\]
Each $A_\alpha$ is finitely generated and torsionfree, hence is a free abelian group. Therefore
\[
\operatorname{Tor}(A_\alpha,B)=0
\]
for every $\alpha$.

By Exercise 4, $\operatorname{Tor}$ commutes with direct limits in the first variable, so
\[
\operatorname{Tor}(A,B)
\cong \varinjlim_\alpha\operatorname{Tor}(A_\alpha,B)
=0.
\]
:::
