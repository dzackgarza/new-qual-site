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
$$
Tv_i=\lambda_i v_i
$$
for $i=1,\ldots,r$.

::: pf

::: {.pf-step #s1-1}

Suppose
$$
\sum_{i=1}^r c_iv_i=0.
$$


::: pf-proof

To prove linear independence, it suffices to show that every such relation has all coefficients equal to zero.

:::

:::

::: {.pf-step #s1-2}

Fix $j\in\{1,\ldots,r\}$ and define
$$
p_j(X)
=
\prod_{\substack{1\le i\le r\\i\ne j}}
(X-\lambda_i).
$$
Then
$$
p_j(T)v_i=0
$$
for every $i\ne j$.


::: pf-proof

For $i\ne j$, the product defining $p_j(T)$ contains the factor
$$
T-\lambda_iI,
$$
which annihilates $v_i$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
p_j(T)v_j
=
\left(
\prod_{i\ne j}(\lambda_j-\lambda_i)
\right)v_j.
$$


::: pf-proof

Because $v_j$ is an eigenvector with eigenvalue $\lambda_j$,
$$
p_j(T)v_j=p_j(\lambda_j)v_j.
$$
Expanding $p_j(\lambda_j)$ gives the displayed scalar.

:::

:::

::: {.pf-step #s1-4}

The coefficient $c_j$ in step [](#s1-1){.pf-ref} is zero.


::: pf-proof

Apply $p_j(T)$ to the relation from step [](#s1-1){.pf-ref}. By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
0
=
c_j
\left(
\prod_{i\ne j}(\lambda_j-\lambda_i)
\right)v_j.
$$
The eigenvalues are distinct, so the scalar product is nonzero, and $v_j\ne0$. Hence
$$
c_j=0.
$$

:::

:::

::: {.pf-step #s1-5}

The vectors $v_1,\ldots,v_r$ are linearly independent.


::: pf-proof

The index $j$ in step [](#s1-4){.pf-ref} was arbitrary, so every coefficient in the relation of step [](#s1-1){.pf-ref} is zero.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
