---
schema: qual/card@1
id: P-BERK96S-05
kind: problem
title: A nonzero nilpotent $2\times2$ complex matrix has no square root
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
    Verified that any hypothetical square root would be nilpotent and hence
    square to zero by Cayley--Hamilton, contradicting the chosen nonzero
    nilpotent matrix.
---

::: {.problem}
Prove or disprove: for every $2\times2$ complex matrix $A$, there is a $2\times2$ complex matrix $B$ such that
\[
A=B^2.
\]
:::

::: {.solution}
Let
$$
N\coloneqq
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

The matrix $N$ is nonzero and satisfies
$$
N^2=0.
$$

::: pf-proof

The $(1,2)$-entry of $N$ is $1$, so $N\neq0$. Direct multiplication gives
$N^2=0$.

:::

:::

::: {.pf-step #s2}

There is no $2\times2$ complex matrix $B$ such that
$$
B^2=N.
$$

::: pf-proof

Suppose that such a matrix $B$ exists. By step [](#s1){.pf-ref},
$$
B^4=N^2=0,
$$
so $B$ is nilpotent. Hence both eigenvalues of $B$ are zero, and its
characteristic polynomial is
$$
\chi_B(t)=t^2.
$$
The Cayley--Hamilton theorem therefore gives
$$
B^2=0.
$$
But $B^2=N$ and $N\neq0$ by step [](#s1){.pf-ref}, a contradiction.

:::

:::

::: {.pf-step #s3}

The proposed statement is
$$
\boxed{\text{false}}.
$$

::: pf-proof

Step [](#s2){.pf-ref} shows that the explicit complex matrix $N$ has no square root in
$M_2(\CC)$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the required disproof.

:::

:::

:::
