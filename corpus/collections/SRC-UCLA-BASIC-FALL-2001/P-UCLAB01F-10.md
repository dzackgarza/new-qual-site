---
schema: qual/card@1
id: P-UCLAB01F-10
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $V$ be a complex vector space and let $T:V\to V$ be linear.
Suppose $v_1,\ldots,v_n$ are nonzero eigenvectors of $T$, each corresponding to a different eigenvalue.
Prove that $v_1,\ldots,v_n$ are linearly independent.
:::

::: {.solution}

Let
$$
Tv_i=\lambda_i v_i,
\qquad
i=1,\ldots,n,
$$
where the scalars $\lambda_1,\ldots,\lambda_n$ are pairwise distinct.

::: pf

::: {.pf-step #s1-1}

Suppose
$$
\sum_{i=1}^n c_i v_i=0.
$$


::: pf-proof

To prove linear independence, it is enough to show that every linear relation among the $v_i$ has all coefficients equal to zero.

:::

:::

::: {.pf-step #s1-2}

Fix $j\in\{1,\ldots,n\}$ and define
$$
p_j(t)=\prod_{\substack{1\le i\le n\\ i\ne j}}(t-\lambda_i).
$$
Then
$$
p_j(T)v_i=0
$$
for every $i\ne j$.


::: pf-proof

If $i\ne j$, the product defining $p_j(T)$ contains the factor
$$
T-\lambda_i I.
$$
Since
$$
(T-\lambda_i I)v_i=0,
$$
the entire product annihilates $v_i$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
p_j(T)v_j
=
\left(\prod_{i\ne j}(\lambda_j-\lambda_i)\right)v_j.
$$


::: pf-proof

For every scalar polynomial $p$ and every eigenvector $v_j$ of $T$ with eigenvalue $\lambda_j$,
$$
p(T)v_j=p(\lambda_j)v_j.
$$
Apply this to $p_j$.

:::

:::

::: {.pf-step #s1-4}

The coefficient $c_j$ in step [](#s1-1){.pf-ref} is zero.


::: pf-proof

Apply $p_j(T)$ to the relation in step [](#s1-1){.pf-ref}. By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
0
=
p_j(T)\left(\sum_{i=1}^n c_i v_i\right)
=
c_j\left(\prod_{i\ne j}(\lambda_j-\lambda_i)\right)v_j.
$$
The eigenvalues are pairwise distinct, so
$$
\prod_{i\ne j}(\lambda_j-\lambda_i)\ne0,
$$
and $v_j\ne0$ by hypothesis. Therefore $c_j=0$.

:::

:::

::: {.pf-step #s1-5}

The vectors $v_1,\ldots,v_n$ are linearly independent.


::: pf-proof

The index $j$ in step [](#s1-4){.pf-ref} was arbitrary. Hence every coefficient in the relation from step [](#s1-1){.pf-ref} is zero, which is exactly linear independence.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
