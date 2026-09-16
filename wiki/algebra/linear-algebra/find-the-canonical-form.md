---
title: Find the canonical form
order: 0
topics:
- Linear Algebra
- Matrices
---

# Find the canonical form

Throughout, $A$ is an $n\times n$ matrix over a field $F$, $\chi_A(t) = \det(tI-A)$ is its characteristic polynomial, and $\min_A$ is its minimal polynomial.

## The forms and the relations they classify

| Setting | Equivalence relation | Normal form |
| --- | --- | --- |
| $\chi_A$ splits over $F$ | similarity | [[algebra/linear-algebra/jordan-canonical-form\|Jordan canonical form]] |
| any field $F$ | similarity | [[algebra/linear-algebra/rational-canonical-form\|rational canonical form]] |
| matrices over a PID; finitely generated modules | equivalence of matrices; isomorphism of modules | [[algebra/linear-algebra/smith-normal-form\|Smith normal form]] |
| real symmetric or complex normal matrices | orthogonal or unitary similarity | [[algebra/linear-algebra/the-spectral-theorem\|spectral theorem]] |

The Jordan form of $A$ over $F$ exists if and only if $\chi_A$ splits over $F$.
The rational canonical form exists over every field.
Both come from the structure theorem for the finitely generated $F[t]$-module $F^n$ with $t$ acting by $A$: the Jordan form from its elementary divisors, the rational form from its invariant factors.

## Computation from a matrix

1. **Characteristic polynomial.** The roots of $\chi_A(t) = \det(tI - A)$ are the eigenvalues, with algebraic multiplicities.
   Also $\tr A = \sum\lambda_i$ and $\det A = \prod \lambda_i$, and the eigenvalues of a triangular matrix are its diagonal entries.

2. **Minimal polynomial.** $\min_A$ divides $\chi_A$ and has the same irreducible factors, so it is determined by the exponents of those factors; it is the monic divisor $p$ of $\chi_A$ of least degree, among those with every irreducible factor of $\chi_A$, such that $p(A) = 0$.

3. **Diagonalizability.** $A$ is diagonalizable over $F$ if and only if $\min_A$ is a product of distinct linear factors over $F$.
   In that case $A$ is similar to $\diag(\lambda_1,\ldots,\lambda_n)$, with each eigenvalue repeated according to its multiplicity in $\chi_A$.

4. **Jordan block sizes.** For each eigenvalue $\lambda$:

   - the exponent of $(t-\lambda)$ in $\min_A$ is the size of the largest Jordan block for $\lambda$;

   - the exponent of $(t-\lambda)$ in $\chi_A$ is the sum of the sizes of the Jordan blocks for $\lambda$;

   - $\dim\ker(A-\lambda I)$ is the number of Jordan blocks for $\lambda$.

   These three numbers determine the Jordan blocks for $\lambda$ when its algebraic multiplicity is at most $6$; for multiplicity $7$, the block sizes $3+3+1$ and $3+2+2$ share all three.
   In general, $\dim\ker(A-\lambda I)^k-\dim\ker(A-\lambda I)^{k-1}$ is the number of Jordan blocks for $\lambda$ of size at least $k$.

5. **Rational canonical form.** If $\chi_A$ does not split, the rational canonical form is the block diagonal matrix of the companion matrices of the invariant factors $p_1\divides\cdots\divides p_m$ of $tI-A$, and $p_m = \min_A$.

## Similarity classes from the two polynomials

Let $\chi_A = \prod_\lambda (t-\lambda)^{a_\lambda}$ and $\min_A = \prod_\lambda (t-\lambda)^{m_\lambda}$.
The similarity classes of matrices with these polynomials correspond to choices, for each eigenvalue $\lambda$, of a partition of $a_\lambda$ with largest part $m_\lambda$.

::: {.example}
For $\chi_A = (t-2)^4$ and $\min_A = (t-2)^2$, the partitions of $4$ with largest part $2$ are $2+2$ and $2+1+1$, so there are two similarity classes, $J_2(2)\oplus J_2(2)$ and $J_2(2)\oplus J_1(2)\oplus J_1(2)$.
:::

## Polynomial identities satisfied by $A$

If $f(A) = 0$ for a polynomial $f$, then $\min_A$ divides $f$.

| Hypothesis | Consequence for $\min_A$ |
| --- | --- |
| $A^2 = A$ | $\min_A \divides t^2 - t$, so $A$ is diagonalizable with eigenvalues in $\ts{0,1}$ |
| $A^k = I$ | $\min_A\divides t^k-1$; if $\operatorname{char} F \notdivides k$ and $t^k-1$ splits over $F$, then $A$ is diagonalizable over $F$ |
| $A^k = 0$ | $\min_A\divides t^k$, so $A$ is nilpotent and all its eigenvalues are $0$ |

In each diagonalizable case, the divisor $\min_A$ of a polynomial with distinct roots in $F$ is a product of distinct linear factors.

## Consistency conditions

- $\min_A$ and $\chi_A$ have the same irreducible factors.

- For each eigenvalue $\lambda$, the number of Jordan blocks equals the geometric multiplicity $\dim\ker(A-\lambda I)$, and the sum of their sizes equals the algebraic multiplicity.
  The geometric multiplicity is at most the algebraic multiplicity, and $A$ is diagonalizable over $F$ if and only if $\chi_A$ splits and the two multiplicities are equal for every eigenvalue.
