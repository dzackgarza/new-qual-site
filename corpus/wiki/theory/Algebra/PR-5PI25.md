---
schema: qual/card@1
id: PR-5PI25
kind: proposition
title: Recognizing $A_n$ or $S_n$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Galois Theory
relations: []
review: draft
---

::: {.proposition}
Useful fact: if $G \leq S_n$ for $n$ prime contains a 2-cycle and a $p\dash$cycle, then $G\cong S_n$.
Note that for $n$ not prime, a transposition and an $n\dash$cycle isn't enough, since one needs the specific $n\dash$cycle $(1,2,\cdots,n)$ in general.

If $n>2$ and $G$ contains a 3-cycle and an $n\dash$cycle, then $G = A_n$ or $S_n$.
Note that by Orbit-Stabilizer $n\divides \size G$, and if $n$ is prime then by Cauchy there is an $n\dash$cycle (but this is not always the case).
In fact, it suffices to find a $k\dash$cycle for any $k\geq n/2$, which can be found by reducing mod $p$ and examining cycle types.

Moreover, if $G$ contains a 2-cycle (transposition), then $G = S_n$.
:::
