---
schema: qual/card@1
id: P-HHJEA
kind: problem
title: Groups of order $p^n$ are solvable, and groups of order $p^r q^s$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
  - Sylow Theory
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
Can you show that all groups of order $p^n$ for $p$ prime are solvable?
Do you know how to do this for groups of order $p^r q^s$?
:::


::: {.solution}
<1>1. Every finite $p$-group is solvable.
::: {.proof}
We argue by induction on $|G|$. The trivial group is solvable. Let $G$ be a nontrivial finite $p$-group. Its center $Z(G)$ is nontrivial. Hence
\[
1<|Z(G)|<|G|
\]
unless $G$ is abelian, in which case $G$ is already solvable.

The quotient $G/Z(G)$ is a smaller $p$-group, so by induction it is solvable. The center $Z(G)$ is abelian, hence solvable. An extension of a solvable group by a solvable group is solvable, so $G$ is solvable.
:::

<1>2. More generally, every finite group of order
\[
p^r q^s
\]
with $p,q$ prime is solvable.
::: {.proof}
This is Burnside's $p^a q^b$ theorem. Unlike the $p$-group case, the general proof is not a direct induction from the class equation; the classical proof uses character theory (and there are later character-free proofs). Applying Burnside's theorem with $a=r$ and $b=s$ gives the result.
:::
:::
