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

::: pf

::: {.pf-step #s1}

One has
$$
V=W_1\oplus\cdots\oplus W_r.
$$

::: pf-proof

The operator $Q$ is diagonalizable over $F$. Therefore $V$ is the direct
sum of its eigenspaces, which are precisely the subspaces $W_i$.

:::

:::

::: {.pf-step #s2}

Every subspace $W_i$ is invariant under $P$.

::: pf-proof

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

:::

::: {.pf-step #s3}

For every $i$, the restriction
$$
P|_{W_i}:W_i\longrightarrow W_i
$$
is diagonalizable.

::: pf-proof

Since $P$ is diagonalizable, its minimal polynomial $m_P(t)$ splits over
$F$ as a product of distinct linear factors.

By step [](#s2){.pf-ref}, the restriction $P|_{W_i}$ is defined. Any polynomial that
annihilates $P$ also annihilates the restriction, so the minimal
polynomial of $P|_{W_i}$ divides $m_P(t)$. It therefore also splits as a
product of distinct linear factors. Hence $P|_{W_i}$ is diagonalizable.

:::

:::

::: {.pf-step #s4}

The space $V$ has a basis consisting of simultaneous eigenvectors
for $P$ and $Q$.

::: pf-proof

For each $i$, choose an eigenbasis of $W_i$ for the diagonalizable
restriction $P|_{W_i}$ from step [](#s3){.pf-ref}. Every vector in this basis is
already a $Q$-eigenvector with eigenvalue $\lambda_i$ by the definition of
$W_i$.

By step [](#s1){.pf-ref}, the union of these bases is a basis of $V$. Every vector in
that union is an eigenvector for both $P$ and $Q$.

:::

:::

::: {.pf-step #s5}

The operator $PQ$ is diagonalizable.

::: pf-proof

Let $v$ be one of the simultaneous eigenvectors from step [](#s4){.pf-ref}, with
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
Thus every vector in the basis from step [](#s4){.pf-ref} is an eigenvector of $PQ$.
Hence $PQ$ has an eigenbasis and is diagonalizable.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
