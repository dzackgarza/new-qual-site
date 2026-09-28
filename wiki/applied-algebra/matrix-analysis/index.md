---
title: Matrix analysis
order: 1
topics:
- Hermitian Matrices
- Singular Values
- Positive Definite Matrices
- Normal Operators
- Norms
- Inner Product Spaces
---

# Matrix analysis

Throughout, $A$ is a complex $n\times n$ matrix, $A^*$ is its conjugate transpose, and $\CC^n$ has the standard inner product.

## Classes of matrices

| $A$ is | Definition | Consequences |
| --- | --- | --- |
| Hermitian | $A^* = A$ | real eigenvalues; eigenvectors for distinct eigenvalues are orthogonal |
| positive definite | $A^* = A$ and $x^*Ax > 0$ for all $x\neq0$ | positive eigenvalues; a Cholesky factorization; a unique positive definite square root |
| unitary | $A^*A = I$ | eigenvalues of absolute value $1$; $\norm{Ax} = \norm x$ for all $x$ |
| normal | $A^*A = AA^*$ | unitarily diagonalizable |

Hermitian, skew-Hermitian, and unitary matrices are normal, and by the spectral theorem $A$ is unitarily diagonalizable if and only if $A$ is normal.

## Factorizations

- **Spectral decomposition.** $A = U\Lambda U^*$ with $U$ unitary and $\Lambda$ diagonal, for normal $A$.

- **Singular value decomposition.** Every $m\times n$ complex matrix has a factorization $A = U\Sigma V^*$ with $U$ and $V$ unitary and $\Sigma$ an $m\times n$ diagonal matrix whose diagonal entries are the singular values of $A$, the nonnegative square roots of the eigenvalues of $A^*A$.
  The operator norm is $\norm A_2 = \sigma_{\max}$, the largest singular value.

- **Cholesky factorization.** $A = LL^*$ with $L$ lower triangular with positive diagonal entries, for positive definite $A$.

- **QR factorization.** $A = QR$ with $Q$ unitary and $R$ upper triangular; for invertible $A$ it is Gram--Schmidt orthonormalization applied to the columns of $A$.

## Eigenvalue location

- **Gershgorin.** Every eigenvalue of $A=(a_{ij})$ lies in some disc $\ts{z \st \abs{z-a_{ii}}\leq\sum_{j\neq i}\abs{a_{ij}}}$.
  A union of $k$ discs disjoint from the other $n-k$ discs contains exactly $k$ eigenvalues, counted with multiplicity.

- **Courant--Fischer.** For Hermitian $A$ with eigenvalues $\lambda_1\geq\cdots\geq\lambda_n$, $\lambda_k = \max_{\dim S = k}\min_{0\neq x\in S} x^*Ax/x^*x$.
  Hence the eigenvalues of $A$ and of $A + vv^*$ interlace.

- **Trace and determinant.** $\tr A = \sum_i\lambda_i$ and $\det A = \prod_i\lambda_i$.

## Norms

A matrix norm is submultiplicative if $\norm{AB}\leq\norm A\norm B$ for all $A,B$; operator norms are submultiplicative.

::: {.example}
The entrywise maximum norm $\norm A_{\max} = \max_{i,j}\abs{a_{ij}}$ is not submultiplicative: for $A = \matt{1}{1}{1}{1}$, $\norm{A^2}_{\max} = 2 > 1 = \norm A_{\max}^2$.
:::

For every submultiplicative norm, the spectral radius satisfies $\rho(A)\leq\norm A$, and $\rho(A) = \lim_{k\to\infty} \norm{A^k}^{1/k}$ by Gelfand's formula.
