---
schema: qual/card@1
id: D-SCHDIM
kind: definition
title: Dimension and codimension of a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Krull Dimension
  - Schemes
relations:
- kind: uses
  target: D-SCHPTS
review: draft
prompts:
- What is the dimension of a scheme?
- How does it relate to the Krull dimension of a ring?
- What is the codimension of a closed subset?
---

::: {.definition}
The \dfn{dimension} of $X$ is the supremum of $n$ over chains
$$
Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n
$$
of irreducible closed subsets of $X$; the length counts links, not sets.
The \dfn{codimension} of an irreducible closed $Z \subseteq X$ is the supremum of lengths of such chains starting at $Z_0 = Z$; for arbitrary closed $Y$ take the infimum over irreducible $Z \subseteq Y$.
:::

::: {.proposition}
$\dim \Spec A = \krulldim A$, since irreducible closed subsets of $\Spec A$ correspond to primes, order-reversingly.
The codimension of $V(\mfp)$ is the height of $\mfp$.
More generally, if $Z \subseteq X$ is an irreducible closed subset with generic point $\zeta$, then $\codim_X Z = \dim \OO_{X,\zeta}$, so the irreducible closed subsets of codimension one are exactly the closures of the points whose local ring has dimension one.
:::

::: {.remark}
Dimension depends only on the underlying topological space, so $\dim X = \dim X^\red$.
For example, $\Spec k[\eps]/\eps^2$ has dimension $0$, and its ring of functions has length $2$, equal to its dimension as a $k$-vector space.

For example, $\dim \Spec \ZZ = 1$ and $\dim \ZZ[x] = 2$. The equality $\dim A[x] = \dim A + 1$ holds for Noetherian $A$ but fails in general.
For an integral scheme $X$ of finite type over a field, $\dim X = \trdeg_k k(X)$, and $\codim_X Z + \dim Z = \dim X$ for every irreducible closed subset $Z$.
:::
