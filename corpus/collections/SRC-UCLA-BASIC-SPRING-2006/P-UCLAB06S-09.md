---
schema: qual/card@1
id: P-UCLAB06S-09
kind: problem
title: Spectral theorem for real symmetric matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
Let $S$ be a real $n\times n$ symmetric matrix, i.e. ${}^tS=S$.

(A) Prove that the eigenvalues of $S$ are real.

(B) State and prove the Spectral Theorem for $S$.
:::

::: {.solution}
<1>1. Let
\[
\lambda\in\mathbb C
\]
be an eigenvalue of the real symmetric matrix $S$, with nonzero eigenvector
\[
z\in\mathbb C^n.
\]
Then
\[
\lambda\in\mathbb R.
\]

::: {.proof}
The eigenvalue equation is
\[
Sz=\lambda z.
\]
Using the standard Hermitian inner product on $\mathbb C^n$,
\[
z^*Sz
=
\lambda z^*z.
\]
Because $S$ is real symmetric,
\[
S^*=S^T=S.
\]
Hence
\[
\overline{z^*Sz}
=
z^*S^*z
=
z^*Sz,
\]
so
\[
z^*Sz
\]
is real.
Also
\[
z^*z>0.
\]
Therefore
\[
\lambda
=
\frac{z^*Sz}{z^*z}
\in
\mathbb R.
\]
:::

<1>2. Every real symmetric matrix has a nonzero real eigenvector.

::: {.proof}
The characteristic polynomial of $S$ has a complex root by the fundamental theorem of algebra.
By step <1>1, every eigenvalue is real.
Choose
\[
\lambda\in\mathbb R
\]
and a nonzero complex vector
\[
z=x+iy
\]
satisfying
\[
Sz=\lambda z.
\]
Since $S$ and $\lambda$ are real,
\[
Sx=\lambda x,
\qquad
Sy=\lambda y.
\]
At least one of $x,y$ is nonzero.
Thus there is a nonzero real eigenvector.
:::

<1>3. If
\[
Sv=\lambda v
\]
with $v\in\mathbb R^n$, then the orthogonal complement
\[
v^\perp
\]
is invariant under $S$.

::: {.proof}
Let
\[
w\in v^\perp.
\]
Then
\[
\langle Sw,v\rangle
=
\langle w,Sv\rangle
\]
because $S$ is symmetric.
Since
\[
Sv=\lambda v,
\]
one gets
\[
\langle Sw,v\rangle
=
\lambda\langle w,v\rangle
=0.
\]
Therefore
\[
Sw\in v^\perp.
\]
:::

<1>4. The restriction
\[
S|_{v^\perp}:v^\perp\to v^\perp
\]
is symmetric.

::: {.proof}
By step <1>3, the restriction is well-defined.
For
\[
w_1,w_2\in v^\perp,
\]
one has
\[
\langle Sw_1,w_2\rangle
=
\langle w_1,Sw_2\rangle
\]
because $S$ is symmetric on all of $\mathbb R^n$.
Thus the restricted operator is symmetric on the inner-product space $v^\perp$.
:::

<1>5. Spectral Theorem: every real symmetric matrix has an orthonormal basis of real eigenvectors.

::: {.proof}
Proceed by induction on
\[
n.
\]
For
\[
n=1,
\]
the statement is immediate.

Assume the result in dimension
\[
n-1
\]
and let $S$ be an $n\times n$ real symmetric matrix.
By step <1>2, choose a nonzero real eigenvector $v_1$ and normalize it so that
\[
\|v_1\|=1.
\]
Then
\[
v_1^\perp
\]
has dimension $n-1$.
By steps <1>3--<1>4, it is invariant under $S$ and the restriction of $S$ to it is symmetric.

By the induction hypothesis, there is an orthonormal basis
\[
v_2,\ldots,v_n
\]
of $v_1^\perp$ consisting of eigenvectors of the restriction, hence of $S$.
Therefore
\[
v_1,\ldots,v_n
\]
is an orthonormal basis of $\mathbb R^n$ consisting of eigenvectors of $S$.
:::

<1>6. Equivalently, there exists an orthogonal matrix $Q$ and a real diagonal matrix $D$ such that
\[
\boxed{Q^TSQ=D}.
\]

::: {.proof}
Let the columns of $Q$ be the orthonormal eigenbasis from step <1>5.
Then
\[
Q^{-1}=Q^T.
\]
If the corresponding eigenvalues are
\[
\lambda_1,\ldots,\lambda_n,
\]
the matrix of $S$ in this basis is
\[
D
=
\operatorname{diag}
(\lambda_1,\ldots,\lambda_n).
\]
Thus
\[
Q^{-1}SQ
=
Q^TSQ
=D.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves part (A).
Steps <1>2--<1>6 state and prove the spectral theorem requested in part (B).
:::
:::
