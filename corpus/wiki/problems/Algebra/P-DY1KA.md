---
schema: qual/card@1
id: P-DY1KA
kind: problem
title: Matrices with the same Jordan form are similar
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Canonical Forms
relations: []
review: draft
---

::: problem
By part (1), we know that these conditions uniquely specify their Jordan forms, so we have $M\definedas JCF(T) = JCF(S)$.

Moreover, since $M = JCF(T)$, we know there is a matrix $P$ such that $T = PMP\inv$.

Similarly, we know there is a matrix $Q$ such that $S = QMQ\inv$.

But then $P\inv TP = M$, and so
$$
S = QMQ\inv = Q(P\inv T P) Q\inv = (QP\inv) T (QP\inv)\inv \definedas ATA\inv
$$

where $A = QP\inv$ is a product of invertible matrices and thus invertible.
:::
