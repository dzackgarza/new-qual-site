---
schema: qual/card@1
id: T-OBPSZ
kind: theorem
title: Orbit-stabilizer theorem
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: D-WYC7C
- kind: uses
  target: T-SZRXI
review: reviewed
---

::: {.theorem}
If $G$ acts on $X$ and $x\in X$, the map
$$
G/G_x\longrightarrow G\cdot x,
\qquad
gG_x\longmapsto g\cdot x
$$
is a bijection. If $G$ is finite, then
$$
\abs{G\cdot x}=[G:G_x]=\frac{\abs G}{\abs{G_x}}.
$$

::: {.proof}
Every point in the orbit has the form $g\cdot x$, so the map is surjective.
Moreover, $g\cdot x=h\cdot x$ exactly when $h^{-1}g\in G_x$, which is exactly
when $gG_x=hG_x$. Thus the map is also well-defined and injective. The
cardinality formula follows from Lagrange's theorem.
:::
:::
