---
schema: qual/card@1
id: T-AILFB
kind: theorem
title: Galois group of an irreducible separable polynomial as a transitive subgroup of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Classification
relations: []
review: draft
---

::: {.theorem}
Let $k$ be a field, let $f\in k[x]$ be [[D-BVMTZ|irreducible]] and [[D-ZT46D|separable]] of degree $n$, let $L$ be a splitting field of $f$ over $k$, and let $G\coloneqq\Gal(L/k)$.

(a) $L/k$ is [[D-5JYEI|Galois]], and $\abs G=[L:k]$.

(b) The action of $G$ on the $n$ roots of $f$ identifies $G$ with a [[D-7UIPO|transitive subgroup]] of $S_n$, well defined up to conjugation, and $n\divides\abs G\divides n!$.
:::

::: {.proof}
(a) $L$ is the splitting field of the separable polynomial $f$, so $L/k$ is Galois and $\abs G=[L:k]$ ([[PR-ZCKLJ]]).

(b) An element of $G$ permutes the roots $\alpha_1,\ldots,\alpha_n$ of $f$ and is determined by this permutation because $L=k(\alpha_1,\ldots,\alpha_n)$; reordering the roots conjugates the image in $S_n$.
For each $i$ there is a $k$-isomorphism $k(\alpha_1)\to k(\alpha_i)$ with $\alpha_1\mapsto\alpha_i$, since $f$ is irreducible, and it extends to an element of $G$, so the action is transitive.
Then $n=[k(\alpha_1):k]$ divides $[L:k]=\abs G$, and $\abs G$ divides $\abs{S_n}=n!$.
:::

::: {.remark}
These facts give a procedure for computing $G$.
Check that $f$ is irreducible and separable, compute $[L:k]=\abs G$, and list the transitive subgroups of $S_n$ of that order.
The remaining candidates are separated by the cycle types that occur in $G$, read off from factorizations of $f$ modulo primes when $k=\QQ$ ([[PR-XDWOP]]), or, for cubics, by the [[D-W3DSO|discriminant]] ([[PR-XPDHE]]).
:::
