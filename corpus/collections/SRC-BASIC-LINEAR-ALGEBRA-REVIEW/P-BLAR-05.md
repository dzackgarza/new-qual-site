---
schema: qual/card@1
id: P-BLAR-05
kind: problem
title: Decide which sets are vector spaces and find bases
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 5 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Decide which of the following sets are vector spaces. It is valid to show a set is a subspace, but you must indicate which vector space it is a subset of. If the set is a vector space, find a basis for it.

(a) The set of $3 \times 3$ diagonal matrices.

(b) The set of vectors of the form $[a, b, 0]$

(c) The set of vectors of the form $[a, 6]$

(d) The set of $3 \times 3$ symmetric matrices.
:::

::: {.solution}
Take all vectors and matrix entries over $\RR$. Let $E_{ij}$ denote the $3\times3$ matrix with a $1$ in position $(i,j)$ and zeros elsewhere.

::: pf

::: pf-step
The $3\times3$ diagonal matrices form a vector subspace of $M_3(\RR)$, with basis
$$
\boxed{\{E_{11},E_{22},E_{33}\}}.
$$

::: pf-proof
The zero matrix is diagonal, and sums and scalar multiples of diagonal matrices are diagonal, so the set is a subspace of $M_3(\RR)$. Every diagonal matrix has the unique form
$$
\operatorname{diag}(a,b,c)=aE_{11}+bE_{22}+cE_{33},
$$
so the displayed matrices span the subspace and are linearly independent.
:::

:::

::: pf-step
The vectors of the form $(a,b,0)$ form a vector subspace of $\RR^3$, with basis
$$
\boxed{\{(1,0,0),(0,1,0)\}}.
$$

::: pf-proof
The set contains the zero vector and is closed under vector addition and scalar multiplication. Moreover,
$$
(a,b,0)=a(1,0,0)+b(0,1,0)
$$
uniquely, proving both spanning and linear independence of the displayed pair.
:::

:::

::: pf-step
The vectors of the form $(a,6)$ are $\boxed{\text{not a vector space}}$ under the usual operations inherited from $\RR^2$.

::: pf-proof
The zero vector $(0,0)$ is not of the form $(a,6)$. Hence this subset of $\RR^2$ fails a necessary vector-space axiom.
:::

:::

::: pf-step
The $3\times3$ symmetric matrices form a vector subspace of $M_3(\RR)$, with basis
$$
\boxed{\{E_{11},E_{22},E_{33},E_{12}+E_{21},E_{13}+E_{31},E_{23}+E_{32}\}}.
$$

::: pf-proof
The zero matrix is symmetric, and if $A^T=A$ and $B^T=B$, then
$$
(A+B)^T=A+B,\qquad (\lambda A)^T=\lambda A,
$$
so the symmetric matrices form a subspace. Every symmetric matrix is uniquely expressible as
$$
aE_{11}+bE_{22}+cE_{33}
+d(E_{12}+E_{21})+e(E_{13}+E_{31})+f(E_{23}+E_{32}),
$$
which proves that the six displayed matrices form a basis.
:::

:::

:::

:::
