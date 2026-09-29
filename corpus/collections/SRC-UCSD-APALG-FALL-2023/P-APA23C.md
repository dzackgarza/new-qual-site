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

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex entries, and $A^H$ denotes the Hermitian transpose of $A$.

Consider any $A \in M_{m,n}$.

(a) Define $|A|$, the modulus of $A$.
Prove that the eigenvalues of $|A|$ are the singular values of $A$.

(b) Prove that if $m = n$, then $|A|$ and $|A^H|$ are similar.
:::

::: {.solution}

**Part (a).**

::: pf

::: {.pf-step #modulus-definition}
$|A| = (A^H A)^{1/2}$, the unique positive semidefinite square root of $A^H A$.

::: pf-proof
definition of the modulus of $A$.
:::

:::

::: {.pf-step #singular-values-definition}
The singular values of $A$ are the nonnegative square roots of the eigenvalues of $A^H A$.

::: pf-proof
definition of singular values.
:::

:::

::: {.pf-step #eigenvalues-of-ahasqrt}
The eigenvalues of $|A| = (A^H A)^{1/2}$ are the square roots of the eigenvalues of $A^H A$.

::: pf-proof
if $A^H A$ has eigenvalues $\lambda_i \ge 0$ (it is positive semidefinite), then $(A^H A)^{1/2}$ has eigenvalues $\sqrt{\lambda_i}$.
:::

:::

::: {.pf-step #eigenvalues-of-modulus-are-singular-values}
Hence the eigenvalues of $|A|$ are exactly the singular values of $A$.

::: pf-proof
Steps [](#singular-values-definition){.pf-ref} and [](#eigenvalues-of-ahasqrt){.pf-ref}.
:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #ahsa-aah-same-nonzero-eigenvalues}
$A^H A$ and $A A^H$ have the same nonzero eigenvalues, with the same multiplicities.

::: pf-proof
for $\lambda \neq 0$, $A^H A v = \lambda v$ implies $A A^H (Av) = \lambda (Av)$ with $Av \neq 0$, giving an injection between the nonzero eigenspaces; the argument is symmetric.
:::

:::

::: {.pf-step #ahsa-aah-same-full-spectrum-when-square}
When $m = n$, $A^H A$ and $A A^H$ are both $n \times n$, so they have the same full multiset of eigenvalues (including $0$).

::: pf-proof
Step [](#ahsa-aah-same-nonzero-eigenvalues){.pf-ref} plus the fact that both have $n$ eigenvalues counted with multiplicity, and the zero eigenvalue has the same multiplicity in both (equal to $n$ minus the number of nonzero eigenvalues).
:::

:::

::: {.pf-step #modulus-formulas-for-a-and-ah}
$|A| = (A^H A)^{1/2}$ and $|A^H| = (A A^H)^{1/2}$.

::: pf-proof
definition, since $(A^H)^H A^H = A A^H$.
:::

:::

::: {.pf-step #modulus-and-adjoint-modulus-same-eigenvalues}
$|A|$ and $|A^H|$ are both positive semidefinite Hermitian matrices with the same eigenvalues.

::: pf-proof
Steps [](#ahsa-aah-same-full-spectrum-when-square){.pf-ref} and [](#modulus-formulas-for-a-and-ah){.pf-ref}.
:::

:::

::: {.pf-step #modulus-and-adjoint-modulus-similar}
Hence $|A|$ and $|A^H|$ are unitarily similar (in particular, similar).

::: pf-proof
two Hermitian matrices are unitarily similar iff they have the same eigenvalues (both are unitarily diagonalizable with the same diagonal).
:::

:::

::: pf-qed
Step [](#eigenvalues-of-modulus-are-singular-values){.pf-ref} (part (a)) and step [](#modulus-and-adjoint-modulus-similar){.pf-ref} (part (b)).
:::

:::

:::
