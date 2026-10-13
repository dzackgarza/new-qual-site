---
schema: qual/card@1
id: P-UCLAB15S-08
kind: problem
title: Density claims for determinant-one and simple-spectrum matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Prove or disprove the following claims.

1. Matrices with determinant $1$ are dense in the set of all $3\times3$ real matrices.

2. Matrices with distinct eigenvalues are dense in the set of all $3\times3$ complex matrices.

Here the distance between $A=(a_{ij})$ and $B=(b_{ij})$ is
\[
d(A,B)=\left(\sum_{1\le i,j\le3}|a_{ij}-b_{ij}|^2\right)^{1/2}.
\]
:::

::: {.solution}
<1>1. Claim 1 is false.

::: {.proof}
Consider the zero matrix
\[
0\in M_3(\mathbb R).
\]
Suppose matrices with determinant $1$ were dense.
Then there would exist a sequence
\[
A_n\to0
\]
in the stated Euclidean matrix norm with
\[
\det A_n=1
\]
for every $n$.

The determinant is a polynomial in the matrix entries, hence continuous.
Therefore
\[
\det A_n\to\det0=0.
\]
But
\[
\det A_n=1
\]
for every $n$, so the left side converges to $1$, a contradiction.
Thus the determinant-one matrices are not dense.
:::

<1>2. In fact, there is an open neighborhood of the zero matrix containing no determinant-one matrix.

::: {.proof}
By continuity of determinant at $0$, there exists $\delta>0$ such that
\[
d(A,0)<\delta
\]
implies
\[
|\det A|<\frac12.
\]
No such matrix can satisfy
\[
\det A=1.
\]
:::

<1>3. Claim 2 is true.
Let
\[
A\in M_3(\mathbb C).
\]
By Schur triangularization, there exists a unitary matrix $U$ such that
\[
U^*AU
=
T
\]
is upper triangular.

::: {.proof}
This is the complex Schur theorem.
:::

<1>4. Write
\[
T=
\begin{pmatrix}
\lambda_1&*&*\\
0&\lambda_2&*\\
0&0&\lambda_3
\end{pmatrix}.
\]
For every $\varepsilon>0$, choose pairwise distinct complex numbers
\[
\mu_1,\mu_2,\mu_3
\]
such that
\[
|\mu_i-\lambda_i|<\varepsilon.
\]

::: {.proof}
Each open disk centered at $\lambda_i$ with radius $\varepsilon$ contains infinitely many complex numbers.
Choose $\mu_1$, then choose $\mu_2$ different from $\mu_1$, then choose $\mu_3$ different from both preceding choices.
:::

<1>5. Let $T_\varepsilon$ be obtained from $T$ by replacing the diagonal entries $\lambda_i$ by $\mu_i$ and leaving the off-diagonal entries unchanged.
Then
\[
T_\varepsilon
\]
has three distinct eigenvalues and is therefore diagonalizable.

::: {.proof}
An upper-triangular matrix has eigenvalues equal to its diagonal entries.
Thus the eigenvalues of $T_\varepsilon$ are
\[
\mu_1,\mu_2,\mu_3,
\]
which are pairwise distinct by construction.
Eigenvectors for distinct eigenvalues are linearly independent.
Hence a $3\times3$ matrix with three distinct eigenvalues is diagonalizable.
:::

<1>6. Define
\[
A_\varepsilon
=
UT_\varepsilon U^*.
\]
Then $A_\varepsilon$ is diagonalizable and
\[
A_\varepsilon\to A
\]
as $\varepsilon\to0$.

::: {.proof}
Similarity preserves diagonalizability, so $A_\varepsilon$ is diagonalizable by step <1>5.

Also,
\[
A_\varepsilon-A
=
U(T_\varepsilon-T)U^*.
\]
The difference
\[
T_\varepsilon-T
\]
is diagonal with entries
\[
\mu_i-\lambda_i,
\]
all of which tend to zero.
Thus
\[
T_\varepsilon\to T.
\]
Multiplication by the fixed matrices $U$ and $U^*$ is continuous, hence
\[
A_\varepsilon\to A.
\]
:::

<1>7. Therefore matrices with distinct eigenvalues are dense in
\[
\boxed{M_3(\mathbb C)}.
\]

::: {.proof}
The matrix $A$ was arbitrary, and step <1>6 constructs matrices with distinct eigenvalues arbitrarily close to it.
:::

<1>8. Hence the answers are:
\[
\boxed{\text{Claim 1 is false; Claim 2 is true}.}
\]

::: {.proof}
Claim 1 is disproved in steps <1>1--<1>2, and Claim 2 is proved in steps <1>3--<1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 gives the complete disposition of both claims.
:::
:::
