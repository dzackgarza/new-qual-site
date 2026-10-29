---
schema: qual/card@1
id: P-UCLAB13S-06
kind: problem
title: Density of diagonalizable matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
(a) Prove that diagonalizable matrices are dense in the set of all $n\times n$ matrices with complex entries.

(b) Are diagonalizable matrices with real entries dense in the set of all $n\times n$ matrices with real entries?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
\[
A\in M_n(\CC).
\]
By the Schur triangularization theorem, there exists a unitary matrix $U$ such that
\[
\boxed{U^*AU=T}
\]
with $T$ upper triangular.


::: pf-proof

The complex Schur theorem states that every complex square matrix is unitarily similar to an upper triangular matrix.

:::

:::

::: {.pf-step #s1-2}

Write the diagonal entries of $T$ as
\[
\lambda_1,\ldots,\lambda_n.
\]
For every $\varepsilon>0$, choose complex numbers
\[
\mu_1,\ldots,\mu_n
\]
such that
\[
|\mu_j-\lambda_j|<\varepsilon
\]
for every $j$ and the $\mu_j$ are pairwise distinct.


::: pf-proof

Each open disk
\[
B(\lambda_j,\varepsilon)
\subseteq\CC
\]
contains infinitely many points.
Choose $\mu_1$ in the first disk.
After choosing
\[
\mu_1,\ldots,\mu_{j-1},
\]
choose $\mu_j$ in the $j$th disk but different from the finitely many previously chosen values.
This produces pairwise distinct choices.

:::

:::

::: pf-step

Let $T_\varepsilon$ be obtained from $T$ by replacing its diagonal entry $\lambda_j$ by $\mu_j$ and leaving every off-diagonal entry unchanged.
Then
\[
T_\varepsilon\to T
\]
as $\varepsilon\to0$.


::: pf-proof

The difference
\[
T_\varepsilon-T
\]
is diagonal with entries
\[
\mu_j-\lambda_j.
\]
Thus in any matrix norm,
\[
\|T_\varepsilon-T\|
\to0
\]
as the diagonal perturbations tend to zero.

:::

:::

::: pf-step

The matrix $T_\varepsilon$ has $n$ distinct eigenvalues
\[
\mu_1,\ldots,\mu_n.
\]


::: pf-proof

An upper triangular matrix has characteristic polynomial
\[
\prod_{j=1}^n(t-\mu_j),
\]
so its eigenvalues are precisely its diagonal entries.
By construction in step [](#s1-2){.pf-ref}, these are pairwise distinct.

:::

:::

::: {.pf-step #s1-5}

Hence $T_\varepsilon$ is diagonalizable over $\CC$.


::: pf-proof

Eigenvectors belonging to distinct eigenvalues are linearly independent.
Since $T_\varepsilon$ has $n$ distinct eigenvalues in an $n$-dimensional space, it has $n$ linearly independent eigenvectors.
Therefore it is diagonalizable.

:::

:::

::: {.pf-step #s1-6}

Define
\[
A_\varepsilon
=
UT_\varepsilon U^*.
\]
Then $A_\varepsilon$ is diagonalizable and
\[
A_\varepsilon\to A.
\]


::: pf-proof

Similarity preserves diagonalizability, so $A_\varepsilon$ is diagonalizable by step [](#s1-5){.pf-ref}.

Also,
\[
\begin{aligned}
\|A_\varepsilon-A\|
&=
\|U(T_\varepsilon-T)U^*\|.
\end{aligned}
\]
For a unitarily invariant norm this equals
\[
\|T_\varepsilon-T\|,
\]
and in any norm it still tends to zero because left and right multiplication by the fixed matrices $U,U^*$ are continuous.
Thus
\[
A_\varepsilon\to A.
\]

:::

:::

::: {.pf-step #s1-7}

Therefore the diagonalizable complex matrices are dense in
\[
\boxed{M_n(\CC)}.
\]


::: pf-proof

The matrix $A$ in step [](#s1-1){.pf-ref} was arbitrary, and step [](#s1-6){.pf-ref} constructs diagonalizable matrices arbitrarily close to it.
This proves part (a).

:::

:::

::: {.pf-step #s1-8}

For real matrices, the answer is yes when
\[
n=1
\]
and no when
\[
n\ge2.
\]


::: pf-proof

When
\[
n=1,
\]
every real matrix is already diagonal.
Thus density is trivial.

It remains to prove failure of density for
\[
n\ge2,
\]
which is done in the following steps.

:::

:::

::: {.pf-step #s1-9}

For
\[
n=2,
\]
consider
\[
R=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
Then there is an open neighborhood of $R$ containing no real-diagonalizable matrix.


::: pf-proof

For a real $2\times2$ matrix $B$, the characteristic polynomial is
\[
t^2-(\operatorname{tr}B)t+\det B.
\]
Its discriminant is
\[
\Delta(B)
=(\operatorname{tr}B)^2-4\det B.
\]
For $R$,
\[
\operatorname{tr}R=0,
\qquad
\det R=1,
\]
so
\[
\Delta(R)=-4<0.
\]
The discriminant is a continuous polynomial function of the matrix entries.
Therefore
\[
\Delta(B)<0
\]
for all $B$ in some open neighborhood of $R$.
Such a matrix has no real eigenvalues and hence cannot be diagonalizable over $\RR$.

:::

:::

::: {.pf-step #s1-10}

For
\[
n>2,
\]
there is likewise an open set of real matrices containing no matrix diagonalizable over $\RR$.


::: pf-proof

Let
\[
A_0
=
R
\oplus
\operatorname{diag}(3,4,\ldots,n),
\]
where $R$ is the rotation matrix from step [](#s1-9){.pf-ref}.
Its eigenvalues are
\[
i,-i,3,4,\ldots,n,
\]
all distinct.

The roots of a monic polynomial depend continuously, as an unordered multiset, on its coefficients.
The coefficients of the characteristic polynomial depend continuously on the matrix entries.
Therefore, for every real matrix $B$ sufficiently close to $A_0$, two eigenvalues of $B$ remain in small disjoint neighborhoods of
\[
i
\quad\text{and}\quad
-i.
\]
These neighborhoods may be chosen disjoint from the real axis.
Hence every sufficiently small real perturbation of $A_0$ still has a nonreal conjugate pair of eigenvalues.
Such a matrix cannot be diagonalizable over $\RR$.
Thus an open neighborhood of $A_0$ contains no real-diagonalizable matrix.

:::

:::

::: {.pf-step #s1-11}

Consequently, for every
\[
n\ge2,
\]
the real matrices diagonalizable over $\RR$ are not dense in
\[
M_n(\RR).
\]


::: pf-proof

Step [](#s1-9){.pf-ref} proves the assertion for $n=2$, and step [](#s1-10){.pf-ref} proves it for all larger $n$ by exhibiting a nonempty open set disjoint from the real-diagonalizable matrices.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and steps [](#s1-8){.pf-ref} through [](#s1-11){.pf-ref} answer part (b).

:::

:::

:::
