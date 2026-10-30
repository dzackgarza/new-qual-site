---
schema: qual/card@1
id: P-CAF24G
kind: problem
title: Bounded harmonic function on the upper half-plane vanishing on the boundary is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $\halfplane = \{z : \operatorname{Im} z > 0\}$ denote the upper half plane.
Let $u : \overline{\halfplane} \to \RR$ be a continuous bounded function which is harmonic in $\halfplane$ and $u = 0$ on $\partial\halfplane$.
Show that $u$ is constant.
:::

::: {.solution}
Reflect $u$ oddly across the real axis:
$$
U(z)=
\begin{cases}
u(z),&\operatorname{Im}z\ge0,\\
-u(\bar z),&\operatorname{Im}z<0.
\end{cases}
$$
Because $u$ is continuous up to the boundary and vanishes on
$\RR$, the harmonic reflection principle shows that $U$ is harmonic on
all of $\CC$. It is bounded because $u$ is bounded. Liouville's theorem
for harmonic functions therefore makes $U$ constant. Since $U$ is odd under
reflection across $\RR$, that constant must be $0$. Hence
$$
u\equiv0
$$
on the upper half-plane.
:::
