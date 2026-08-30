---
schema: qual/card@1
id: P-CLXFD
kind: problem
title: Galois groups of irreducible cubics
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
What are the Galois groups of irreducible cubics?
:::

::: {.solution}
<1>1. Let $f \in F[x]$ be irreducible of degree $3$.
Proof: setup.

<1>2. The Galois group $G = \operatorname{Gal}(f)$ embeds as a transitive subgroup of $S_3$.
Proof: $G$ acts faithfully and transitively on the three roots (irreducibility).

<1>3. The transitive subgroups of $S_3$ are $A_3 \cong \mathbb{Z}/3$ and $S_3$ itself.
Proof: classification ($|G|$ is divisible by $3$, and the only transitive subgroups of $S_3$ are $A_3$ and $S_3$).

<1>4. $G \cong A_3$ iff the discriminant $\Delta(f)$ is a square in $F$; otherwise $G \cong S_3$.
Proof: $G \le A_3$ iff $G$ consists of even permutations iff $\sqrt{\Delta} \in F$.

<1>5. Hence the Galois group of an irreducible cubic is $A_3$ (cyclic of order $3$) when the discriminant is a square in $F$, and $S_3$ (of order $6$) otherwise.
Proof: <1>3 and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
