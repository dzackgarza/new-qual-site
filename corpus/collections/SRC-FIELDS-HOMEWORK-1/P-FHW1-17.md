---
schema: qual/card@1
id: P-FHW1-17
kind: problem
title: Degree of a composite field
classification:
  areas: [algebra]
  topics: [Field Extensions]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $K_1,K_2$ be subfields of a field $K$. Then the composite field $K_1K_2$ of $K_1$ and $K_2$ is the smallest subfield of $K$ containing $K_1$ and $K_2$. Show that
$$
[K_1K_2:F]\leq[K_1:F][K_2:F],
$$
with equality if and only if some basis of $K_2$ over $F$ is linearly independent over $K_1$.
:::

::: remark
The sheet does not introduce $F$. The statement is meant for a common subfield $F\subseteq K_1\cap K_2$ with $[K_1:F]$ and $[K_2:F]$ finite.
:::

::: {.solution}
Let $n=[K_2:F]$ and let $b_1,\ldots,b_n$ be a basis of $K_2$ over $F$; write $K_1K_2$ for the smallest subfield of $K$ containing both $K_1$ and $K_2$.

::: pf

::: {.pf-step #span-is-composite}
$K_1K_2=\sum_{i=1}^nK_1b_i=\Bigl\{\sum_{i=1}^nc_ib_i : c_i\in K_1\Bigr\}$.

::: pf-proof
The set $R=\sum_iK_1b_i$ is a $K_1$-subspace of $K$, contains $K_1$ (take $i$ with $b_i=1\in F$) and contains each $b_i$ (take $c_i=1$ and the other coefficients $0$), hence contains $K_2$.
It is closed under multiplication, because $b_ib_j\in K_2$ and $K_2=\sum_iFb_i$, so $b_ib_j=\sum_kf_{ijk}b_k$ with $f_{ijk}\in F\subseteq K_1$, and the products $c_ic_j'f_{ijk}$ lie in $K_1$.
A nonzero element of $R$ is thus algebraic over $K_1$ in the sense of [[P-FHW1-01|the invariant-subspace criterion]], since $R$ is finite-dimensional over $K_1$ and stable under multiplication by it; the argument of [[P-FHW1-07]] then shows that its inverse lies in $R$, so $R$ is a field.
Being a field containing $K_1$ and $K_2$, it contains $K_1K_2$, while $K_1K_2$ contains $K_1$ and the $b_i$ and hence contains $R$; the two are equal.
:::

:::

::: {.pf-step #bound}
$[K_1K_2:F]\le[K_1:F][K_2:F]$.

::: pf-proof
By step [](#span-is-composite){.pf-ref} the composite is spanned over $K_1$ by the $n$ elements $b_1,\ldots,b_n$, so $[K_1K_2:K_1]\le n$.
The tower law for $F\subseteq K_1\subseteq K_1K_2$ gives $[K_1K_2:F]=[K_1K_2:K_1][K_1:F]\le n[K_1:F]=[K_1:F][K_2:F]$.
:::

:::

::: {.pf-step #equality}
$[K_1K_2:F]=[K_1:F][K_2:F]$ if and only if some basis of $K_2$ over $F$ is linearly independent over $K_1$.

::: pf-proof
If the basis $b_1,\ldots,b_n$ is linearly independent over $K_1$, then $[K_1K_2:K_1]=n$ and the tower law gives equality.
Conversely, suppose equality holds and let $b_1',\ldots,b_n'$ be any basis of $K_2$ over $F$. It spans $K_1K_2$ over $K_1$ by the argument of step [](#span-is-composite){.pf-ref}, and $[K_1K_2:K_1]=[K_2:F]=n$, so $n$ spanning elements of an $n$-dimensional space form a basis and are $K_1$-linearly independent.
:::

:::

:::

:::
