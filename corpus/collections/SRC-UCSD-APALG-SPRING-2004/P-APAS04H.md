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

::: {.solution}
<1>1. The permutation representation $A^{(2,4)}$ is isomorphic to
\[
\operatorname{Ind}_{S_2\times S_2}^{S_4}\mathbf 1.
\]
::: {.proof}
The group $S_4$ acts transitively on the six $2$-element subsets of $\{1,2,3,4\}$. The stabilizer of the subset $\{1,2\}$ consists of the permutations preserving $\{1,2\}$ and $\{3,4\}$ setwise, hence is the Young subgroup
\[
S_{\{1,2\}}\times S_{\{3,4\}}\cong S_2\times S_2.
\]
A transitive permutation representation on $G/H$ is the induced representation $\operatorname{Ind}_H^G\mathbf 1$, which gives the claim.
:::

<1>2. The Frobenius image of $\chi^{(2,4)}$ is
\[
\boxed{\operatorname{ch}\chi^{(2,4)}=h_2h_2=s_{(2)}s_{(2)}.}
\]
::: {.proof}
Under the Frobenius characteristic map, induction from a Young subgroup corresponds to multiplication of symmetric functions. The trivial representation of $S_2$ corresponds to
\[
s_{(2)}=h_2.
\]
Therefore
\[
\operatorname{ch}\left(\operatorname{Ind}_{S_2\times S_2}^{S_4}(\mathbf1\boxtimes\mathbf1)\right)
=s_{(2)}s_{(2)}=h_2h_2.
\]
By <1>1, this is the Frobenius image of $\chi^{(2,4)}$.
:::

<1>3. By the Pieri rule,
\[
h_2s_{(2)}=s_{(4)}+s_{(3,1)}+s_{(2,2)}.
\]
Hence
\[
\boxed{\chi^{(2,4)}=\chi^{(4)}+\chi^{(3,1)}+\chi^{(2,2)}.}
\]
::: {.proof}
Multiplication by $h_2$ adds a horizontal $2$-strip to the Young diagram $(2)$. The possible resulting partitions of $4$ are exactly
\[
(4),\qquad(3,1),\qquad(2,2),
\]
each with coefficient $1$. Applying the inverse Frobenius characteristic map yields the stated irreducible-character decomposition.
:::
:::
