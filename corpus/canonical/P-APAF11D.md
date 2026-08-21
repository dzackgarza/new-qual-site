---
schema: qual/card@1
id: P-APAF11D
kind: problem
title: Permutation representation from cosets; fixed-point character on $S_n$
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a subgroup of $G$ and let $G=\tau_1 H+\cdots+\tau_k H$ be its coset decomposition. Define a permutation representation $L$ of $G$ by
\begin{align}
\sigma\langle\tau_1 H,\ldots,\tau_k H\rangle
&=\langle\sigma\tau_1 H,\ldots,\sigma\tau_k H\rangle\\
&=\langle\tau_1 H,\ldots,\tau_k H\rangle L(\sigma)
\end{align}
so that $L(\sigma)_{i,j}=\chi(\tau_i H=\sigma\tau_j H)$.

(a) Prove that $L$ is a representation.

(b) Consider the special case where $G=S_n$ and $H=S_{n-1}\times S_1=\{\sigma\in S_n:\sigma(n)=n\}$.

(i) Show that the coset decomposition of $G$ relative to $H$ is given by
\[
G=H+(1,n)H+\cdots+(n-1,n)H
\]
where $(i,n)$ denotes the transposition which interchanges $i$ and $n$.

(ii) Show that $\chi^L(\sigma)=\operatorname{fix}(\sigma)$ where $\operatorname{fix}(\sigma)$ denotes the number of fixed points of $\sigma$.

(c) In the special case where $G=S_4$ and $H=S_3\times S_1$, use part (b) to decompose $L$ as a sum of irreducible representations of $S_4$.
:::
