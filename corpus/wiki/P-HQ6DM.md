---
schema: qual/card@1
id: P-HQ6DM
kind: problem
title: "Definition: We say $A \\sim B$ in $M_n(R)$ $\\iff$ there exists an invertible $P$ such that $B=PAP\\inv$."
classification:
  areas:
  - algebra
  topics:
  - matrices
  - canonical-forms
  - smith-normal-form
relations: []
review: draft
---

::: problem
**Definition:** We say $A \sim B$ in $M_n(R)$ $\iff$ there exists an invertible $P$ such that $B=PAP\inv$.

- Reflexive, $A\sim A$:

  Take $P = I_n$ the identity matrix.

- Symmetric, $A\sim B \implies B \sim A$:

  $B = PAP\inv \implies BP = PA \implies P\inv B P = A$, so we can take $Q = P\inv$ to yield $A = Q B Q\inv$.

- Transitive, $A\sim B \& B\sim C \implies A \sim C$:

  If $B = PAP\inv, C = QBQ\inv$, then $C = Q(PAP\inv)Q\inv = (QP) A (QP)\inv$, so take $L = QP$ to yield $C = LAL\inv$.

**Definition:** We say $A \sim B$ in $M(n\times n, R)$ $\iff$ $B = PAQ$ with $P \in \GL(n, R), Q \in \GL(m, R)$.

- Reflexive, $A\sim A$:

  Take $P = I_{m, n}$ the matrix with $1$s on the diagonal and zeros elsewhere, and $Q = P^t$.

- Symmetric, $A\sim B \implies B \sim A$:

  $B = PAQ \implies BQ\inv = PA \implies P\inv B Q\inv = A$, so we can take $S = P\inv, T = Q\inv$ to yield $A = Q B T$.

- Transitive, $A\sim B \& B\sim C \implies A \sim C$:

  If $B = PAQ, C = RBS$, then $C = R(PAQ)S = (RP) A (QS)$, so take $L = RP, M  = QS$ to yield $C = LAM$.
:::
