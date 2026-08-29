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
---

::: problem
Discuss sufficient conditions on a polynomial of degree 5 to have Galois group $S_5$ over $\QQ$ and prove your statements.
:::

::: {.solution}
<1>1. Let $f \in \QQ[x]$ be an irreducible polynomial of degree $5$.
Proof: setup.

<1>2. The Galois group $G = \operatorname{Gal}(f)$ is a transitive subgroup of $S_5$ (it acts transitively on the $5$ roots).
Proof: $f$ is irreducible, so $G$ acts transitively on the roots.

<1>3. If $f$ has exactly two non-real roots (and three real roots), then complex conjugation acts as a transposition on the roots, so $G$ contains a transposition.
Proof: complex conjugation fixes the three real roots and swaps the two non-real roots.

<1>4. If $f$ has a root $\alpha$ such that $[\QQ(\alpha) : \QQ] = 5$ (automatic by irreducibility) and $G$ contains a transposition, then $G = S_5$.
Proof: a transitive subgroup of $S_5$ containing a transposition is all of $S_5$ (a standard fact: a transitive subgroup of $S_p$ for prime $p$ containing a transposition is $S_p$).

<1>5. Hence a sufficient condition: $f$ is irreducible of degree $5$ and has exactly two non-real roots.
Proof: <1>2–<1>4.

<1>6. Another sufficient condition: $f$ is irreducible of degree $5$ and $G$ contains both a transposition and a $5$-cycle (equivalently, $f$ has exactly two non-real roots, which gives the transposition, and irreducibility gives the $5$-cycle).
Proof: <1>4 (the $5$-cycle comes from transitivity, and the transposition from the two non-real roots).

<1>7. Q.E.D.
Proof: <1>5 and <1>6.
:::
