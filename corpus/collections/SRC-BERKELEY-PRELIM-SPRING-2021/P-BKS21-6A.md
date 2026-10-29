---
schema: qual/card@1
id: P-BKS21-6A
kind: problem
title: Positive off-diagonal entries and negative row sums force $\det A\ne0$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 column-elimination induction. Its preserved sign and row-sum conditions are valid. The solution below gives a shorter direct kernel argument from strict row diagonal dominance.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified that each diagonal entry is negative with magnitude strictly larger than the sum of the off-diagonal entries in its row, and that a maximal-coordinate kernel vector yields a contradiction.
---

::: {.problem}
Let $A$ be a real $n\times n$ matrix such that every off-diagonal entry is positive and the sum of the entries in each row is negative. Show that $\det A\ne0$.
:::

::: {.solution}

Write $A=(a_{ij})$.

::: pf

::: {.pf-step #s1-1}

For every row index $i$,
$$
|a_{ii}|>\sum_{j\neq i}|a_{ij}|.
$$


::: pf-proof

All off-diagonal entries are positive, so
$$
\sum_{j\neq i}a_{ij}>0.
$$
The hypothesis on the $i$-th row says
$$
a_{ii}+\sum_{j\neq i}a_{ij}<0.
$$
Hence
$$
a_{ii}<-\sum_{j\neq i}a_{ij}<0.
$$
Therefore
$$
|a_{ii}|=-a_{ii}>
\sum_{j\neq i}a_{ij}
=
\sum_{j\neq i}|a_{ij}|.
$$

:::

:::

::: {.pf-step #s1-2}

The kernel of $A$ is trivial.


::: pf-proof

Suppose, for contradiction, that $Ax=0$ for some nonzero
$$
x=(x_1,\ldots,x_n)^T.
$$
Choose $k$ such that
$$
|x_k|=\max_{1\leq j\leq n}|x_j|.
$$
Then $|x_k|>0$. The $k$-th row of $Ax=0$ gives
$$
a_{kk}x_k=-\sum_{j\neq k}a_{kj}x_j.
$$
Taking absolute values and using maximality of $|x_k|$,
$$
\begin{aligned}
|a_{kk}|\,|x_k|
&\leq
\sum_{j\neq k}|a_{kj}|\,|x_j|\\
&\leq
\left(\sum_{j\neq k}|a_{kj}|\right)|x_k|.
\end{aligned}
$$
Since $|x_k|>0$, cancellation gives
$$
|a_{kk}|
\leq
\sum_{j\neq k}|a_{kj}|,
$$
contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Consequently
$$
\boxed{\det A\neq0}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} shows that the linear map defined by the square matrix $A$ is injective. A linear endomorphism of the finite-dimensional space $\RR^n$ is injective if and only if it is invertible, and a square matrix is invertible if and only if its determinant is nonzero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
