---
schema: qual/card@1
id: P-PRX3C
kind: problem
title: Prime and maximal ideals, with examples in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - prime-ideals
  - maximal-ideals
  - ideals
relations: []
review: draft
solved: true
---

a. Define *prime ideal*, give an example of a nontrivial ideal in the ring $\ZZ$ that is not prime, and prove that it is not prime.

b. Define *maximal ideal*, give an example of a nontrivial maximal ideal in $\ZZ$ and prove that it is maximal.

::: {.solution}
\envlist

- $\mfp$ is **prime** iff $xy\in \mfp \implies x\in \mfp$ or $y\in \mfp$.

  - An ideal $I\normal \ZZ$ that is not prime: $I \da 8\ZZ$.

  - For example, $2\cdot 4\in 8\ZZ$ but neither 2 nor 4 is a multiple of 8.

- $\mfm$ is **maximal** iff whenever $I\contains \mfm$ is an ideal in $R$, then either $I=\mfm$ or $I = R$.

  - A maximal ideal in $\ZZ$: $p\ZZ$.
    This is because primes are maximal in a PID and $p\ZZ$ is a prime ideal.
    Alternatively, "to contain is to divide" holds for Dedekind domains, so $m\ZZ \contains p\ZZ \iff m\divides p$, which forces $m=1,p$, so either $m\ZZ = p\ZZ$ or $m\ZZ = \ZZ$.
:::
