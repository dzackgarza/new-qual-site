---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-P2
kind: problem
title: The loop traced by the basepoint under a self-homotopy of the identity is central in $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
(May 2017) If $H:X\times[0,1]\to X$ is a homotopy with $H_0=H_1$ the identity map, show that the map $\gamma:I\to X$ given by $\gamma(t)=H(x_0,t)$ is a loop representing an element $g=[\gamma]\in\pi_1(X,x_0)$ which lies in the center of $\pi_1(X,x_0)$, i.e. $gh=hg$ for all $h\in\pi_1(X,x_0)$.
:::

::: {.solution}
<1>1. $\gamma$ is a loop based at $x_0$.
::: {.proof}
$\gamma(0) = H_0(x_0) = x_0$ and $\gamma(1) = H_1(x_0) = x_0$ because $H_0 = H_1 = \operatorname{id}_X$.
:::

<1>2. For every loop $\alpha$ at $x_0$, the map $F\colon I \times I \to X$, $F(s, t) = H(\alpha(s), t)$, has bottom and top edges $\alpha$ and left and right edges $\gamma$.
::: {.proof}
$F(s, 0) = H_0(\alpha(s)) = \alpha(s)$ and $F(s, 1) = H_1(\alpha(s)) = \alpha(s)$. Since $\alpha(0) = \alpha(1) = x_0$, $F(0, t) = F(1, t) = H(x_0, t) = \gamma(t)$.
:::

<1>3. For every loop $\alpha$ at $x_0$, $\alpha \cdot \gamma \simeq \gamma \cdot \alpha$ relative to the endpoints.
::: {.proof}
For a map $F\colon I \times I \to X$, the path along the bottom edge followed by the right edge and the path along the left edge followed by the top edge are paths in the convex square from $(0,0)$ to $(1,1)$, hence homotopic in $I \times I$ relative to the endpoints; composing with $F$ gives a homotopy relative to the endpoints between their images. By step <1>2 these images are $\alpha \cdot \gamma$ and $\gamma \cdot \alpha$.
:::

<1>4. Q.E.D.
::: {.proof}
By step <1>3, $[\alpha][\gamma] = [\gamma][\alpha]$ for every $h = [\alpha] \in \pi_1(X, x_0)$, so $g = [\gamma]$ lies in the center of $\pi_1(X, x_0)$.
:::
:::
