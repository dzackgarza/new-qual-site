---
title: The spectral theorem
order: 60
topics:
- Diagonalization
- Spectral Theorem
- Inner Product Spaces
- Bilinear Forms
- Quadratic Forms
- Dual Spaces
- Functional Analysis
---

# The spectral theorem

A real symmetric or complex Hermitian matrix is diagonalizable in an orthonormal basis of eigenvectors, and the two classes of matrices are the ones whose diagonalizing change of basis can be taken orthogonal or unitary.

[[D-DVLK5]] [[D-BSUV4]]

## Diagonalizability

[[FD-K6FVX]]

[[L-C5DDK]]

[[FT-BC6S2]]

[[P-7IYBS]]

## The spectral theorem

[[T-WQHMA]]

[[E-LJ7PF]]

The converse holds as well and is short: if $Q^tAQ = D$ with $Q$ orthogonal and $D$ diagonal, then $A = QDQ^t$ and $A^t = QD^tQ^t = A$, so a matrix that is orthogonally diagonalizable is symmetric; the unitary statement with $Q^{\dagger}$ in place of $Q^t$ shows the same way that a unitarily diagonalizable matrix is normal.

## Simultaneous diagonalization

[[PR-GV5CF]]

::: {.example title="Noncommuting diagonalizable operators"}
The matrices $A = \matt{1}{0}{0}{2}$ and $B = \matt{0}{1}{1}{0}$ are diagonalizable over $\RR$ and do not commute.
They are not simultaneously diagonalizable: the eigenvectors of $A$ are the multiples of $e_1$ and of $e_2$, and neither $e_1$ nor $e_2$ is an eigenvector of $B$.
:::
