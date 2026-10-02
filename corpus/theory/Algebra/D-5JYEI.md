---
schema: qual/card@1
id: D-5JYEI
kind: definition
title: Galois extension and Galois group
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Separability
  - Splitting Fields
relations: []
review: draft
---

::: {.definition}
Let $L/k$ be a finite field extension.
$L/k$ is a \dfn{Galois extension} if it is [[D-LZTAK|normal]] and [[D-JGYLA|separable]].
In this case the \dfn{Galois group} of $L/k$ is
$$
\Gal(L/k) \coloneqq \Aut_{\Fieldsover{k}} (L).
$$
:::

::: {.proposition}
Let $L/k$ be a finite field extension, and let $[L:k]_s$ be its [[D-WB4M5|separable degree]].
The following are equivalent:

1. $L/k$ is normal and separable.

2. The [[D-5FG7E|fixed field]] of $\Aut_{\Fieldsover{k}}(L)$ is $k$.

3. $L$ is a splitting field over $k$ of a separable polynomial $p\in k[x]$.

4. $L$ is a splitting field over $k$ of an irreducible separable polynomial $p\in k[x]$.

5. $\size \Aut_{\Fieldsover{k}} (L) = [L: k]_s = [L: k]$.
:::

::: {.remark}
The separable degree counts the embeddings of $L$ into an algebraic closure that extend a fixed embedding of $k$:

![figures/2021-08-09_22-29-40.png](../../assets/figures/2021-08-09_22-29-40.png)
:::
