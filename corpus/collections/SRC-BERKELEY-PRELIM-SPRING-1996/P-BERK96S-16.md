---
schema: qual/card@1
id: P-BERK96S-16
kind: problem
title: Spectrum and determinant of the matrix with zero diagonal and ones off diagonal
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the invariant-line and zero-sum-hyperplane decomposition,
    including the n=1 case, and the determinant from the eigenvalue
    multiplicities.
---

::: {.problem}
Let $A$ be the $n\times n$ matrix with zeros on the main diagonal and ones everywhere else. Find the eigenvalues and eigenspaces of $A$, and compute $\det A$.
:::

::: {.solution}
Let
$$
\mathbf{1}\coloneqq(1,\ldots,1)^T
$$
and
$$
H\coloneqq
\left\{
x=(x_1,\ldots,x_n)^T\in\RR^n:
\sum_{i=1}^n x_i=0
\right\}.
$$

<1>1. The vector $\mathbf{1}$ is an eigenvector of $A$ with eigenvalue
$n-1$.

::: {.proof}
Every row of $A$ contains exactly $n-1$ entries equal to $1$. Hence
$$
A\mathbf{1}=(n-1)\mathbf{1}.
$$
:::

<1>2. Every vector in $H$ is an eigenvector with eigenvalue $-1$, unless it
is zero.

::: {.proof}
If $x\in H$, then for each $i$,
$$
(Ax)_i
=
\sum_{j\neq i}x_j
=
\sum_{j=1}^n x_j-x_i
=
-x_i.
$$
Thus
$$
Ax=-x.
$$
:::

<1>3. For $n\geq2$, the complete eigenspace decomposition is
$$
\boxed{
E_{n-1}
=
\{c\mathbf{1}:c\in\RR\},
\qquad
E_{-1}
=
H
}.
$$

::: {.proof}
The subspace $H$ has dimension $n-1$, while
$$
\{c\mathbf{1}:c\in\RR\}
$$
has dimension $1$. Their intersection is zero because a scalar multiple of
$\mathbf{1}$ lies in $H$ only when
$$
nc=0,
$$
hence $c=0$. Therefore
$$
\RR^n
=
\{c\mathbf{1}:c\in\RR\}
\oplus H.
$$
Steps <1>1 and <1>2 show that $A$ acts on these summands by $n-1$ and $-1$,
respectively, so there are no other eigenvalues or eigenspaces.

If $n=1$, then $A=(0)$, so the only eigenvalue is $0$ and its eigenspace is
all of $\RR$.
:::

<1>4. The determinant is
$$
\boxed{
\det A
=
(n-1)(-1)^{n-1}
}.
$$

::: {.proof}
For $n\geq2$, step <1>3 gives the eigenvalue $n-1$ with multiplicity $1$
and the eigenvalue $-1$ with multiplicity $n-1$. Their product is the
displayed determinant. If $n=1$, then $A=(0)$ and the same formula gives
$0$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 give the requested eigenspaces, eigenvalues, and
determinant.
:::
:::
