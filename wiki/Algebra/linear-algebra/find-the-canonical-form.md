---
title: Find the canonical form
order: 0
problems:
  topics:
  - Linear Algebra
  - Matrices
---

# Find the canonical form

You are handed a matrix, or a characteristic polynomial, or a list of constraints, and asked for a normal form.
Which form, and how much work it takes, is decided by what you were given and by the field you are over.

## Which form is being asked for

| You are over | You want to classify | Use |
| --- | --- | --- |
| a field with all eigenvalues present | similarity | [[Algebra/linear-algebra/jordan-canonical-form\|Jordan]] |
| a field where $\chi_A$ does not split | similarity | [[Algebra/linear-algebra/rational-canonical-form\|rational]] |
| a PID, or a f.g. module | isomorphism | [[Algebra/linear-algebra/smith-normal-form\|Smith]] |
| $\RR$ or $\CC$ with an inner product | orthogonal similarity | [[Algebra/linear-algebra/the-spectral-theorem\|spectral]] |

Jordan form exists exactly when $\chi_A$ splits.
Rational form always exists, over any field, and is the one to reach for when the problem says "over $\QQ$" and the polynomial does not factor.
The two are the same theorem -- the structure theorem for $F[t]\dash$modules -- read against two choices of decomposition.

## The recipe, given a matrix

1. **Compute $\chi_A(t) = \det(tI - A)$.**
   Its roots are the eigenvalues with algebraic multiplicities.
   Shortcuts: $\tr A = \sum\lambda_i$ and $\det A = \prod \lambda_i$, and for a triangular matrix the diagonal *is* the spectrum.

2. **Compute $\min_A(t)$.**
   It divides $\chi_A$, and has the same irreducible factors, so the only freedom is the exponents.
   Test the candidates in increasing degree: the correct one is the lowest-degree monic $p$ with $p(A) = 0$.

3. **Read off diagonalizability.**
   $A$ is diagonalizable over $F$ exactly when $\min_A$ splits into *distinct* linear factors.
   If it does, stop: the form is $\diag(\lambda_i)$ with multiplicities from $\chi_A$.

4. **If not, get the block sizes.**
   For each eigenvalue $\lambda$:
   - the exponent of $(t-\lambda)$ in $\min_A$ is the size of the *largest* Jordan block;
   - the exponent in $\chi_A$ is the *total* size of all blocks for $\lambda$;
   - $\dim\ker(A-\lambda I)$ is the *number* of blocks.

   Those three numbers determine the blocks outright when the multiplicity is small, which is the case on an exam.
   When they do not, compute $\dim\ker(A-\lambda I)^k$ for increasing $k$: the successive differences give the number of blocks of size at least $k$.

5. **If $\chi_A$ does not split**, do the same computation with invariant factors instead: the rational form is the companion matrices of the invariant factors, and the last invariant factor is $\min_A$.

## Given the characteristic and minimal polynomials only

This is the standard exam question, and it is a combinatorics problem rather than a computation.
List the partitions of each eigenvalue's algebraic multiplicity whose largest part matches the exponent in $\min_A$; each list is one similarity class.

For $\chi_A = (t-2)^4$ and $\min_A = (t-2)^2$: partitions of $4$ with largest part $2$, so $2+2$ and $2+1+1$, giving exactly two classes.

## Given constraints instead of a matrix

Translate each constraint into a divisibility statement about $\min_A$, since almost every hypothesis about $A$ is one:

| Hypothesis | Says about $\min_A$ |
| --- | --- |
| $A^2 = A$ | divides $t^2 - t$, so $A$ is diagonalizable with eigenvalues $0,1$ |
| $A^k = I$ | divides $t^k-1$, so $A$ is diagonalizable when $\characteristic F \nmid k$ |
| $A^n = 0$ | divides $t^n$, so $A$ is nilpotent and all eigenvalues are $0$ |
| $A$ has finite order | as for $A^k = I$ |
| $A$ is a projection | as for $A^2 = A$ |

Every one of these is settled by step 3: a squarefree minimal polynomial means diagonalizable, and that is usually the whole problem.

## Two checks that catch most errors

- $\min_A$ and $\chi_A$ have the same irreducible factors.
  If a factor appears in one and not the other, the computation is wrong.

- The number of Jordan blocks for $\lambda$ equals the *geometric* multiplicity $\dim\ker(A-\lambda I)$, and the total of their sizes equals the *algebraic* multiplicity.
  Geometric $\leq$ algebraic always, with equality for every eigenvalue exactly when $A$ is diagonalizable.
