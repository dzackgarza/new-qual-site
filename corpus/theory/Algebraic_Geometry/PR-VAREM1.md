---
schema: qual/card@1
id: PR-VAREM1
kind: proposition
title: The exceptional curve has self-intersection $-1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Intersection Theory
  - Canonical Divisor
relations:
- kind: uses
  target: D-VARBLOW
review: draft
prompts:
- Why does the exceptional curve $E$ in $\Bl_p X$ satisfy $E^2 = -1$?
- What is the canonical class of a blowup?
---

::: {.proposition}
Let $X$ be a smooth projective surface, $\pi: \Bl_p X \to X$ the blowup at a point, $E$ the exceptional curve.
Then
\[
E \cong \PP^1, \qquad E^2 = -1, \qquad K_{\Bl_p X} = \pi^* K_X + E .
\]
In dimension $n$ the last formula reads $K_{\Bl_p X} = \pi^* K_X + (n-1)E$.
:::

::: {.proof title="of the self-intersection"}
Pullback preserves intersection numbers, and $\pi^* A . E = 0$ for every divisor $A$ on $X$, since $\pi_* E = 0$.
For $C \subseteq X$ a curve smooth at $p$, the proper transform satisfies $\pi^* C = \tilde{C} + E$ and $\tilde{C}$ meets $E$ transversally in the one point recording the tangent direction of $C$.
Intersecting with $E$:
\[
0 = \pi^* C . E = (\tilde{C} + E).E = \tilde{C}.E + E^2 = 1 + E^2 .
\]
:::

::: {.remark}
The other route is the one to give if the examiner wants a picture: take two lines in $\PP^2$ meeting transversally away from $p$, so $\pi^* L_1 . \pi^* L_2 = L_1 . L_2 = 1$; move them to meet at $p$, so $\pi^* L_i' = \tilde{L}_i' + E$ and the proper transforms now miss each other; expanding gives $1 = 0 + 1 + 1 + E^2$.
Both arguments run on the same two facts, $\pi^*A.E = 0$ and $\pi^*C = \tilde{C} + E$.

The consequence is Castelnuovo's criterion — a smooth rational curve with $E^2 = -1$ on a surface is the exceptional curve of a blowup and can be contracted — which is what makes minimal models of surfaces possible.
The canonical formula is the reason blowing up strictly increases $K^2$-deficiency: $K^2$ drops by one each time, and $p_a$ and $p_g$ do not change.
:::
