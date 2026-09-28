---
schema: qual/card@1
id: P-BERK80S-14
kind: problem
title: Normal form for anticommuting involutions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 14 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the source convention $T^{-1}AT$ and $T^{-1}BT$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified diagonalizability of A, the eigenspace swap induced by B, and the simultaneous basis giving both required normal forms.
---

::: {.problem}
Let $A$ and $B$ be real $2\times2$ matrices such that $A^2=B^2=I$ and $AB+BA=0$.
Prove there exists a real nonsingular matrix $T$ with

$$
TAT^{-1}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad TBT^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
:::

::: {.solution}
<1>1. The matrix $A$ is diagonalizable over $\RR$, and both $1$ and $-1$ are
eigenvalues of $A$, each with a one-dimensional eigenspace.

::: {.proof}
Because $A^2=I$, the minimal polynomial of $A$ divides $(t-1)(t+1)$, which
has distinct real roots. Hence $A$ is diagonalizable over $\RR$ with
eigenvalues in $\{1,-1\}$.

If $A=I$, then
$$
AB+BA=2B=0,
$$
which is impossible because $B^2=I$ makes $B$ invertible. Similarly,
$A=-I$ would give
$$
AB+BA=-2B=0,
$$
again impossible. A diagonalizable $2\times2$ matrix with eigenvalues in
$\{1,-1\}$ that is neither $I$ nor $-I$ has both eigenvalues, each with a
one-dimensional eigenspace.
:::

<1>2. $B$ maps the $\lambda$-eigenspace of $A$ isomorphically onto the
$(-\lambda)$-eigenspace, for $\lambda\in\{1,-1\}$.

::: {.proof}
Let $v$ satisfy
$$
Av=\lambda v.
$$
From $AB=-BA$,
$$
A(Bv)=-B(Av)=-\lambda Bv.
$$
Because $B$ is invertible, $Bv\ne0$ whenever $v\ne0$, and $B$ is injective
between these one-dimensional eigenspaces.
:::

<1>3. Let $u\ne0$ satisfy $Au=u$, and let $P$ be the real matrix with
columns $u$ and $Bu$. Then $P$ is nonsingular and
$$
P^{-1}AP=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
P^{-1}BP=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

::: {.proof}
By step <1>2,
$$
A(Bu)=-Bu,
$$
so $u$ and $Bu$ are nonzero vectors in distinct eigenspaces of $A$ and
form a basis of $\RR^2$. Hence $P$ is nonsingular. In this basis,
$$
Au=u,
\qquad
A(Bu)=-Bu,
$$
which gives the matrix of $A$, and
$$
B(u)=Bu,
\qquad
B(Bu)=B^2u=u,
$$
which gives the matrix of $B$.
:::

<1>4. The real nonsingular matrix
$$
\boxed{T=P^{-1}}
$$
satisfies
$$
TAT^{-1}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
TBT^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

::: {.proof}
With $T=P^{-1}$, one has $TAT^{-1}=P^{-1}AP$ and $TBT^{-1}=P^{-1}BP$;
step <1>3 computes both.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 exhibits the required matrix $T$.
:::
:::
