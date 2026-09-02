---
schema: qual/card@1
id: PRB-INDEXP
kind: problem
title: Show a subgroup of index $p$ in a $p\dash$group is normal
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
---

::: problem
Let $G$ be a finite $p\dash$group and $H \leq G$ with $[G:H] = p$.
Show $H \normal G$.
:::

::: solution
Let $G$ act on $G/H$ by left translation, giving $\varphi: G \to S_p$ with $\ker \varphi \leq H$.

::: proof
The image is a $p\dash$group inside $S_p$, hence has order dividing $p$, so $[G : \ker\varphi] \leq p$.
Since $\ker\varphi \leq H$ and $[G:H] = p$, the two coincide and $H = \ker\varphi \normal G$.
:::
:::
