---
schema: qual/card@1
id: P-APA22E
kind: problem
title: Permutation representation on perfect matchings and a map onto $S^{(n,n)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
relations: []
review: draft
---

::: {.problem}
Let $M_n$ be the set of perfect matchings of $\{1, 2, \ldots, 2n\}$, i.e., a decomposition of this set into disjoint $2$-element subsets.
The permutation action of $S_{2n}$ induces an action on $M_n$.
Let $k$ be a field.

(a) Describe a subgroup $H$ of $S_{2n}$ so that the permutation representation $k[M_n]$ is isomorphic to the induced representation of the trivial representation of $H$ to $S_{2n}$.

(b) Construct a surjective $S_{2n}$-equivariant map $\phi$ from $k[M_n]$ onto the Specht module $S^{(n,n)}$ and describe a spanning set for the kernel of $\phi$.

[Note: This is very closely related to a homework problem. Do not use the result of that problem unless you are planning to reprove it.]
:::


::: {.solution}
Part (a) is valid, but part (b) is false as stated for general $n$ and $k$.

For (a), fix the standard matching
\[
m_0=\bigl\{\{1,2\},\{3,4\},\ldots,\{2n-1,2n\}\bigr\}.
\]
Its stabilizer consists of arbitrary swaps inside the $n$ pairs together with arbitrary permutations of the pairs. Thus
\[
H=\operatorname{Stab}_{S_{2n}}(m_0)\cong (S_2)^n\rtimes S_n=S_2\wr S_n.
\]
The action of $S_{2n}$ on $M_n$ is transitive, and the map
\[
S_{2n}/H\longrightarrow M_n,\qquad gH\longmapsto g m_0
\]
is an $S_{2n}$-equivariant bijection. Therefore the associated permutation module is
\[
\boxed{k[M_n]\cong \operatorname{Ind}_{H}^{S_{2n}}\mathbf 1.}
\]

For (b), take $n=1$ and, for example, $k=\mathbb C$. There is exactly one perfect matching of $\{1,2\}$, so
\[
\mathbb C[M_1]\cong \mathbf 1
\]
is the trivial one-dimensional representation of $S_2$. But
\[
S^{(1,1)}\cong \operatorname{sgn}
\]
is the nontrivial sign representation. Hence
\[
\operatorname{Hom}_{S_2}(\mathbb C[M_1],S^{(1,1)})=0,
\]
so there cannot be a surjective equivariant map of the requested kind. Thus the assertion in part (b), and consequently the request for a spanning set of its kernel, is not correct as written.

There is also a general characteristic-zero obstruction. The classical decomposition of the perfect-matching permutation representation is
\[
\operatorname{Ind}_{S_2\wr S_n}^{S_{2n}}\mathbf 1
\cong
\bigoplus_{\lambda\vdash n} S^{2\lambda},
\]
where $2\lambda=(2\lambda_1,2\lambda_2,\ldots)$. Hence $S^{(n,n)}$ can occur only when $n$ is even (then $(n,n)=2(n/2,n/2)$); for odd $n$ it does not occur at all. This is consistent with the explicit counterexample $n=1$ above.
:::
