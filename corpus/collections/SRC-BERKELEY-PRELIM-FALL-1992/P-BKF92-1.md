---
schema: qual/card@1
id: P-BKF92-1
kind: problem
title: Similarity of two $3\times3$ matrices with characteristic polynomial $(x-1)^2(x-2)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Compared the similarity-invariant rank of M-I: it is 1 for A and 2 for B.
---

::: {.problem}
Are the matrices
\[
A=\begin{pmatrix}
1&0&0\\
-1&1&1\\
-1&0&2
\end{pmatrix},
\qquad
B=\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&2
\end{pmatrix}
\]
similar?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
$$
\operatorname{rank}(A-I)=1.
$$

::: pf-proof

Subtracting the identity gives
$$
A-I=
\begin{pmatrix}
0&0&0\\
-1&0&1\\
-1&0&1
\end{pmatrix}.
$$
The two nonzero rows are equal, so the row space is one-dimensional.

:::

:::

::: {.pf-step #s2}

One has
$$
\operatorname{rank}(B-I)=2.
$$

::: pf-proof

Here
$$
B-I=
\begin{pmatrix}
0&1&0\\
0&0&0\\
0&0&1
\end{pmatrix}.
$$
Its first and third rows are nonzero and linearly independent, so its rank is $2$.

:::

:::

::: {.pf-step #s3}

If two matrices $M,N$ are similar, then
$$
\operatorname{rank}(M-I)=\operatorname{rank}(N-I).
$$

::: pf-proof

If
$$
M=PNP^{-1}
$$
for some invertible matrix $P$, then
$$
M-I=P(N-I)P^{-1}.
$$
Multiplication on either side by an invertible matrix does not change rank.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{A\text{ and }B\text{ are not similar}}.
$$

::: pf-proof

If $A$ and $B$ were similar, step [](#s3){.pf-ref} would force
$$
\operatorname{rank}(A-I)=\operatorname{rank}(B-I),
$$
contradicting steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} answers the question.

:::

:::

:::
