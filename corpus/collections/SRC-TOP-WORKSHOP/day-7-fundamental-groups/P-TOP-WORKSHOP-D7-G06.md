---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G06
kind: problem
title: A torus with a disk attached along the diagonal
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
(June ’08) Attach a $2$-disk $D^2$ to a torus $S^1\times S^1$ by the attaching map $e^{2\pi it}\mapsto(e^{2\pi it},e^{2\pi it})$, thinking of the boundary $\partial D^2$ and each $S^1$ factor as the unit circle in the complex plane, and let $X$ be the resulting space.
Compute a presentation for the fundamental group of $X$.
:::

::: {.solution}
Let \(a,b\) be the standard generators of
\[
\pi_1(T^2)\cong\langle a,b\mid [a,b]=1\rangle.
\]
The attaching map winds once positively around each circle factor, so its class is \(ab\). Attaching the disk kills this element. Hence
\[
\pi_1(X)\cong\langle a,b\mid [a,b],ab\rangle.
\]
From \(ab=1\) we obtain \(b=a^{-1}\), after which the commutator relation is automatic. Therefore
\[
\boxed{\pi_1(X)\cong\mathbb Z}.
\]
:::
