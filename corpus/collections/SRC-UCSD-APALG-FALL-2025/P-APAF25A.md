---
schema: qual/card@1
id: P-APAF25A
kind: problem
title: Unitary form placing two distinct eigenvalues in a $2\times 2$ block
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Inner Product Spaces
relations: []
review: draft
---

::: problem
Given $n\geq 3$, fix $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ satisfying that there exist two eigenvalues $\alpha,\beta$ of $A$ with $\alpha\neq\beta$.
Prove there exists unitary $Q\in M_n(\mathbb{C})$ such that
\[
Q^H AQ=\begin{bmatrix}
\alpha & \delta & v^H \\
0 & \beta & 0 \\
0 & w & B
\end{bmatrix},
\]
for some $\delta\in\mathbb{C}$, $v,w\in\mathbb{C}^{n-2}$, and $B\in M_{n-2}(\mathbb{C})$.

(Notationally: for all $m,n\geq 1$, $z^H=\overline{z}^T$ for all $z\in M_{m,n}(\mathbb{C})=\mathbb{C}^{m\times n}$.)
:::

::: {.solution}
Choose a unit eigenvector \(q_1\in\mathbb C^n\) of \(A\) for \(\alpha\):
\[
Aq_1=\alpha q_1.
\]
Because \(\beta\) is an eigenvalue of \(A\), \(\overline\beta\) is an eigenvalue of \(A^H\). Choose a unit vector \(q_2\) such that
\[
A^Hq_2=\overline\beta\,q_2.
\]

<1>1. The vectors \(q_1\) and \(q_2\) are orthogonal.
::: {.proof}
We have
\[
q_2^HAq_1=\alpha q_2^Hq_1.
\]
On the other hand, from \(A^Hq_2=\overline\beta q_2\), taking Hermitian transpose gives
\[
q_2^HA=\beta q_2^H,
\]
so
\[
q_2^HAq_1=\beta q_2^Hq_1.
\]
Hence
\[
(\alpha-\beta)q_2^Hq_1=0.
\]
Since \(\alpha\ne\beta\), it follows that \(q_2^Hq_1=0\).
:::

<1>2. Extend \(q_1,q_2\) to an orthonormal basis
\[
q_1,q_2,q_3,\ldots,q_n
\]
of \(\mathbb C^n\), and let
\[
Q=[q_1\ q_2\ \cdots\ q_n].
\]
Then \(Q\) is unitary.
::: {.proof}
By <1>1, \(q_1,q_2\) are orthonormal. Every orthonormal set in a finite-dimensional inner-product space extends to an orthonormal basis. A matrix whose columns form an orthonormal basis is unitary.
:::

<1>3. The first column of \(Q^HAQ\) is
\[
(\alpha,0,\ldots,0)^T.
\]
::: {.proof}
The first column consists of the coordinates of \(Aq_1=\alpha q_1\) in the basis \(q_1,\ldots,q_n\). Hence its only nonzero entry is the first, equal to \(\alpha\).
:::

<1>4. The second row of \(Q^HAQ\) is
\[
(0,\beta,0,\ldots,0).
\]
::: {.proof}
Its \(j\)-th entry is
\[
q_2^HAq_j.
\]
Since \(q_2^HA=\beta q_2^H\), this equals
\[
\beta q_2^Hq_j.
\]
By orthonormality this is \(0\) for \(j\ne2\) and \(\beta\) for \(j=2\).
:::

<1>5. Therefore \(Q^HAQ\) has the required form
\[
Q^HAQ=
\begin{bmatrix}
\alpha&\delta&v^H\\
0&\beta&0\\
0&w&B
\end{bmatrix}
\]
for suitable \(\delta\in\mathbb C\), \(v,w\in\mathbb C^{n-2}\), and \(B\in M_{n-2}(\mathbb C)\).
::: {.proof}
The first-column restrictions are exactly <1>3 and the second-row restrictions are exactly <1>4. All remaining entries are unconstrained; denote them by \(\delta,v,w,B\) according to the indicated block decomposition.
:::
:::
