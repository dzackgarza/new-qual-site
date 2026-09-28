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
Let $\mathbb{H} = \{z : \operatorname{Im} z > 0\}$ denote the upper half plane.
Let $u : \mathbb{H} \to \mathbb{R}$ be a continuous bounded function which is harmonic in $\mathbb{H}$ and $u = 0$ on $\partial\mathbb{H}$.
Show that $u$ is constant.
:::

::: {.solution}
Reflect $u$ oddly across the real axis:
\[
U(z)=
\begin{cases}
u(z),&\operatorname{Im}z\ge0,\\
-u(\bar z),&\operatorname{Im}z<0.
\end{cases}
\]
Because $u$ is continuous up to the boundary and vanishes on
$\mathbb R$, the harmonic reflection principle shows that $U$ is harmonic on
all of $\mathbb C$. It is bounded because $u$ is bounded. Liouville's theorem
for harmonic functions therefore makes $U$ constant. Since $U$ is odd under
reflection across $\mathbb R$, that constant must be $0$. Hence
\[
u\equiv0
\]
on the upper half-plane.
:::
