---
schema: qual/card@1
id: P-OERA3
kind: problem
title: Sufficient conditions for a degree $5$ polynomial to have Galois group $S_5$
  over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Discuss sufficient conditions on a polynomial of degree 5 to have Galois group $S_5$ over $\QQ$ and prove your statements.
:::

::: {.solution}
Let $f\in\mathbb Q[x]$ be irreducible of degree $5$, and let $G$ be its Galois group acting on the five roots. Irreducibility makes this action transitive.

If $f$ has exactly three real roots and one nonreal conjugate pair, complex conjugation fixes the three real roots and swaps the two nonreal roots. Thus $G$ contains a transposition.

A transitive subgroup $G\le S_5$ containing a transposition equals $S_5$: if $\tau=(a\ b)\in G$, then all conjugates $g\tau g^{-1}=(g(a)\ g(b))$ lie in $G$. Form the graph on the five roots whose edges are these conjugate transpositions. The graph is $G$-invariant and contains an edge; transitivity forces it to be connected. Transpositions along the edges of a connected graph generate the full symmetric group, so $S_5\le G$.

Hence a sufficient condition is:
\[
\boxed{f\text{ irreducible of degree }5\text{ and having exactly three real roots}.}
\]
Equivalently, it is enough that the transitive Galois group contain a transposition. Irreducibility also implies $5\mid |G|$, hence by Cauchy's theorem $G$ contains an element of order $5$, necessarily a $5$-cycle.
:::
