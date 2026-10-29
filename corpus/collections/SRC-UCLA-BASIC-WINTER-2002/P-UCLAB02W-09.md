---
schema: qual/card@1
id: P-UCLAB02W-09
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
  note: Checked against Problem 9 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Let $V$ be a real vector space and $T:V\to V$ linear.
Let $\lambda_1,\ldots,\lambda_m$ be distinct eigenvalues of $T$, and for each $i$ let $0\ne v_i$ be an eigenvector with eigenvalue $\lambda_i$.
Show that
$$
\{v_1,\ldots,v_m\}
$$
is linearly independent.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The assertion is true when $m=1$.


::: pf-proof

The single vector $v_1$ is nonzero by hypothesis, so the set $\{v_1\}$ is linearly independent.

:::

:::

::: {.pf-step #s1-2}

Assume the assertion holds for every collection of $m-1$ eigenvectors belonging to distinct eigenvalues, and suppose
$$
a_1v_1+\cdots+a_mv_m=0.
$$
Then
$$
a_1(\lambda_1-\lambda_m)v_1
+\cdots+
+a_{m-1}(\lambda_{m-1}-\lambda_m)v_{m-1}
=0.
$$


::: pf-proof

Apply the linear map $T-\lambda_m I$ to the assumed relation. Since
$$
Tv_i=\lambda_i v_i,
$$
one has
$$
(T-\lambda_m I)v_i=(\lambda_i-\lambda_m)v_i.
$$
For $i=m$ this is zero, while for $1\le i<m$ it gives the displayed relation.

:::

:::

::: {.pf-step #s1-3}

One has
$$
a_1=\cdots=a_{m-1}=0.
$$


::: pf-proof

The eigenvalues $\lambda_1,\ldots,\lambda_{m-1}$ are distinct, so by the induction hypothesis the vectors
$$
v_1,\ldots,v_{m-1}
$$
are linearly independent. Step [](#s1-2){.pf-ref} therefore implies
$$
a_i(\lambda_i-\lambda_m)=0
$$
for every $1\le i<m$. Because the eigenvalues are pairwise distinct,
$$
\lambda_i-\lambda_m\ne0,
$$
so $a_i=0$ for every $i<m$.

:::

:::

::: {.pf-step #s1-4}

One also has $a_m=0$.


::: pf-proof

Substituting the conclusion of step [](#s1-3){.pf-ref} into the original relation gives
$$
a_mv_m=0.
$$
Since $v_m\ne0$, it follows that $a_m=0$.

:::

:::

::: {.pf-step #s1-5}

Hence $\{v_1,\ldots,v_m\}$ is linearly independent.


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show that every linear relation among $v_1,\ldots,v_m$ has all coefficients equal to zero. This is the definition of linear independence.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} supplies the base case, and steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} establish the induction step. Therefore the assertion holds for every $m\ge1$.

:::

:::

:::
