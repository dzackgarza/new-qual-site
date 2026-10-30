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
Let $Ax=\lambda x$ with $x\ne0$. Choose an index $i$ such that
$$
\abs{x_i}=\max_{1\le k\le n}\abs{x_k}.
$$
Then $x_i\ne0$. Looking at the $i$th coordinate of the eigenvalue equation gives
$$
\sum_{j=1}^n a_{ij}x_j=\lambda x_i,
$$
so
$$
(\lambda-a_{ii})x_i=\sum_{j\ne i}a_{ij}x_j.
$$
Therefore
$$
\abs{\lambda-a_{ii}}\,\abs{x_i}
\le
\sum_{j\ne i}\abs{a_{ij}}\,\abs{x_j}
\le
\abs{x_i}\sum_{j\ne i}\abs{a_{ij}}.
$$
Dividing by $\abs{x_i}>0$ yields
$$
\abs{\lambda-a_{ii}}\le\sum_{j\ne i}\abs{a_{ij}}.
$$
Thus $\lambda\in D_i$, and hence
$$
\boxed{\lambda\in\bigcup_{i=1}^nD_i.}
$$
:::
