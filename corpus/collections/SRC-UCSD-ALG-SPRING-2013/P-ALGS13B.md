---
schema: qual/card@1
id: P-ALGS13B
kind: problem
title: Projective modules over a commutative ring are flat
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Projective Modules
relations: []
review: draft

audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $A$ be a commutative ring.
Prove that any projective $A$-module is flat.
(Hint: first prove it for free modules).
:::

::: {.solution}
<1>1. Every free $A$-module is flat.
::: {.proof}
Let $F=igoplus_{i\in I}A$.
For every $A$-module $M$ there is a natural isomorphism
\[
M\otimes_A F\cong igoplus_{i\in I}(M\otimes_A A)\cong igoplus_{i\in I}M.
\]
Thus the functor $-\otimes_A F$ is naturally isomorphic to the direct-sum functor $M\mapstoigoplus_{i\in I}M$.
Direct sums of exact sequences of modules are exact, so $-\otimes_A F$ is exact.
Hence $F$ is flat.
:::

<1>2. A direct summand of a flat module is flat.
::: {.proof}
Suppose $N\cong P\oplus Q$ and $N$ is flat.
Then for every $A$-module $M$,
\[
M\otimes_A N\cong (M\otimes_A P)\oplus(M\otimes_A Q).
\]
Given an injection $u:M'\hookrightarrow M$, flatness of $N$ makes
\[
u\otimes 1_N:(M'\otimes_A P)\oplus(M'\otimes_A Q)\longrightarrow (M\otimes_A P)\oplus(M\otimes_A Q)
\]
injective.
Its restriction to the first direct summand is $u\otimes 1_P$, so $u\otimes 1_P$ is injective.
Since tensor product is always right exact, $-\otimes_A P$ is exact.
Thus $P$ is flat.
:::

<1>3. Every projective $A$-module is flat.
::: {.proof}
Let $P$ be projective.
There exists a free module $F$ and a module $Q$ such that
\[
F\cong P\oplus Q.
\]
By <1>1, $F$ is flat.
By <1>2, its direct summand $P$ is flat.
:::

<1>4. Therefore every projective module over a commutative ring is flat.
::: {.proof}
This is exactly <1>3.
:::
:::
