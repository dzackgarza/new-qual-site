---
schema: qual/card@1
id: P-VPB55
kind: problem
title: Jordan canonical form over a non-algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Canonical Forms
  - Rational Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Talk about Jordan canonical form.
What happens when the field is not algebraically closed?
:::

::: {.solution}
<1>1. Over an algebraically closed field $F$, every matrix is similar to its Jordan canonical form: a block-diagonal matrix of Jordan blocks $J_m(\lambda)$ (an $m \times m$ matrix with $\lambda$ on the diagonal, $1$'s on the superdiagonal, and $0$'s elsewhere).
Proof: the Jordan canonical form theorem.

<1>2. The Jordan form is determined by the generalized eigenspaces and the sizes of the Jordan blocks, which are determined by the ranks of $(A - \lambda I)^k$.
Proof: the structure of the Jordan form.

<1>3. When $F$ is not algebraically closed, the Jordan form may not exist over $F$ (the eigenvalues may not lie in $F$).
Proof: the Jordan form requires the characteristic polynomial to split into linear factors over $F$.

<1>4. Over a non-algebraically-closed field, the appropriate canonical form is the rational canonical form.
Proof: the rational canonical form exists over any field.

<1>5. The rational canonical form is a block-diagonal matrix of companion matrices of the invariant factors $d_1 \mid d_2 \mid \cdots \mid d_k$ (monic polynomials over $F$).
Proof: the rational canonical form theorem.

<1>6. The rational canonical form generalizes the Jordan form: over an algebraically closed field, the companion matrix of $(x - \lambda)^m$ is similar to the Jordan block $J_m(\lambda)$.
Proof: the companion matrix of $(x-\lambda)^m$ has a single eigenvalue $\lambda$ and a single Jordan block of size $m$.

<1>7. Q.E.D.
Proof: <1>1–<1>6.
:::
