---
schema: qual/card@1
id: E-HAT-1.1-8
kind: problem
title: Borsuk–Ulam theorem for the torus
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fixed Point Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used projection to the first circle, viewed as the unit circle in the plane, to give an explicit counterexample.
---

Does the Borsuk–Ulam theorem hold for the torus?
In other words, for every map $f: S^1 \times S^1 \longrightarrow \mathbb{R}^2$ must there exist $(x, y) \in S^1 \times S^1$ such that $f(x, y) = f(-x, -y)$?

::: {.solution}
No.

<1>1. Regard $S^1$ as the unit circle in $\mathbb R^2$ and define
\[
f:S^1\times S^1\to\mathbb R^2,
\qquad
f(x,y)=x.
\]
::: {.proof}
This is the composition of the projection
\[
S^1\times S^1\to S^1,
\qquad (x,y)\mapsto x,
\]
with the inclusion $S^1\hookrightarrow\mathbb R^2$, so it is continuous.
:::

<1>2. For every $(x,y)\in S^1\times S^1$,
\[
f(-x,-y)=-x\ne x=f(x,y).
\]
::: {.proof}
If $x=-x$ as a vector in $\mathbb R^2$, then $2x=0$, hence $x=0$.
But $x\in S^1$ has norm $1$, so this is impossible.
:::

<1>3. Therefore the stated Borsuk--Ulam analogue fails for the torus.
::: {.proof}
The continuous map in <1>1 has no point satisfying the required equality by <1>2.
:::
:::
