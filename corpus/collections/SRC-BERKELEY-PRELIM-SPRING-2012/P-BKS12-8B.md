---
schema: qual/card@1
id: P-BKS12-8B
kind: problem
title: Product of commuting diagonalizable operators is diagonalizable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 6 of the retained Spring 2012 solution PDF and independently reviewed the simultaneous-eigenbasis argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked P-invariance of the Q-eigenspaces, diagonalizability of the restrictions via squarefree minimal polynomials, and diagonalization of PQ.
---

::: {.problem}
Suppose that V is a finite-dimensional vector space over a field F , and $P , Q$ are commuting diagonalizable linear maps from V to V . Show $P Q$ is diagonalizable.
:::

::: {.solution}
Let
$$
\lambda_1,\ldots,\lambda_r
$$
be the distinct eigenvalues of $Q$, and set
$$
W_i\coloneqq\ker(Q-\lambda_iI).
$$

<1>1. One has
$$
V=W_1\oplus\cdots\oplus W_r.
$$

::: {.proof}
The operator $Q$ is diagonalizable over $F$. Therefore $V$ is the direct
sum of its eigenspaces, which are precisely the subspaces $W_i$.
:::

<1>2. Every subspace $W_i$ is invariant under $P$.

::: {.proof}
Let
$$
w\in W_i.
$$
Then
$$
Qw=\lambda_iw.
$$
Using
$$
PQ=QP,
$$
one obtains
$$
Q(Pw)
=
P(Qw)
=
P(\lambda_iw)
=
\lambda_iPw.
$$
Hence
$$
Pw\in W_i.
$$
:::

<1>3. For every $i$, the restriction
$$
P|_{W_i}:W_i\longrightarrow W_i
$$
is diagonalizable.

::: {.proof}
Since $P$ is diagonalizable, its minimal polynomial $m_P(t)$ splits over
$F$ as a product of distinct linear factors.

By step <1>2, the restriction $P|_{W_i}$ is defined. Any polynomial that
annihilates $P$ also annihilates the restriction, so the minimal
polynomial of $P|_{W_i}$ divides $m_P(t)$. It therefore also splits as a
product of distinct linear factors. Hence $P|_{W_i}$ is diagonalizable.
:::

<1>4. The space $V$ has a basis consisting of simultaneous eigenvectors
for $P$ and $Q$.

::: {.proof}
For each $i$, choose an eigenbasis of $W_i$ for the diagonalizable
restriction $P|_{W_i}$ from step <1>3. Every vector in this basis is
already a $Q$-eigenvector with eigenvalue $\lambda_i$ by the definition of
$W_i$.

By step <1>1, the union of these bases is a basis of $V$. Every vector in
that union is an eigenvector for both $P$ and $Q$.
:::

<1>5. The operator $PQ$ is diagonalizable.

::: {.proof}
Let $v$ be one of the simultaneous eigenvectors from step <1>4, with
$$
Pv=\mu v
$$
and
$$
Qv=\lambda v.
$$
Then
$$
PQv
=
P(\lambda v)
=
\lambda\mu v.
$$
Thus every vector in the basis from step <1>4 is an eigenvector of $PQ$.
Hence $PQ$ has an eigenbasis and is diagonalizable.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
