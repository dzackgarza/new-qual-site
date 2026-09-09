---
schema: qual/card@1
id: P-OU7QZ
kind: problem
title: The Galois group of an irreducible quintic with two non-real roots is $S_5$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
---

::: problem
Let $f\in \QQ[x]$ be an irreducible quintic with exactly two non-real roots. Prove that its Galois group over $\QQ$ is $S_5$.
:::

::: {.solution}
Let $L$ be the splitting field and let
\[
G=\operatorname{Gal}(L/\QQ)\le S_5
\]
act on the five roots.

Because $f$ is irreducible, this action is transitive. Hence $5\mid |G|$, so by Cauchy's theorem $G$ contains an element of order $5$, necessarily a $5$-cycle.

Since $f$ has rational coefficients and exactly two non-real roots, complex conjugation fixes the three real roots and swaps the two non-real conjugate roots. Thus complex conjugation acts as a transposition in $G$.

A $5$-cycle together with any transposition generates $S_5$: after conjugating the transposition by powers of the $5$-cycle one obtains enough adjacent/star transpositions to generate all of $S_5$. Therefore
\[
G=S_5.
\]
:::
