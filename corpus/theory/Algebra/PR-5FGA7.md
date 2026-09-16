---
schema: qual/card@1
id: PR-5FGA7
kind: proposition
title: A simple group with a proper subgroup of index $n$ embeds in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Simple Groups
  - Permutations
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a [[D-T2NZ4|simple]] group and $H < G$ a proper subgroup of finite [[D-VJGH5|index]] $[G:H] = n$.
Then there is an injective group homomorphism $\phi\colon G \injects S_n$.
:::

::: {.proof}
The [[D-3T6O2|action]] of $G$ on the set $G/H$ of left cosets by $g \cdot xH \coloneqq gxH$ gives a homomorphism $\phi\colon G \to \operatorname{Sym}(G/H) \cong S_n$.
If $g \in \ker\phi$, then $gH = H$, so $\ker\phi \subseteq H \neq G$.
Since $\ker\phi$ is a normal subgroup of the simple group $G$ and $\ker\phi \neq G$, $\ker\phi$ is trivial.
:::
