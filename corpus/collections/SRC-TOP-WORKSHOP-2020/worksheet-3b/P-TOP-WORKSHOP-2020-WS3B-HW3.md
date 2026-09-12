---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-HW3
kind: problem
title: 'Galois correspondence for universal covers'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
State the Galois Correspondence Theorem for a path-connected, locally path-connected, and semilocally simply connected space $X$.
:::

::: {.solution}
Let \(X\) be path connected, locally path connected, and semilocally simply connected, with basepoint \(x_0\). Then:

- Isomorphism classes of **based connected covering spaces**
\[
(p:E\to X,e_0),\qquad p(e_0)=x_0,
\]
correspond bijectively to subgroups
\[
H\le\pi_1(X,x_0),
\qquad H=p_*\pi_1(E,e_0).
\]
- If basepoints upstairs are forgotten, connected covering spaces correspond to conjugacy classes of subgroups of \(\pi_1(X,x_0)\).
- The covering is regular (normal/Galois) exactly when \(H\trianglelefteq\pi_1(X,x_0)\). In general its deck group is
\[
N(H)/H,
\]
and for a regular cover this is \(\pi_1(X,x_0)/H\).
- The universal cover corresponds to the trivial subgroup. If \(\widetilde X\to X\) is universal, every connected cover is obtained, up to equivalence, as
\[
\widetilde X/H\to X
\]
for a subgroup \(H\le\operatorname{Deck}(\widetilde X/X)\cong\pi_1(X,x_0)\).
:::
