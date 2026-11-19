---
schema: qual/card@1
id: T-SPRTR
kind: theorem
title: Orthogonal and unitary diagonalizability characterize symmetric and normal matrices
slogan: 'A real matrix is symmetric exactly when an orthogonal change of basis diagonalizes it; a complex matrix is normal exactly when a unitary one does.'
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Spectral Theorem
  - Inner Product Spaces
relations: []
review: draft
---

::: {.theorem}
Let $A\in\Mat_n(\RR)$.
Then $A$ is symmetric if and only if there is an orthogonal $Q$ with $Q^tAQ$ diagonal.

Let $A\in\Mat_n(\CC)$.
Then $A$ is normal if and only if there is a unitary $U$ with $U^{\dagger}AU$ diagonal.
:::

::: {.proof}
If $Q$ is orthogonal and $D=Q^tAQ$ is diagonal, then $A=QDQ^t$ and
$$
A^t = (QDQ^t)^t = QD^tQ^t = QDQ^t = A,
$$
so $A$ is symmetric.
If $U$ is unitary and $D=U^{\dagger}AU$ is diagonal, then $A=UDU^{\dagger}$ and
$$
A^{\dagger}A = UD^{\dagger}U^{\dagger}UDU^{\dagger} = UD^{\dagger}DU^{\dagger} = UDD^{\dagger}U^{\dagger} = AA^{\dagger},
$$
so $A$ is normal, since $D$ is diagonal.

The other directions are the [[T-WQHMA|spectral theorem]] for symmetric and Hermitian matrices, together with [[E-LJ7PF|the unitary diagonalizability of normal matrices]].
:::
