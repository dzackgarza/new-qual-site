---
schema: qual/card@1
id: P-UCLAB08F-07
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Let $T$ be a complex $n\times n$ matrix.
Suppose $\lambda_1,\ldots,\lambda_r$ are distinct eigenvalues with corresponding nonzero eigenvectors $v_1,\ldots,v_r$.
Prove that $v_1,\ldots,v_r$ are linearly independent.
:::

::: {.solution}
Write
\[
Tv_i=\lambda_i v_i
\]
for $i=1,\ldots,r$.

<1>1. Suppose
\[
\sum_{i=1}^r c_iv_i=0.
\]

::: {.proof}
To prove linear independence, it suffices to show that every such relation has all coefficients equal to zero.
:::

<1>2. Fix $j\in\{1,\ldots,r\}$ and define
\[
p_j(X)
=
\prod_{\substack{1\le i\le r\\i\ne j}}
(X-\lambda_i).
\]
Then
\[
p_j(T)v_i=0
\]
for every $i\ne j$.

::: {.proof}
For $i\ne j$, the product defining $p_j(T)$ contains the factor
\[
T-\lambda_iI,
\]
which annihilates $v_i$.
:::

<1>3. One has
\[
p_j(T)v_j
=
\left(
\prod_{i\ne j}(\lambda_j-\lambda_i)
\right)v_j.
\]

::: {.proof}
Because $v_j$ is an eigenvector with eigenvalue $\lambda_j$,
\[
p_j(T)v_j=p_j(\lambda_j)v_j.
\]
Expanding $p_j(\lambda_j)$ gives the displayed scalar.
:::

<1>4. The coefficient $c_j$ in step <1>1 is zero.

::: {.proof}
Apply $p_j(T)$ to the relation from step <1>1. By steps <1>2--<1>3,
\[
0
=
c_j
\left(
\prod_{i\ne j}(\lambda_j-\lambda_i)
\right)v_j.
\]
The eigenvalues are distinct, so the scalar product is nonzero, and $v_j\ne0$. Hence
\[
c_j=0.
\]
:::

<1>5. The vectors $v_1,\ldots,v_r$ are linearly independent.

::: {.proof}
The index $j$ in step <1>4 was arbitrary, so every coefficient in the relation of step <1>1 is zero.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
