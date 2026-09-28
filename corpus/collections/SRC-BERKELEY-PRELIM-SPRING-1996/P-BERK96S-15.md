---
schema: qual/card@1
id: P-BERK96S-15
kind: problem
title: A positive-semidefinite symmetric matrix anticommuting with another matrix has zero product
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
  note: The matrix hypotheses were checked directly on the retained PDF page.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the eigenbasis entry calculation, the two zero-product
    conclusions, and the nonzero two-dimensional example.
---

::: {.problem}
Let $A,B$ be real $n\times n$ matrices. Suppose
\[
A^T=A,
\qquad
v^TAv\ge0\quad\text{for every }v\in\mathbb R^n,
\]
and
\[
AB+BA=0.
\]
Show that
\[
AB=BA=0.
\]
Give an example in which neither $A$ nor $B$ is zero.
:::

::: {.solution}
Since $A$ is real symmetric and positive semidefinite, choose an orthonormal
basis in which
$$
A=\diag(\lambda_1,\ldots,\lambda_n),
\qquad
\lambda_i\geq0.
$$
Write $B=(b_{ij})$ in the same basis.

<1>1. If $\lambda_i>0$ or $\lambda_j>0$, then
$$
b_{ij}=0.
$$

::: {.proof}
The $(i,j)$-entry of
$$
AB+BA=0
$$
is
$$
(\lambda_i+\lambda_j)b_{ij}=0.
$$
Because all eigenvalues are nonnegative, the assumption that at least one of
$\lambda_i,\lambda_j$ is positive implies
$$
\lambda_i+\lambda_j>0.
$$
Therefore $b_{ij}=0$.
:::

<1>2. One has
$$
AB=0.
$$

::: {.proof}
The $(i,j)$-entry of $AB$ is
$$
\lambda_i b_{ij}.
$$
If $\lambda_i=0$, this entry is zero. If $\lambda_i>0$, step <1>1 gives
$b_{ij}=0$. Thus every entry of $AB$ is zero.
:::

<1>3. One has
$$
BA=0.
$$

::: {.proof}
The $(i,j)$-entry of $BA$ is
$$
b_{ij}\lambda_j.
$$
If $\lambda_j=0$, this entry is zero. If $\lambda_j>0$, step <1>1 gives
$b_{ij}=0$. Thus every entry of $BA$ is zero.
:::

<1>4. Neither matrix need be zero.

::: {.proof}
For example, in dimension $2$ take
$$
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$
Then $A$ is symmetric positive semidefinite, both $A$ and $B$ are nonzero,
and
$$
AB=BA=0.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 prove the required vanishing, and step <1>4 supplies the
requested example.
:::
:::
