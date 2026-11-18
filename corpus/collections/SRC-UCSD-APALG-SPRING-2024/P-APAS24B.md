---
schema: qual/card@1
id: P-APAS24B
kind: problem
title: Gershgorin disks contain every eigenvalue
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $A=(a_{ij})\in M_n(\CC)=\CC^{n\times n}$ and define the sets
$$
D_i=\Biggl\{\beta\in\CC\ \st\ \abs{\beta-a_{ii}}\le\sum_{\substack{j=1\\ j\neq i}}^{n}\abs{a_{ij}}\Biggr\}\subseteq\CC,
$$
for $1\le i\le n$.
Given any eigenvalue $\lambda$ of $A$, prove
$$
\lambda\in\bigcup_{i=1}^{n}D_i.
$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/SP24_math_202_exam.pdf` and no solutions sheet accompanies it, so the argument below is the card's own; it is the standard proof of the first half of the Gershgorin circle theorem. The earlier version of the card left two points unstated: that the maximum modulus coordinate exists and is nonzero, and that every $\abs{x_{j}}$ is at most $\abs{x_{i}}$ — which is the inequality the estimate turns on.

Throughout, $A=(a_{ij})\in M_{n}(\CC)$, and for $1\leq i\leq n$
$$
D_{i}\coloneqq\Biggl\{\beta\in\CC\ \Big|\ \abs{\beta-a_{ii}}\leq\sum_{j\neq i}\abs{a_{ij}}\Biggr\}.
$$

::: pf

::: {.pf-step #maximal-coordinate}
Let $\lambda$ be an eigenvalue of $A$ with eigenvector $x\neq0$. There is an index $i$ with $\abs{x_{i}}=\max_{1\leq k\leq n}\abs{x_{k}}$, and for that $i$ one has $x_{i}\neq0$ and $\abs{x_{j}}\leq\abs{x_{i}}$ for every $j$.

::: pf-proof
The set $\theset{\abs{x_{1}},\dots,\abs{x_{n}}}$ is a nonempty finite set of real numbers, so it has a maximum, attained at some index $i$. Since $x\neq0$ some coordinate is nonzero, so the maximum is positive and $x_{i}\neq0$. Every $\abs{x_{j}}$ is at most the maximum by definition of maximum.
:::

:::

::: {.pf-step #row-equation}
$(\lambda-a_{ii})x_{i}=\sum_{j\neq i}a_{ij}x_{j}$.

::: pf-proof
The eigenvalue equation is $Ax=\lambda x$, whose $i$-th coordinate reads $\sum_{j=1}^{n}a_{ij}x_{j}=\lambda x_{i}$. Moving the $j=i$ term to the right, $\sum_{j\neq i}a_{ij}x_{j}=\lambda x_{i}-a_{ii}x_{i}=(\lambda-a_{ii})x_{i}$.
:::

:::

::: {.pf-step #estimate}
$\abs{\lambda-a_{ii}}\abs{x_{i}}\leq\abs{x_{i}}\sum_{j\neq i}\abs{a_{ij}}$.

::: pf-proof
Taking moduli in step [](#row-equation){.pf-ref} and applying the triangle inequality,
$$
\abs{\lambda-a_{ii}}\abs{x_{i}}=\Big|\sum_{j\neq i}a_{ij}x_{j}\Big|\leq\sum_{j\neq i}\abs{a_{ij}}\abs{x_{j}}\leq\sum_{j\neq i}\abs{a_{ij}}\abs{x_{i}}=\abs{x_{i}}\sum_{j\neq i}\abs{a_{ij}},
$$
where the middle inequality uses $\abs{x_{j}}\leq\abs{x_{i}}$ from step [](#maximal-coordinate){.pf-ref} and the fact that each $\abs{a_{ij}}$ is nonnegative.
:::

:::

::: pf-step
Therefore
$$
\boxed{\lambda\in\bigcup_{i=1}^{n}D_{i}.}
$$

::: pf-proof
Dividing the inequality of step [](#estimate){.pf-ref} by $\abs{x_{i}}>0$, which is legitimate by step [](#maximal-coordinate){.pf-ref}, gives $\abs{\lambda-a_{ii}}\leq\sum_{j\neq i}\abs{a_{ij}}$, which is exactly the defining condition for $\lambda\in D_{i}$; and $D_{i}$ is one of the sets in the union. Note that the index $i$ is chosen from the eigenvector, so it depends on $\lambda$.
:::

:::

:::

:::
