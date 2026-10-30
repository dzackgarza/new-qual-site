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
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (b) of the UCSD Spring 2022 exam asks to construct a surjective S_2n-equivariant map from k[M_n] onto S^(n,n) and describe a spanning set for its kernel; no such map exists for n=1, k=C, and the intended module is not determined by the source. Part (b) now asks to prove or disprove that such a map exists for every n and k.
---

::: {.problem}
Let $M_n$ be the set of perfect matchings of $\{1, 2, \ldots, 2n\}$, i.e., a decomposition of this set into disjoint $2$-element subsets.
The permutation action of $S_{2n}$ induces an action on $M_n$.
Let $k$ be a field.

(a) Describe a subgroup $H$ of $S_{2n}$ so that the permutation representation $k[M_n]$ is isomorphic to the induced representation of the trivial representation of $H$ to $S_{2n}$.

(b) Prove or disprove: for every $n \geq 1$ and every field $k$ there is a surjective $S_{2n}$-equivariant map $\phi$ from $k[M_n]$ onto the Specht module $S^{(n,n)}$.

[Note: This is very closely related to a homework problem. Do not use the result of that problem unless you are planning to reprove it.]

:::

::: {.solution}
Write
$$
m_0=\bigl\{\{1,2\},\{3,4\},\ldots,\{2n-1,2n\}\bigr\}
$$
for the standard matching.

::: pf

::: {.pf-step}
(a) The subgroup
$$
\boxed{H=\operatorname{Stab}_{S_{2n}}(m_0)\cong (S_2)^n\rtimes S_n=S_2\wr S_n}
$$
satisfies $k[M_n]\cong\operatorname{Ind}_H^{S_{2n}}\mathbf 1$.

::: pf-proof
A permutation fixes $m_0$ exactly when it permutes its $n$ pairs, possibly swapping the two entries inside each pair; these permutations form the wreath product $S_2\wr S_n$.
Any perfect matching is carried to $m_0$ by a permutation that sends its pairs to the pairs of $m_0$, so $S_{2n}$ acts transitively on $M_n$.
Hence
$$
S_{2n}/H\longrightarrow M_n,\qquad gH\longmapsto g m_0,
$$
is an $S_{2n}$-equivariant bijection, and the permutation module of $S_{2n}/H$ is $\operatorname{Ind}_H^{S_{2n}}\mathbf 1$.
:::

:::

::: {.pf-step}
(b) $\boxed{\text{False}}$: for $n=1$ and $k=\CC$ there is no surjective $S_2$-equivariant map $\CC[M_1]\to S^{(1,1)}$.

::: pf-proof
There is exactly one perfect matching of $\{1,2\}$, so $\CC[M_1]$ is the trivial one-dimensional representation of $S_2$.
The Specht module $S^{(1,1)}$ is the sign representation, on which the transposition acts by $-1$.
An equivariant map $\phi$ from the trivial representation satisfies $(12)\phi(v)=\phi(v)$, while $(12)$ acts by $-1$ on the target; since $2\ne0$ in $\CC$, $\phi(v)=0$.
Thus every equivariant map $\CC[M_1]\to S^{(1,1)}$ is zero, and none is surjective.
:::

:::

:::

:::
