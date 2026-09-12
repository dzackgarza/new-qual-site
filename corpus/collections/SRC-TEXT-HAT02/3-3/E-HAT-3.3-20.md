---
schema: qual/card@1
id: E-HAT-3.3-20
kind: problem
title: "Compactly supported $H^0$ of noncompact spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $H_c^0(X; G) = 0$ if $X$ is path-connected and noncompact.

::: {.solution}
A degree-zero cocycle with coefficients in $G$ is a locally constant function
\[
f:X\to G.
\]
If $X$ is path-connected, every locally constant function is constant. A compactly supported degree-zero class must therefore be represented by a constant function whose support is compact.

If the constant is nonzero, its support is all of $X$, which is noncompact. Hence the only compactly supported degree-zero cocycle is the zero function. Therefore
\[
\boxed{H_c^0(X;G)=0.}
\]
:::
