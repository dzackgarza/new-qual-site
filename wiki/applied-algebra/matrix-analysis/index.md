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

The adjoint, symmetric, Hermitian, orthogonal, unitary, positive definite, and normal matrices are defined on [[D-DVLK5|adjoint, symmetric, Hermitian, orthogonal, unitary, positive definite, and normal matrices]].
A Hermitian matrix has real eigenvalues, and eigenvectors for distinct eigenvalues are orthogonal ([[T-WQHMA|the spectral theorem for Hermitian and real symmetric matrices]]); a matrix is unitarily diagonalizable if and only if it is normal, [[T-SPRTR|which characterises the normal matrices]].

## Factorizations

The spectral decomposition $A = U\Lambda U^*$, with $U$ unitary and $\Lambda$ diagonal, exists if and only if $A$ is normal ([[T-SPRTR]]).

Every $m\times n$ complex matrix has a singular value decomposition $A = U\Sigma V^*$, with $U$ and $V$ unitary and $\Sigma$ an $m\times n$ diagonal matrix whose diagonal entries are the singular values of $A$, the nonnegative square roots of the eigenvalues of $A^*A$; the operator norm is then $\norm A_2 = \sigma_{\max}$, the largest singular value ([[P-U547U|the singular value decomposition]], with its proof).

A positive definite $A$ has a Cholesky factorization $A = LL^*$, with $L$ lower triangular of positive diagonal, and a unique positive definite square root; the factorization is stated in the upper triangular form $A = R^tR$ on [[P-BKF20-6A|Cholesky factorization and a related similarity]].

An invertible $A$ has a QR factorization $A = QR$, with $Q$ unitary and $R$ upper triangular of positive diagonal, unique in this normalization ([[P-BKS83-11|QR decomposition with positive diagonal]]); for a real invertible $A$ it is Gram--Schmidt orthonormalization applied to the columns.

## Eigenvalue location

Every eigenvalue of $A = (a_{ij})$ lies in one of the discs $\theset{z\st\abs{z-a_{ii}}\leq\sum_{j\neq i}\abs{a_{ij}}}$ ([[P-APAS24B|Gershgorin discs contain every eigenvalue]]).

For a Hermitian $A$ with eigenvalues $\lambda_1\geq\cdots\geq\lambda_n$,
$$
\lambda_k = \max_{\dim S = k}\min_{0\neq x\in S} \frac{x^*Ax}{x^*x},
$$
by [[P-UCLAB10S-02|the Courant--Fischer characterization of the ordered eigenvalues]]; the same characterization shows that the eigenvalues of $A$ and of $A + vv^*$ interlace.

The trace and the determinant are the coefficients of $t^{n-1}$ and $t^0$ in the characteristic polynomial, so $\tr A = \sum_i\lambda_i$ and $\det A = \prod_i\lambda_i$.

## Norms

A matrix norm is submultiplicative when $\norm{AB}\leq\norm A\norm B$ for all $A$ and $B$; an operator norm is submultiplicative, since $\norm{ABx}\leq\norm A\norm{Bx}\leq\norm A\norm B\norm x$.

::: {.example}
The entrywise maximum norm $\norm A_{\max} = \max_{i,j}\abs{a_{ij}}$ is not submultiplicative: for $A = \matt{1}{1}{1}{1}$, $\norm{A^2}_{\max} = 2 > 1 = \norm A_{\max}^2$.
:::

[[T-GELFND|Gelfand's formula]] gives $\rho(A) = \lim_{k\to\infty}\norm{A^k}^{1/k}$ for every norm on $M_n(\CC)$, and for a submultiplicative norm also $\rho(A)\leq\norm A$ and $\rho(A)=\inf_k\norm{A^k}^{1/k}$: the infimum is the sharper bound, which the limit attains.
