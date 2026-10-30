---
schema: qual/card@1
id: P-BKS07-9B
kind: problem
title: Cauchy--Binet formula for $\det(A^tB)$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $k$ and $n$ be integers with $n \geq k \geq 0$. Let $A$ and $B$ be $n \times k$ matrices with real coefficients.
Let $A^{t}$ be the transpose of $A$. For each size-$k$ subset $I \subseteq \{1, \ldots, n\}$, let $A_{I}$ be the $k \times k$ matrix obtained by discarding all rows of $A$ except those whose index belongs to $I$. Define $B_{I}$ similarly.
Prove that
$$
\det(A^{t} B) = \sum_{I} \det(A_{I}) \det(B_{I}),
$$
where the sum is over all size-$k$ subsets $I \subseteq \{1, \ldots, n\}$. (Suggestion: use linearity to reduce to the case where the columns of $A$ and $B$ are particularly simple.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Both sides are multilinear in the columns $a_1,\ldots,a_k$ of $A$ and $b_1,\ldots,b_k$ of $B$. So it suffices to prove the identity when $a_i=e_{\sigma(i)}$ and $b_j=e_{\tau(j)}$ for maps $\sigma,\tau\colon\{1,\ldots,k\}\to\{1,\ldots,n\}$, where $e_1,\ldots,e_n$ is the standard basis.

::: pf-proof

The $(i,j)$ entry of $A^tB$ is $a_i^tb_j$, and the determinant is linear in each row and each column, so $\det(A^tB)$ is linear in each $a_i$ and each $b_j$. The columns of $A_I$ are the columns $a_i$ with the rows outside $I$ deleted, so $\det(A_I)$ is linear in each $a_i$, and likewise for $B$. Each column is a linear combination of the $e_m$. For $k=0$, both sides equal $1$.

:::

:::

::: {.pf-step #s2}

If $\sigma$ is not injective, both sides are $0$, and likewise for $\tau$.

::: pf-proof

If $a_i=a_{i'}$ with $i\ne i'$, then $A^tB$ has two equal rows and every $A_I$ has two equal columns. The case of $\tau$ is the same, with columns of $A^tB$.

:::

:::

::: {.pf-step #s3}

If $\sigma$ and $\tau$ are injective, both sides equal $\det(A_S)\det(B_S)$ when $S=\sigma(\{1,\ldots,k\})$ equals $\tau(\{1,\ldots,k\})$, and both sides are $0$ otherwise.

::: pf-proof

For a $k$-subset $I$, the matrix $A_I$ has a zero row unless $I=S$, so $\det(A_I)=0$ for $I\ne S$. Similarly $\det(B_I)=0$ unless $I$ is the image $S'$ of $\tau$. If $S\ne S'$, every term of the sum vanishes, and $A^tB$ has a zero row: choose $i$ with $\sigma(i)\notin S'$; then $a_i^tb_j=0$ for every $j$. If $S=S'$, the only term of the sum is $\det(A_S)\det(B_S)$, and $A^tB=A_S^tB_S$ because the rows of $A$ and $B$ outside $S$ are zero.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} to [](#s3){.pf-ref} prove the identity.

:::

:::

:::
