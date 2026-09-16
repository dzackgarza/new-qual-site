---
schema: qual/card@1
id: PR-ZCKLJ
kind: proposition
title: Separable splitting fields are Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Separability
  - Splitting Fields
relations: []
review: draft
---

::: {.proposition}
Let $L/k$ be a finite field extension, with [[D-WB4M5|separable degree]] $[L:k]_s$.

(a) If $L/k$ is [[D-JGYLA|separable]], then $[L: k] = [L:k]_s$.

(b) If $L/k$ is separable and $L$ is the splitting field of a polynomial in $k[x]$, then
$$
[L:k] = \abs{\Aut_{\Fieldsover{k}}(L)},
$$
so $L/k$ is [[D-5JYEI|Galois]] with $\Gal(L/k)=\Aut_{\Fieldsover{k}}(L)$.
:::

::: {.proof}
(b) Fix an algebraic closure $\bar k$ containing $L$.
Since $L/k$ is a finite splitting field, it is [[D-LZTAK|normal]] ([[PR-TZN4M]]), so every $k$-embedding $L\to\bar k$ has image $L$ ([[PR-OZYUC]]) and is a $k$-automorphism of $L$.
Hence $[L:k]_s=\abs{\Aut_{\Fieldsover{k}}(L)}$, and (a) gives $[L:k]=\abs{\Aut_{\Fieldsover{k}}(L)}$.
:::
