---
schema: qual/card@1
id: D-5JYEI
kind: definition
title: Galois extension and Galois group
prompts:
- In terms of $\abs{\Aut(K/F)}$, when is a finite extension $K/F$ Galois?
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
Fix an algebraic closure $\bar{k}$ of $k$. For every finite extension $L/k$,
$$
[L:k]_s
=
\size\Hom_{k\text{-alg}}(L,\bar{k}).
$$
If $L/k$ is Galois, normality implies that every $k$-embedding $L\hookrightarrow\bar{k}$ has image $L$. Hence
$$
\Hom_{k\text{-alg}}(L,\bar{k})=\Aut_k(L)=\Gal(L/k)
$$
and $\size\Gal(L/k)=[L:k]$.
:::
