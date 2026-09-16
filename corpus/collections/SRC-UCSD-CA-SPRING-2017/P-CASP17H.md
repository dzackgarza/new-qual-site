---
schema: qual/card@1
id: P-CASP17H
kind: problem
title: "Bounded harmonic functions on C and on the upper half-plane with zero boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
  - Maximum Principle
relations: []
review: draft
---

::: {.problem}
(i) Let $u : \mathbb{C} \to \mathbb{R}$ be a harmonic function which is bounded.
Show that $u$ is constant.

(ii) Let $H = \{z : \operatorname{Im} z > 0\}$ denote the upper half plane.
Let $u : H \to \mathbb{R}$ be a continuous bounded function which is harmonic in $H$ and $u = 0$ on $\partial H$.
Show that $u$ is constant.
:::

::: {.solution}
For (i), since $\mathbb C$ is simply connected, $u$ has a harmonic conjugate
$v$, so $F=u+iv$ is entire. If $u$ is bounded above, then
\[
|e^{F(z)}|=e^{u(z)}
\]
is bounded. Liouville's theorem makes $e^F$ constant, hence $F'\equiv0$ and
$u$ is constant.

For (ii), reflect $u$ oddly across the real axis:
\[
U(x+iy)=
\begin{cases}
u(x+iy),&y\ge0,\\
-u(x-iy),&y<0.
\end{cases}
\]
Because $u$ is continuous up to the boundary and vanishes there, the harmonic
reflection principle shows that $U$ is harmonic on all of $\mathbb C$.
It is bounded, so part (i) implies that $U$ is constant. Oddness forces that
constant to be $0$. Hence $u\equiv0$ on $H$.
:::
