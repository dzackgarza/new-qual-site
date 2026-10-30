---
schema: qual/card@1
id: P-PUS07
kind: problem
title: The ring of invariants $\CC[x_1,\ldots,x_n]^G$ of a subgroup $G\le S_n$ is a finitely generated $\CC$-algebra
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Group Actions
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $R=\CC[x_1,\ldots,x_n]$ be the polynomial ring over $\CC$ in $n$ indeterminates $x_1,\ldots,x_n$.
Let $S_n$ be the $n$-th symmetric group.
If $\sigma\in S_n$, then we can identify $\sigma$ with the automorphism of $R$ defined as follows: $\sigma(c)=c$ for all $c\in\CC$, and $\sigma(x_i)=x_{\sigma(i)}$ for all $i$, $1\leq i\leq n$.
Suppose that $G$ is any subgroup of $S_n$.
Let
$$
S=R^G=\{r\in R\mid \sigma(r)=r \text{ for all } \sigma\in G\}.
$$
Prove that $S$ is a finitely-generated $\CC$-algebra.
:::
