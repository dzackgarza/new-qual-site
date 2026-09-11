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
The **dimension** of $X$ is the supremum of $n$ over chains
\[
Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n
\]
of irreducible closed subsets of $X$; the length counts links, not sets.
The **codimension** of an irreducible closed $Z \subseteq X$ is the supremum of lengths of such chains starting at $Z_0 = Z$; for arbitrary closed $Y$ take the infimum over irreducible $Z \subseteq Y$.
:::

::: {.proposition}
$\dim \Spec A = \krulldim A$, since irreducible closed subsets of $\Spec A$ correspond to primes, order-reversingly.
The codimension of $V(\mfp)$ is the height of $\mfp$.
:::

::: {.remark}
Dimension is topological, so it cannot see nilpotents: $\dim X = \dim X^\red$, and $\Spec k[\eps]/\eps^2$ has dimension $0$ despite a two-dimensional ring of functions.
That is the standard trap, and the honest correction is that length, not dimension, measures the extra structure.

Dimension is not local in the naive sense, and it is not additive: $\dim \Spec \ZZ = 1$, $\dim \ZZ[x] = 2$, and $\dim A[x] = \dim A + 1$ holds for Noetherian $A$ but fails in general.
For an integral scheme of finite type over a field, $\dim X = \trdeg_k k(X)$, and codimension and dimension add up — $\codim_X Z + \dim Z = \dim X$ — which is the case that matches intuition and the case where that identity is safe to use.
:::
