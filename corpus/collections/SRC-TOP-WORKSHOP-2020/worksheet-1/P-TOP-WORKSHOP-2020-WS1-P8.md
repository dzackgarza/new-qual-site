---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P8
kind: problem
title: Simplicial homology of the connected sum of two projective planes via a $\Delta$-complex structure
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Cell Complexes
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
(May 2016) Construct a $\Delta$-complex structure, and use it to compute the simplicial homology groups, for the connected sum of two projective planes.
:::

::: solution
**Theorem.**  
Let $K=\mathbb{R}P^2\#\mathbb{R}P^2$.
Then
$$
H_0(K)\cong\mathbb Z,\qquad
H_1(K)\cong\mathbb Z\oplus\mathbb Z/2,\qquad
H_2(K)=0.
$$

**Proof.**

1. Realize each copy of $\mathbb RP^2$ by a 2-simplex quotient with one 0-cell $v$, one 1-cell $a$, and one 2-cell.
2. Remove open disks from the two $\mathbb RP^2$ pieces and glue the circular boundaries.
This gives a $\Delta$-complex with:
   - one 0-simplex $v$,
   - two 1-simplices $a,b$,
   - one 2-simplex $f$.
   This is the standard Klein-bottle complex; $K\cong \mathbb RP^2\#\mathbb RP^2$.

3. The attaching map of $f$ follows the edge word $a b a b^{-1}$.

4. The simplicial chain groups are
$$
C_2\cong\mathbb Z\langle f\rangle,\quad
C_1\cong\mathbb Z\langle a,b\rangle,\quad
C_0\cong\mathbb Z\langle v\rangle.
$$
   The boundary map $\partial_1$ is zero because there is only one vertex.

5. The cellular boundary $\partial_2$ is the sum over the boundary word:
$$
\partial_2(f)=2a.
$$
   (Reading the edge loop $a b a b^{-1}$ contributes $a+a- a-a$ in chains, which reduces to $2a$ after cancellation over $\mathbb Z$.)

6. Therefore
$$
H_2(K)=\ker\partial_2/\mathrm{im}\,\partial_3\cong0
$$
because $\partial_2\neq 0$ is injective from $\mathbb Z\to\mathbb Z^2$.

7. Also
$$
H_1(K)=\ker\partial_1/\mathrm{im}\,\partial_2
\cong \mathbb Z^2/\langle 2a\rangle
\cong \mathbb Z\oplus\mathbb Z/2.
$$

8. Since the complex is connected, $\ker\partial_1\cong C_0$, so $H_0(K)\cong\mathbb Z$.

Hence the homology groups are the stated groups. ∎
:::
