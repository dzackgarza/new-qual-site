---
schema: qual/card@1
id: P-TOPF23C
kind: problem
title: "Intersection forms on mod-2 homology of the torus, Klein bottle, and RP^2 # RP^2"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Intersection Theory
  - Surfaces
  - Mod 2
relations: []
review: draft
---

::: problem
The torus $T$, the Klein bottle $K$ and the connect-sum $C = \mathbb{RP}^2 \# \mathbb{RP}^2$ all have isomorphic mod-$2$ homology groups.
Compute the intersection forms (on the first homology with mod-$2$ coefficients) of these three spaces; to what extent are they distinguishable using these intersection forms?
:::

::: {.solution}
<1>1. For the torus $T^2$, choose the standard meridian and longitude classes $a,b\in H_1(T^2;\mathbb F_2)$. Its intersection matrix is
$$\boxed{\begin{pmatrix}0&1\\1&0\end{pmatrix}.}$$
::: {.proof}
Each standard curve has self-intersection $0$, and they meet transversely in one point.
:::

<1>2. The Klein bottle is homeomorphic to $\mathbb{RP}^2\#\mathbb{RP}^2$. For either description, choose the two one-sided crosscap curves $x,y$. The intersection matrix is
$$\boxed{\begin{pmatrix}1&0\\0&1\end{pmatrix}.}$$
::: {.proof}
The crosscap curves may be chosen disjoint from each other, while each one-sided curve has mod-$2$ self-intersection $1$.
:::

<1>3. Thus the Klein bottle and $C=\mathbb{RP}^2\#\mathbb{RP}^2$ have identical intersection forms, as they must because they are homeomorphic.
::: {.proof}
The connected sum of two projective planes is precisely the nonorientable genus-$2$ surface, i.e. the Klein bottle.
:::

<1>4. The torus form is not isometric to the other two over $\mathbb F_2$.
::: {.proof}
The torus form is alternating: $v\cdot v=0$ for every $v$. The diagonal form is nonalternating since $x\cdot x=1$. Alternation is invariant under change of basis.
:::

<1>5. Hence the intersection form distinguishes the torus from the Klein bottle, but cannot distinguish the Klein bottle from $\mathbb{RP}^2\#\mathbb{RP}^2$.
::: {.proof}
Combine <1>1--<1>4.
:::
:::
