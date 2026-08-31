---
schema: qual/card@1
id: P-APA23C
kind: problem
title: 'Modulus of a matrix: singular values and similarity of $|A|$ and $|A^H|$'
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex entries, and $A^H$ denotes the Hermitian transpose of $A$.

Consider any $A \in M_{m,n}$.

(a) Define $|A|$, the modulus of $A$.
Prove that the eigenvalues of $|A|$ are the singular values of $A$.

(b) Prove that if $m = n$, then $|A|$ and $|A^H|$ are similar.
:::

::: {.solution}
**Part (a).**

<1>1. $|A| = (A^H A)^{1/2}$, the unique positive semidefinite square root of $A^H A$.
::: {.proof}
definition of the modulus of $A$.
:::

<1>2. The singular values of $A$ are the nonnegative square roots of the eigenvalues of $A^H A$.
::: {.proof}
definition of singular values.
:::

<1>3. The eigenvalues of $|A| = (A^H A)^{1/2}$ are the square roots of the eigenvalues of $A^H A$.
::: {.proof}
if $A^H A$ has eigenvalues $\lambda_i \ge 0$ (it is positive semidefinite), then $(A^H A)^{1/2}$ has eigenvalues $\sqrt{\lambda_i}$.
:::

<1>4. Hence the eigenvalues of $|A|$ are exactly the singular values of $A$.
::: {.proof}
<1>2 and <1>3.
:::

**Part (b).**

<1>1. $A^H A$ and $A A^H$ have the same nonzero eigenvalues, with the same multiplicities.
::: {.proof}
for $\lambda \neq 0$, $A^H A v = \lambda v$ implies $A A^H (Av) = \lambda (Av)$ with $Av \neq 0$, giving an injection between the nonzero eigenspaces; the argument is symmetric.
:::

<1>2. When $m = n$, $A^H A$ and $A A^H$ are both $n \times n$, so they have the same full multiset of eigenvalues (including $0$).
::: {.proof}
<1>1 plus the fact that both have $n$ eigenvalues counted with multiplicity, and the zero eigenvalue has the same multiplicity in both (equal to $n$ minus the number of nonzero eigenvalues).
:::

<1>3. $|A| = (A^H A)^{1/2}$ and $|A^H| = (A A^H)^{1/2}$.
::: {.proof}
definition, since $(A^H)^H A^H = A A^H$.
:::

<1>4. $|A|$ and $|A^H|$ are both positive semidefinite Hermitian matrices with the same eigenvalues.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Hence $|A|$ and $|A^H|$ are unitarily similar (in particular, similar).
::: {.proof}
two Hermitian matrices are unitarily similar iff they have the same eigenvalues (both are unitarily diagonalizable with the same diagonal).
:::

<1>6. Q.E.D.
::: {.proof}
<1>4 (part (a)) and <1>5 (part (b)).
:::
:::
