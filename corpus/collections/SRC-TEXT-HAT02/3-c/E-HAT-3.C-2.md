---
schema: qual/card@1
id: E-HAT-3.C-2
kind: problem
title: "Retracts of H-spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a retract of an H-space is an H-space if it contains the identity element.

::: {.solution}
Let $X$ be an H-space with identity $e$, and let $A\subset X$ be a retract containing $e$. Write
\[
i:A\hookrightarrow X,
\qquad
r:X\to A,
\qquad
r\circ i=\operatorname{id}_A.
\]
If
\[
\mu:X\times X\to X
\]
is the H-space multiplication, define
\[
\mu_A=r\circ\mu\circ(i\times i):A\times A\to A.
\]
Then
\[
\mu_A(a,e)=r(\mu(i(a),e)),
\qquad
\mu_A(e,a)=r(\mu(e,i(a))).
\]
The two maps $x\mapsto\mu(x,e)$ and $x\mapsto\mu(e,x)$ are homotopic to $\operatorname{id}_X$ through basepoint-preserving maps. Composing these homotopies with $i$ and $r$ gives basepoint-preserving homotopies
\[
a\longmapsto\mu_A(a,e)\simeq r i(a)=a,
\]
and similarly
\[
a\longmapsto\mu_A(e,a)\simeq a.
\]
Thus $A$ is an H-space with identity $e$.
:::
