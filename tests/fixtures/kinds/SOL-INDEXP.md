---
schema: qual/card@1
id: SOL-INDEXP
kind: solution
title: Index $p$ normality via the action on cosets
classification:
  areas:
  - algebra
  topics:
  - groups
relations:
- kind: solves
  target: PRB-INDEXP
review: draft
---

::: solution
Let $G$ act on $G/H$ by left translation, giving $\varphi: G \to S_p$ with
$\ker \varphi \leq H$.

::: proof
The image is a $p\dash$group inside $S_p$, hence has order dividing $p$, so
$[G : \ker\varphi] \leq p$. Since $\ker\varphi \leq H$ and $[G:H] = p$, the two
coincide and $H = \ker\varphi \normal G$.
:::
:::
