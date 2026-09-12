---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G04
kind: problem
title: A torus with a disk attached along one circle factor
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Cell Complexes
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
(June ’12) Let $X$ be the space obtained from the torus $T^2=S^1\times S^1$ by gluing in a disk $D^2$ along its boundary $\partial D^2=S^1$ using the map $\alpha:S^1\to T^2$ given by $z\mapsto(z,(1,0))$ for $z\in S^1$.

(a) Find $\pi_1(X)$.

(b) Give a CW complex for $X$.
:::

::: {.solution}
Use the standard CW structure on the torus: one \(0\)-cell, two \(1\)-cells \(a,b\), and one \(2\)-cell attached by
\[
aba^{-1}b^{-1}.
\]
The new disk is a second \(2\)-cell whose boundary is attached along the \(a\)-circle. Thus a CW structure for \(X\) has one \(0\)-cell, \(1\)-cells \(a,b\), and two \(2\)-cells with attaching words
\[
[a,b]\quad\text{and}\quad a.
\]
Van Kampen gives
\[
\pi_1(X)\cong\langle a,b\mid [a,b],a\rangle\cong\langle b\rangle\cong\mathbb Z.
\]
This answers both parts: the displayed cells give the requested CW complex, and its fundamental group is infinite cyclic.
:::
