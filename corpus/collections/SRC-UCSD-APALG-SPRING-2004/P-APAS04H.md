---
schema: qual/card@1
id: P-APAS04H
kind: problem
title: Character of the action on $k$-subsets; Frobenius image of $\chi^{(2,4)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Permutations
relations: []
review: draft
---

::: problem
If $S=\{1\le i_1<i_2<\cdots<i_k\le n\}$ is a subset of $\{1,2,\ldots,n\}$ and $\sigma=(\sigma_1,\sigma_2,\ldots,\sigma_n)$ is a permutation, let $\sigma(S)$ denote the subset $\sigma(S)=\{\sigma_{i_1},\ldots,\sigma_{i_k}\}$.
In this manner we can define an action of $S_n$ on the $k$-subsets of $\{1,2,\ldots,n\}$ and induce a representation $A^{(k,n)}$ such that if $S_1,\ldots,S_{\binom{n}{k}}$ is a list of the $k$-element subsets of $\{1,\ldots,n\}$, then
\begin{align}
\sigma\langle S_1,\ldots,S_{\binom{n}{k}}\rangle
&=\langle\sigma(S_1),\ldots,\sigma(S_{\binom{n}{k}})\rangle\\
&=\langle S_1,\ldots,S_{\binom{n}{k}}\rangle A^{(k,n)}(\sigma).
\end{align}
Let $\chi^{(k,n)}$ be the character of $A^{(k,n)}$.

(a) Find the Frobenius image of $\chi^{(2,4)}$.

(b) Use your result in (a) to compute the decomposition of $\chi^{(2,4)}$ into a sum of irreducible characters of $S_4$.
:::
