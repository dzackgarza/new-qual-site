---
schema: qual/card@1
id: P-KQ3DJ
kind: problem
title: Projective module
classification:
  areas:
  - algebra
  topics:
  - Projective Modules
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is a projective module? Give standard equivalent characterizations.
:::

::: {.solution}
An $R$-module $P$ is **projective** if it has the following lifting property: whenever
\[
M\twoheadrightarrow N
\]
is a surjective $R$-linear map and $f:P\to N$ is any $R$-linear map, there exists $\widetilde f:P\to M$ such that the triangle commutes:
\[
P\xrightarrow{\widetilde f}M\twoheadrightarrow N
\quad=\quad
P\xrightarrow{f}N.
\]

The following are equivalent:

1. $P$ is projective.
2. Every short exact sequence
   \[
   0\to A\to B\to P\to0
   \]
   splits.
3. $P$ is a direct summand of a free module: there is a module $Q$ and a free module $F$ with
   \[
   F\cong P\oplus Q.
   \]
4. The functor
   \[
   \Hom_R(P,-)
   \]
   is exact.

Every free module is projective. Over a PID, every submodule of a free module is free, and every finitely generated projective module is free; over a general ring, projective modules need not be free.
:::
