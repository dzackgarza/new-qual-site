---
schema: qual/card@1
id: P-UCLAB11S-04
kind: problem
title: Existence and uniqueness of LU decomposition
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2011.
---
::: {.problem}
Let $A$ be an $n\times n$ real matrix.

(a) Define an $LU$ decomposition of $A$ and state a necessary and sufficient condition for such a decomposition to exist.

(b) If the diagonal entries of $L$ are normalized to be $1$, prove that the decomposition, when it exists, is unique.

(c) Find an $LU$ decomposition of
$$
\begin{pmatrix}4&3\\6&3\end{pmatrix}.
$$
:::

::: {.solution}
An $LU$ decomposition of $A$ is a factorization
$$
\boxed{A=LU}
$$
with $L$ lower triangular and $U$ upper triangular.
For the standard no-row-exchange elimination convention, normalize
$$
L_{ii}=1.
$$
Under this convention, the usual existence-and-uniqueness theorem assumes that the pivots through stage $n-1$ are nonzero, equivalently that the first $n-1$ leading principal minors are nonzero.
The literal uniqueness assertion in the source is false without such a hypothesis; this is recorded explicitly below.

::: pf

::: {.pf-step #p2-s1}

If such a normalized decomposition exists and
$$
\Delta_k
$$
denotes the determinant of the leading $k\times k$ principal submatrix of $A$, then
$$
\Delta_k
=
\prod_{i=1}^k u_{ii}.
$$

::: pf-proof

Let $A_k,L_k,U_k$ denote the leading $k\times k$ principal blocks.
Because $L$ is lower triangular and $U$ is upper triangular,
$$
A_k=L_kU_k.
$$
The matrix $L_k$ is unit lower triangular, so
$$
\det L_k=1.
$$
Therefore
$$
\Delta_k
=
\det A_k
=
\det L_k\det U_k
=
\prod_{i=1}^ku_{ii}.
$$

:::

:::

::: {.pf-step #p2-s2}

If
$$
\Delta_k\ne0
$$
for
$$
k=1,\ldots,n-1,
$$
then the first $n-1$ diagonal entries of $U$ are nonzero.

::: pf-proof

By step [](#p2-s1){.pf-ref},
$$
\Delta_k
=
u_{11}\cdots u_{kk}.
$$
If this product is nonzero for every $k<n$, then each factor
$$
u_{kk}
$$
with $k<n$ is nonzero.

:::

:::

::: {.pf-step #p2-s3}

The condition
$$
\boxed{
\Delta_k\ne0
\quad
(k=1,\ldots,n-1)
}
$$
is sufficient for existence of a normalized $LU$ decomposition.

::: pf-proof

Proceed by Gaussian elimination without row exchanges.
At the first stage, the pivot is
$$
a_{11}=\Delta_1\ne0.
$$
Use it to eliminate all entries below it.

After eliminating the first $k-1$ columns, the next pivot $u_{kk}$ satisfies
$$
\Delta_k
=
u_{11}\cdots u_{kk}
$$
because the elimination factors accumulated so far are unit lower triangular.
Since
$$
\Delta_j\ne0
$$
for every $j\le k<n$, all previous pivots are nonzero and hence
$$
u_{kk}
=
\frac{\Delta_k}{\Delta_{k-1}}
\ne0.
$$
Thus elimination can continue through column $n-1$ without a row exchange.

The multipliers used to clear entries below each pivot form a unit lower triangular matrix $L$, and the resulting echelon matrix is upper triangular $U$.
Reversing the elimination gives
$$
A=LU.
$$
No condition on $\Delta_n=\det A$ is needed: the final diagonal entry of $U$ may be zero.

:::

:::

::: {.pf-step #p2-s4}

The condition in step [](#p2-s3){.pf-ref} is also necessary.

::: pf-proof

Suppose a normalized decomposition
$$
A=LU
$$
exists in the elimination sense, so the factorization is obtained without row exchanges and the pivots through column $n-1$ are nonzero.
Then step [](#p2-s1){.pf-ref} gives
$$
\Delta_k
=
u_{11}\cdots u_{kk}
\ne0
$$
for
$$
k=1,\ldots,n-1.
$$
Thus the leading principal minors must be nonzero.

:::

:::

::: {.pf-step #p2-s5}

Hence the necessary and sufficient condition for the normalized no-pivot $LU$ decomposition is
$$
\boxed{
\det A_k\ne0
\quad
k=1,\ldots,n-1.
}
$$

::: pf-proof

Sufficiency is step [](#p2-s3){.pf-ref} and necessity is step [](#p2-s4){.pf-ref}.
This answers part (a).

:::

:::

::: {.pf-step #p2-s6}

Without the nonzero-pivot hypothesis, normalized $LU$ decompositions need not be unique.

::: pf-proof

Take
$$
A=0\in M_2(\RR).
$$
For every real number $\ell$,
$$
L_\ell
=
\begin{pmatrix}
1&0\\
\ell&1
\end{pmatrix}
$$
is unit lower triangular, and with
$$
U=0
$$
one has
$$
A=L_\ell U.
$$
Different values of $\ell$ give different normalized decompositions.
Thus the source's part (b) cannot be true for arbitrary existing triangular factorizations.

:::

:::

::: {.pf-step #p2-s7}

Under the nonzero-leading-minor condition from step [](#p2-s5){.pf-ref}, the normalized $LU$ decomposition is unique.

::: pf-proof

Proceed by induction on $n$.
The case $n=1$ is immediate:
$$
A=[a]=[1][a].
$$

Assume uniqueness in size $n-1$ and write
$$
A=
\begin{pmatrix}
A_{n-1}&b\\
c^T&d
\end{pmatrix}.
$$
Any normalized factorization has block form
$$
L=
\begin{pmatrix}
L_0&0\\
\ell^T&1
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
U_0&u\\
0&\alpha
\end{pmatrix},
$$
so
$$
A_{n-1}=L_0U_0.
$$
The first $n-2$ leading principal minors of $A_{n-1}$ are nonzero, and
$$
\det A_{n-1}\ne0
$$
by the $k=n-1$ hypothesis.
Thus the induction hypothesis uniquely determines $L_0,U_0$, and $U_0$ is invertible.

The upper-right block equation
$$
b=L_0u
$$
then uniquely determines
$$
u=L_0^{-1}b.
$$
The lower-left block equation
$$
c^T=\ell^TU_0
$$
uniquely determines
$$
\ell^T=c^TU_0^{-1}.
$$
Finally,
$$
d=\ell^Tu+\alpha
$$
uniquely determines
$$
\alpha=d-\ell^Tu.
$$
Hence every entry of $L$ and $U$ is uniquely determined.
Therefore
$$
\boxed{L\text{ and }U\text{ are unique under the condition in step [](#p2-s5){.pf-ref}}.}
$$

:::

:::

::: pf-step

For
$$
A=
\begin{pmatrix}
4&3\\
6&3
\end{pmatrix},
$$
eliminating the entry $6$ below the pivot $4$ uses the multiplier
$$
\ell_{21}=\frac64=\frac32.
$$

::: pf-proof

Replace the second row by
$$
R_2-\frac32R_1.
$$
Then
$$
\begin{pmatrix}
4&3\\
6&3
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
4&3\\
0&-\frac32
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #p2-s9}

Therefore
$$
\boxed{
\begin{pmatrix}
4&3\\
6&3
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
\frac32&1
\end{pmatrix}
\begin{pmatrix}
4&3\\
0&-\frac32
\end{pmatrix}.
}
$$

::: pf-proof

Multiply:
$$
\begin{pmatrix}
1&0\\
\frac32&1
\end{pmatrix}
\begin{pmatrix}
4&3\\
0&-\frac32
\end{pmatrix}
=
\begin{pmatrix}
4&3\\
6&\frac92-\frac32
\end{pmatrix}
=
\begin{pmatrix}
4&3\\
6&3
\end{pmatrix}.
$$
This proves part (c).

:::

:::

::: pf-qed

Step [](#p2-s5){.pf-ref} gives the standard no-pivot existence criterion.
Step [](#p2-s6){.pf-ref} records the literal source defect in part (b), while step [](#p2-s7){.pf-ref} proves the intended uniqueness statement under the nonzero-pivot hypothesis.
Step [](#p2-s9){.pf-ref} gives the requested decomposition in part (c).

:::

:::

:::
