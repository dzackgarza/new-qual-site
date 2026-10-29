---
schema: qual/card@1
id: P-UCLAB16F-03
kind: problem
title: Matrices of the form $R^T\operatorname{diag}(1,-1)R$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 3 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let

$$
B = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}.
$$

Find necessary and sufficient conditions on a $3 \times 3$ matrix $A$ with real entries so that the equation

$$
A = R^T B R
$$

admits a solution $R$ of full rank.
Here $R$ must be a $2 \times 3$ matrix with real entries.
You must prove that your conditions are necessary and sufficient.
:::

::: {.solution}

The necessary and sufficient condition is:
\[
\boxed{
A\text{ is real symmetric, has rank }2,\text{ and is indefinite.}
}
\]
Equivalently, the quadratic form defined by $A$ has inertia
\[
(1,1,1_0),
\]
namely one positive square, one negative square, and one zero square.

::: pf

::: {.pf-step #s1-1}

Suppose
\[
A=R^TBR
\]
for a real $2\times3$ matrix $R$ of rank $2$.
Then $A$ is symmetric.


::: pf-proof

Since
\[
B^T=B,
\]
one has
\[
A^T
=(R^TBR)^T
=
R^TB^TR
=
R^TBR
=A.
\]

:::

:::

::: {.pf-step #s1-2}

Under the same hypothesis,
\[
\ker A=\ker R.
\]


::: pf-proof

If
\[
Rx=0,
\]
then
\[
Ax=R^TBRx=0,
\]
so
\[
\ker R\subseteq\ker A.
\]

Conversely, suppose
\[
Ax=0.
\]
Then
\[
R^TBRx=0.
\]
Because $R$ has rank $2$, the transpose
\[
R^T:\RR^2\to\RR^3
\]
also has rank $2$ and is therefore injective.
Hence
\[
BRx=0.
\]
The matrix $B$ is invertible, so
\[
Rx=0.
\]
Thus
\[
\ker A\subseteq\ker R.
\]

:::

:::

::: {.pf-step #s1-3}

Under the same hypothesis,
\[
\operatorname{rank}A=2.
\]


::: pf-proof

Since $R$ has rank $2$ as a map
\[
\RR^3\to\RR^2,
\]
rank-nullity gives
\[
\dim\ker R=1.
\]
By step [](#s1-2){.pf-ref},
\[
\dim\ker A=1.
\]
Thus
\[
\operatorname{rank}A
=
3-1
=2.
\]

:::

:::

::: {.pf-step #s1-4}

Under the same hypothesis, the quadratic form defined by $A$ takes both positive and negative values.


::: pf-proof

Since $R$ has rank $2$, it is onto
\[
\RR^2.
\]
Choose
\[
x_+,x_-\in\RR^3
\]
such that
\[
Rx_+=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
Rx_-=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]
Then
\[
\begin{aligned}
x_+^TAx_+
&=
(Rx_+)^TB(Rx_+)\\
&=
\begin{pmatrix}
1&0
\end{pmatrix}
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\begin{pmatrix}
1\\
0
\end{pmatrix}\\
&=
1,
\end{aligned}
\]
while
\[
x_-^TAx_-=-1.
\]
Thus $A$ is indefinite.

:::

:::

::: {.pf-step #s1-5}

Hence symmetry, rank $2$, and indefiniteness are necessary.


::: pf-proof

Symmetry is step [](#s1-1){.pf-ref}, rank $2$ is step [](#s1-3){.pf-ref}, and indefiniteness is step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Conversely, suppose $A$ is real symmetric, has rank $2$, and is indefinite.
Then its eigenvalues are
\[
\lambda>0,\qquad -\mu<0,\qquad 0
\]
for some
\[
\lambda,\mu>0.
\]


::: pf-proof

By the real spectral theorem, all eigenvalues of $A$ are real and $A$ has an orthonormal eigenbasis.
Rank $2$ means exactly one eigenvalue is zero.
Indefiniteness means among the two nonzero eigenvalues, one is positive and one is negative.
Write them as
\[
\lambda
\quad\text{and}\quad
-\mu
\]
with $\lambda,\mu>0$.

:::

:::

::: {.pf-step #s1-7}

There exists an orthogonal matrix $Q$ such that
\[
A
=
Q^T
\begin{pmatrix}
\lambda&0&0\\
0&-\mu&0\\
0&0&0
\end{pmatrix}
Q.
\]


::: pf-proof

Choose an orthonormal eigenbasis of $A$, ordered so that the corresponding eigenvalues are
\[
\lambda,-\mu,0.
\]
Let $Q$ be the orthogonal change-of-basis matrix.
The spectral theorem gives the displayed diagonalization.

:::

:::

::: {.pf-step #s1-8}

Define
\[
R
=
\begin{pmatrix}
\sqrt{\lambda}&0&0\\
0&\sqrt{\mu}&0
\end{pmatrix}
Q.
\]
Then $R$ has rank $2$.


::: pf-proof

The matrix
\[
\begin{pmatrix}
\sqrt{\lambda}&0&0\\
0&\sqrt{\mu}&0
\end{pmatrix}
\]
has rank $2$ because $\lambda,\mu>0$.
Multiplication on the right by the invertible matrix $Q$ preserves rank.
Thus
\[
\operatorname{rank}R=2.
\]

:::

:::

::: {.pf-step #s1-9}

The matrix from step [](#s1-8){.pf-ref} satisfies
\[
\boxed{A=R^TBR}.
\]


::: pf-proof

Let
\[
D=
\begin{pmatrix}
\sqrt{\lambda}&0&0\\
0&\sqrt{\mu}&0
\end{pmatrix}.
\]
Then
\[
R=DQ.
\]
Hence
\[
\begin{aligned}
R^TBR
&=
Q^TD^TBDQ\\
&=
Q^T
\begin{pmatrix}
\lambda&0&0\\
0&-\mu&0\\
0&0&0
\end{pmatrix}
Q\\
&=
A
\end{aligned}
\]
by step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore the stated conditions are sufficient.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} construct a full-rank $2\times3$ matrix $R$ satisfying the required identity.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves necessity, and step [](#s1-10){.pf-ref} proves sufficiency.

:::

:::

:::
