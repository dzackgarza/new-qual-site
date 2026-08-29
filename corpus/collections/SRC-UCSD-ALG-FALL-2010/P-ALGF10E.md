---
schema: qual/card@1
id: P-ALGF10E
kind: problem
title: "Intermediate extensions of abelian Galois extensions are Galois"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $E$ be a finite-dimensional Galois extension of a field $F$ and let $G = \operatorname{Gal}(E/F)$.
Suppose that $G$ is an abelian group.
Prove that if $K$ is any field between $E$ and $F$, then $K$ is a Galois extension of $F$.
What is the Galois group of $K$ over $F$?
:::

::: {.solution}
<1>1. By the fundamental theorem of Galois theory, $K$ corresponds to a subgroup $H = \operatorname{Gal}(E/K) \le G$.
Proof: Galois correspondence.

<1>2. Since $G$ is abelian, every subgroup $H \le G$ is normal.
Proof: abelian groups have all subgroups normal.

<1>3. Hence $K/F$ is Galois (a subgroup $H$ corresponds to a Galois intermediate field iff $H$ is normal in $G$).
Proof: <1>2 and the fundamental theorem.

<1>4. The Galois group of $K$ over $F$ is $\operatorname{Gal}(K/F) \cong G/H$.
Proof: fundamental theorem of Galois theory.

<1>5. Q.E.D.
Proof: <1>3 and <1>4.
:::
