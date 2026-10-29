---
schema: qual/card@1
id: P-UCLAB16S-10
kind: problem
title: Density of matrices with distinct eigenvalues and failure for one Jordan block
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $S$ be a subset of $\operatorname{Mat}(3,\CC)$.
Call $S$ dense if every matrix in $\operatorname{Mat}(3,\CC)$ is a limit of a sequence of matrices in $S$.

1. Prove that the set of matrices with distinct eigenvalues is dense in $\operatorname{Mat}(3,\CC)$.

2. Prove that the set of matrices with one Jordan block is not dense in $\operatorname{Mat}(3,\CC)$.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
A\in\operatorname{Mat}(3,\CC).
$$
By Schur triangularization, there exists a unitary matrix $U$ such that
$$
U^*AU
=
T
$$
is upper triangular.


::: pf-proof

This is the complex Schur theorem.

:::

:::

::: {.pf-step #s1-2}

Write the diagonal entries of $T$ as
$$
\lambda_1,\lambda_2,\lambda_3.
$$
For every $\varepsilon>0$, choose pairwise distinct complex numbers
$$
\mu_1,\mu_2,\mu_3
$$
such that
$$
|\mu_i-\lambda_i|<\varepsilon.
$$


::: pf-proof

Each open disk
$$
B(\lambda_i,\varepsilon)
$$
contains infinitely many points.
Choose the $\mu_i$ successively, avoiding the finitely many previous choices.

:::

:::

::: pf-step

Let $T_\varepsilon$ be obtained from $T$ by replacing $\lambda_i$ by $\mu_i$ on the diagonal.
Then $T_\varepsilon$ has three distinct eigenvalues and is diagonalizable.


::: pf-proof

The eigenvalues of an upper-triangular matrix are its diagonal entries.
Thus
$$
\sigma(T_\varepsilon)
=
\{\mu_1,\mu_2,\mu_3\}.
$$
They are pairwise distinct by step [](#s1-2){.pf-ref}.
A $3\times3$ matrix with three distinct eigenvalues has three linearly independent eigenvectors and is therefore diagonalizable.

:::

:::

::: {.pf-step #s1-4}

Define
$$
A_\varepsilon
=
UT_\varepsilon U^*.
$$
Then
$$
A_\varepsilon\to A
$$
and each $A_\varepsilon$ has distinct eigenvalues.


::: pf-proof

Similarity preserves eigenvalues, so $A_\varepsilon$ has the same three distinct eigenvalues as $T_\varepsilon$.
Also,
$$
A_\varepsilon-A
=
U(T_\varepsilon-T)U^*,
$$
and
$$
T_\varepsilon-T\to0.
$$
Hence
$$
A_\varepsilon\to A.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore matrices with distinct eigenvalues are dense in
$$
\boxed{\operatorname{Mat}(3,\CC)}.
$$


::: pf-proof

The matrix $A$ was arbitrary, and step [](#s1-4){.pf-ref} constructs matrices with distinct eigenvalues arbitrarily close to it.
This proves part 1.

:::

:::

::: {.pf-step #s1-6}

Let
$$
D
=
\operatorname{diag}(0,1,2).
$$
Then there exists an open neighborhood of $D$ in which every matrix has three distinct eigenvalues.


::: pf-proof

The discriminant of the characteristic polynomial is a polynomial in its coefficients, and those coefficients are polynomial functions of the matrix entries.
Thus the discriminant
$$
\Delta(A)
$$
is a continuous polynomial function on
$$
\operatorname{Mat}(3,\CC).
$$

For
$$
D=\operatorname{diag}(0,1,2),
$$
the characteristic polynomial is
$$
t(t-1)(t-2),
$$
which has three distinct roots.
Hence
$$
\Delta(D)\ne0.
$$
By continuity, $\Delta(A)$ remains nonzero for all matrices $A$ in some open neighborhood of $D$.
Nonzero discriminant means the characteristic polynomial has no repeated root, so every matrix in that neighborhood has three distinct eigenvalues.

:::

:::

::: {.pf-step #s1-7}

Any $3\times3$ matrix with one Jordan block has only one eigenvalue.


::: pf-proof

A single $3\times3$ Jordan block has the form
$$
J_3(\lambda)
=
\begin{pmatrix}
\lambda&1&0\\
0&\lambda&1\\
0&0&\lambda
\end{pmatrix}.
$$
Its characteristic polynomial is
$$
(t-\lambda)^3.
$$
Thus any matrix similar to a single Jordan block has exactly one eigenvalue, of algebraic multiplicity $3$.

:::

:::

::: {.pf-step #s1-8}

Hence the open neighborhood from step [](#s1-6){.pf-ref} contains no matrix with one Jordan block.


::: pf-proof

Every matrix in that neighborhood has three distinct eigenvalues by step [](#s1-6){.pf-ref}.
Every matrix with one Jordan block has only one eigenvalue by step [](#s1-7){.pf-ref}.
Thus the two sets are disjoint.

:::

:::

::: {.pf-step #s1-9}

Therefore the set of matrices with one Jordan block is not dense in
$$
\boxed{\operatorname{Mat}(3,\CC)}.
$$


::: pf-proof

A dense subset must meet every nonempty open set.
Step [](#s1-8){.pf-ref} exhibits a nonempty open neighborhood that contains no matrix with one Jordan block.
This proves part 2.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part 1, and step [](#s1-9){.pf-ref} proves part 2.

:::

:::

:::
