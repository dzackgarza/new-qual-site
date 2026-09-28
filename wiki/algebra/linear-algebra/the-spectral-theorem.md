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

A real symmetric or complex Hermitian matrix is diagonalizable in an orthonormal basis of eigenvectors.

::: {.remark title="Notation"}
For a matrix $A$, $A^t$ is the transpose and $A^{\dagger}$ the conjugate transpose, and $\inner{\cdot}{\cdot}$ is the standard inner product on $\RR^n$ or $\CC^n$.

- The \dfn{adjoint} of $A$ is the matrix $A^{\dagger}$, characterized by $\inner{A\vector x}{\vector y} = \inner{\vector x}{A^{\dagger} \vector y}$ for all $\vector x,\vector y$, and $A$ is \dfn{self-adjoint} if $A=A^\dagger$.

- A real matrix $A$ is \dfn{symmetric} if $A = A^t$, and \dfn{orthogonal} if $A^tA = AA^t = I$.

- A complex matrix $A$ is \dfn{Hermitian} if $A^{\dagger} = A$, [[D-BSUV4|normal]] if $AA^{\dagger} = A^{\dagger}A$, and \dfn{unitary} if $A^{\dagger}A = AA^{\dagger} = I$.
:::

## Diagonalizability

[[FD-K6FVX]]

[[L-C5DDK]]

[[T-6ABNR]]

[[FT-BC6S2]]

::: {.proof}
$\impliedby$: If $\min_A$ is a product of distinct linear factors, then every invariant factor of $A$ divides $\min_A$, so every elementary divisor is linear, and the Jordan form of $A$ is diagonal.
:::

::: {.remark title="Criterion"}
$A$ is diagonalizable over $F$ if and only if $\min_A$ is a product of distinct linear factors over $F$.
Hence a polynomial identity $f(A) = 0$ with $f$ a product of distinct linear factors over $F$, such as $A^2 = A$, implies that $A$ is diagonalizable; see [[algebra/linear-algebra/find-the-canonical-form|Find the canonical form]].
:::

## The spectral theorem

[[T-WQHMA]]

::: {.remark}
A real matrix $A$ is diagonalizable by an orthogonal matrix if and only if $A$ is symmetric: if $Q^tAQ = D$ with $Q$ orthogonal and $D$ diagonal, then $A = QDQ^t$ and $A^t = QD^tQ^t = A$.
A complex matrix is diagonalizable by a unitary matrix if and only if it is normal.
:::

::: {.proof title="of the spectral theorem"}
\envlist

- Let $A$ be Hermitian, and let $\lambda$ be an eigenvalue of $A$ with unit eigenvector $\vector v$, which exists over $\CC$.
  Then
$$
\lambda = \lambda\inner{\vector v}{\vector v} = \inner{A\vector v}{\vector v} = \inner{\vector v}{A\vector v} = \overline{\lambda},
$$
so $\lambda \in \RR$.
A real symmetric matrix is Hermitian, so its eigenvalues are real, and it has a real unit eigenvector.

- Let $W = \ts{\vector v}^\perp$.
  For $\vector w \in W$,
$$
\inner{\vector v}{ A \vector w} =
\inner{A \vector v}{\vector w} =
\lambda \inner{\vector v}{\vector w} = 0,
$$
so $A(W)\subseteq W$, and the restriction of $A$ to $W$ is again self-adjoint.

- By induction on the dimension, $W$ has an orthonormal basis of eigenvectors of $A$, and adjoining $\vector v$ gives an orthonormal basis of eigenvectors of $A$ for the whole space.
:::

## Simultaneous diagonalization

[[PR-GV5CF]]

::: {.proof}
Suppose $A_1,\ldots,A_n$ are pairwise commuting diagonalizable operators on $V$; we induct on $n$.

- Since $A_n$ is diagonalizable, $V = \bigoplus_i E_i$, where $E_i$ is the eigenspace of $A_n$ for the eigenvalue $\mu_i$.

- If $A_jA_n = A_nA_j$ and $\vector v\in E_i$, then $A_n(A_j\vector v) = A_jA_n\vector v = \mu_iA_j\vector v$, so each $E_i$ is $A_j$-invariant.

- The minimal polynomial of the restriction $A_j|_{E_i}$ divides that of $A_j$, so $A_j|_{E_i}$ is diagonalizable.

- By induction, $A_1|_{E_i},\ldots,A_{n-1}|_{E_i}$ are simultaneously diagonalizable, and every vector of $E_i$ is an eigenvector of $A_n$.

- The union over $i$ of these bases of $E_i$ is a basis of $V$ in which every $A_j$ is diagonal.
:::

::: {.example title="Noncommuting diagonalizable operators"}
The matrices $A = \matt{1}{0}{0}{2}$ and $B = \matt{0}{1}{1}{0}$ are diagonalizable over $\RR$ and do not commute.
They are not simultaneously diagonalizable: the eigenvectors of $A$ are the multiples of $e_1$ and of $e_2$, and neither $e_1$ nor $e_2$ is an eigenvector of $B$.
:::
