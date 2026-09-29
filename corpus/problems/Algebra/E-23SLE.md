---
schema: qual/card@1
id: E-23SLE
kind: problem
title: Jordan form of $\begin{pmatrix}1&-1&0\\-1&4&-1\\-4&13&-3\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Compute $\JCF(A)$ for
\[
A \da
\mattt{1}{-1}{0}{-1}{4}{-1}{-4}{13}{-3}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $A$ is
\[
\chi_A(t)=t(t-1)^2.
\]

::: pf-proof

Direct expansion gives
\[
\det(tI-A)
=
\det\begin{pmatrix}
t-1&1&0\\
1&t-4&1\\
4&-13&t+3
\end{pmatrix}
=(t-1)(t^2-t+1)-(t-1)
=t(t-1)^2.
\]

:::

:::

::: {.pf-step #s2}

The eigenspace for the eigenvalue $0$ is one-dimensional.

::: pf-proof

The eigenvalue $0$ has algebraic multiplicity $1$ by step [](#s1){.pf-ref}, so its geometric multiplicity
is also $1$.

:::

:::

::: {.pf-step #s3}

The eigenspace for the eigenvalue $1$ is one-dimensional.

::: pf-proof

One has
\[
A-I=
\begin{pmatrix}
0&-1&0\\
-1&3&-1\\
-4&13&-4
\end{pmatrix}.
\]
The first two rows are linearly independent, while the third row equals $-13$ times the
first row plus $4$ times the second row. Hence $\operatorname{rank}(A-I)=2$, so by
rank-nullity
\[
\dim\ker(A-I)=1.
\]

:::

:::

::: {.pf-step #s4}

The Jordan blocks for the eigenvalue $1$ consist of one block of size $2$.

::: pf-proof

By step [](#s1){.pf-ref}, the eigenvalue $1$ has algebraic multiplicity $2$. By step [](#s3){.pf-ref}, its eigenspace has
dimension $1$, which equals the number of Jordan blocks for that eigenvalue. Therefore
there is exactly one such block, and its total size must be $2$.

:::

:::

::: pf-step

Therefore
\[
\JCF(A)=J_2(1)\oplus J_1(0),
\]
up to permutation of Jordan blocks; explicitly,
\[
\JCF(A)\sim
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&0
\end{pmatrix}.
\]

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
