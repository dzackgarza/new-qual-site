---
schema: qual/card@1
id: P-WB2SR
kind: problem
title: A basis of $V$ yields a basis of $V^{\oplus m}$
classification:
  areas:
  - algebra
  topics:
  - Bases
  - Vector Spaces
  - Direct Products
relations: []
review: draft
---

::: {.problem}
Let $V$ be an $n$-dimensional vector space with basis $\mathcal B=\{b_1,\ldots,b_n\}$. Construct a basis of $V^{\oplus m}$ and compute its dimension.
:::

::: {.solution}

No retained solution set covers this exercise: the card is an unsorted compilation problem with no book or sheet attributed in its collection, so the construction and the verification below are the card's own. Both halves of the basis condition are checked coordinatewise, which is the only point the earlier version of the card left implicit.

Throughout, $V$ is an $n$-dimensional vector space over a field with basis $\mathcal{B}=\theset{b_{1},\dots,b_{n}}$, and
$$
V^{\oplus m}\coloneqq\underbrace{V\oplus\cdots\oplus V}_{m\text{ copies}}=\theset{(v_{1},\dots,v_{m})\mid v_{i}\in V},
$$
with coordinatewise addition and scalar multiplication. For $1\leq i\leq m$ and $1\leq k\leq n$ let $e_{i,k}\in V^{\oplus m}$ be the $m$-tuple whose $i$-th entry is $b_{k}$ and whose other entries are $0$.

::: pf

::: {.pf-step #coordinates}
Each $v\in V^{\oplus m}$ has a unique expression $v=\sum_{i=1}^{m}\sum_{k=1}^{n}a_{i,k}e_{i,k}$ with the $a_{i,k}$ in the field, and its $i$-th entry is then $\sum_{k=1}^{n}a_{i,k}b_{k}$.

::: pf-proof
Write $v=(v_{1},\dots,v_{m})$. Since $\mathcal{B}$ is a basis of $V$, each $v_{i}$ has a unique expression $v_{i}=\sum_{k=1}^{n}a_{i,k}b_{k}$. An $m$-tuple is determined by its entries, and the $i$-th entry of $\sum_{i,k}a_{i,k}e_{i,k}$ is $\sum_{k}a_{i,k}b_{k}$ because $e_{i,k}$ contributes $b_{k}$ in the $i$-th slot and $0$ in the others; so $v$ equals that sum. Uniqueness follows from the uniqueness of each expansion $v_{i}=\sum_{k}a_{i,k}b_{k}$, since the $i$-th entry of the sum determines exactly the coefficients $a_{i,1},\dots,a_{i,n}$.
:::

:::

::: {.pf-step #spanning}
$\mathcal{B}^{(m)}\coloneqq\theset{e_{i,k}\mid1\leq i\leq m,\ 1\leq k\leq n}$ spans $V^{\oplus m}$.

::: pf-proof
By the first half of step [](#coordinates){.pf-ref} every $v\in V^{\oplus m}$ is a linear combination of the elements $e_{i,k}$, which is what spanning means.
:::

:::

::: {.pf-step #independent}
$\mathcal{B}^{(m)}$ is linearly independent.

::: pf-proof
Suppose $\sum_{i=1}^{m}\sum_{k=1}^{n}a_{i,k}e_{i,k}=0$ in $V^{\oplus m}$. Reading the $i$-th entry, and using the description of that entry in step [](#coordinates){.pf-ref}, gives $\sum_{k=1}^{n}a_{i,k}b_{k}=0$ in $V$ for each $i$. Since $\mathcal{B}$ is linearly independent, $a_{i,k}=0$ for all $k$, and this holds for every $i$; so all the coefficients vanish.
:::

:::

::: pf-step
Therefore $\mathcal{B}^{(m)}$ is a basis of $V^{\oplus m}$ and
$$
\boxed{\dim V^{\oplus m}=mn=m\dim V.}
$$

::: pf-proof
The set $\mathcal{B}^{(m)}$ spans by step [](#spanning){.pf-ref} and is independent by step [](#independent){.pf-ref}, hence is a basis. Its elements are indexed by the pairs $(i,k)$ with $1\leq i\leq m$, $1\leq k\leq n$, of which there are $mn$; the cardinality of a basis is the dimension, so $\dim V^{\oplus m}=mn=m\dim V$.
:::

:::

:::

:::
