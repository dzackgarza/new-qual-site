---
title: Matrix analysis
order: 1
problems:
  topics:
  - Hermitian Matrices
  - Singular Values
  - Positive Definite Matrices
  - Normal Operators
  - Norms
  - Inner Product Spaces
---

# Matrix analysis

Linear algebra over $\CC$ with an inner product, where the questions are about norms, eigenvalue location, and factorizations rather than canonical forms.

## The classes, and what each guarantees

| $A$ is | Means | Gives |
| --- | --- | --- |
| Hermitian | $A^* = A$ | real eigenvalues, orthogonal eigenvectors |
| positive definite | Hermitian, $x^*Ax > 0$ | positive eigenvalues, a Cholesky factorization, a unique positive square root |
| unitary | $A^*A = I$ | eigenvalues on the unit circle, preserves the norm |
| normal | $A^*A = AA^*$ | unitarily diagonalizable, and this is exactly the class that is |

Normal is the largest of these and is the right hypothesis for the spectral theorem: Hermitian, unitary and skew-Hermitian are all special cases, and the theorem is that unitary diagonalizability *characterizes* normality.

## The factorizations

- **Spectral:** $A = U\Lambda U^*$ for normal $A$.

- **Singular value:** $A = U\Sigma V^*$ for any $A$, with $\Sigma$ the nonnegative square roots of the eigenvalues of $A^*A$.
  This is the tool when $A$ is not square or not normal, and it is what makes the operator norm computable: $\norm A_2 = \sigma_{\max}$.

- **Cholesky:** $A = LL^*$ for positive definite $A$.

- **QR:** Gram--Schmidt, stated as a factorization.

## Eigenvalue location without computing

- **Gershgorin:** every eigenvalue lies in some disc centred at a diagonal entry with radius the absolute row sum off the diagonal.
  A disjoint disc contains exactly one eigenvalue, which is how the discs are used.

- **Rayleigh quotients and Courant--Fischer:** the eigenvalues of a Hermitian matrix are the min-max values of $x^*Ax/x^*x$, which gives interlacing under rank-one perturbation.

- **Trace and determinant** bound the spectrum crudely and are worth checking first.

## Norms

For estimates involving products, use a submultiplicative norm: $\norm{AB}\leq\norm A\norm B$.
The entrywise max norm fails this inequality and is the standard trap.
The spectral radius is at most every submultiplicative norm, with equality in the limit: $\rho(A) = \lim \norm{A^n}^{1/n}$.
