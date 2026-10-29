---
schema: qual/card@1
id: FD-T7IQV
kind: proposition
title: Solvability via composition factors
prompts:
- When is a group solvable, in terms of its composition factors?
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
relations:
- kind: uses
  target: D-DFIDP
- kind: uses
  target: D-FYX4I
review: draft
---

::: {.proposition}
A finite group $G$ is [[D-DFIDP|solvable]] if and only if it has a [[D-FYX4I|composition series]] whose composition factors are all abelian.
:::

::: {.proof}
Suppose $G = G^0 \geq G^1 \geq \cdots \geq G^n = \theset{e}$ is a composition series with every $G_i/G_{i+1}$ abelian.
Reversing the indices gives a normal series from $\theset{e}$ to $G$ with abelian successive quotients, so $G$ is solvable.

Conversely, suppose $G$ is solvable, witnessed by $\theset{e} = G_0 \normal G_1 \normal \cdots \normal G_n = G$ with abelian quotients.

1. A finite group has a composition series. By induction on $\size G$: if $G\neq\theset{e}$, choose a proper normal subgroup $N$ of maximal order; it is a maximal proper normal subgroup, and a composition series of $N$ followed by $G$ is one of $G$.
2. Subgroups of $G$ are solvable. For $H\leq G$, the series $H\cap G_i$ is normal, and $(H\cap G_i)/(H\cap G_{i-1})$ embeds in $G_i/G_{i-1}$ by the second isomorphism theorem, so it is abelian.
3. Quotients of $G$ are solvable. For $N\normal G$, the series $G_iN/N$ is normal, and $G_iN/G_{i-1}N$ is a quotient of $G_i/G_{i-1}$, so it is abelian.
4. A simple solvable group $S$ is abelian. Delete repeated terms from a solvable series of $S$; its second-to-last term is a proper normal subgroup of $S$, hence trivial, so $S$ is isomorphic to the last quotient, which is abelian.
5. Take a composition series of $G$ by step 1. Each factor $G_i/G_{i+1}$ is a quotient of the subgroup $G_i$, hence solvable by steps 2 and 3, and simple by [[D-FYX4I|definition]], hence abelian by step 4.
:::
