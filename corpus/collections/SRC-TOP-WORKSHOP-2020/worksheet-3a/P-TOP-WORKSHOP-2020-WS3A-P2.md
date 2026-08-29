---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-P2
kind: problem
title: A homotopy of the identity forces the represented element to be central
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
<1>1. $\gamma(0) = H(x_0, 0) = H_0(x_0) = x_0$ and $\gamma(1) = H(x_0, 1) = H_1(x_0) = x_0$, so $\gamma$ is a loop based at $x_0$.
Proof: $H_0 = H_1 = \operatorname{id}$.

<1>2. Let $h = [\alpha]$ for a loop $\alpha$ based at $x_0$.
Proof: take an arbitrary element of $\pi_1(X, x_0)$.

<1>3. Define $F : I \times I \to X$ by $F(s, t) = H(\alpha(s), t)$.
Proof: definition.

<1>4. $F$ is a homotopy from $F(\cdot, 0) = H_0 \circ \alpha = \alpha$ to $F(\cdot, 1) = H_1 \circ \alpha = \alpha$.
Proof: <1>3 and $H_0 = H_1 = \operatorname{id}$.

<1>5. The boundary of the square $F$ is: the bottom edge $\alpha$, the top edge $\alpha$, the left edge $F(0, t) = H(\alpha(0), t) = H(x_0, t) = \gamma(t)$, and the right edge $F(1, t) = H(\alpha(1), t) = H(x_0, t) = \gamma(t)$.
Proof: <1>3 and $\alpha(0) = \alpha(1) = x_0$.

<1>6. Hence $\alpha \cdot \gamma \simeq \gamma \cdot \alpha$ (both are homotopic to the boundary of the square, traversed appropriately).
Proof: <1>5 (the square gives a homotopy between the concatenation $\alpha \cdot \gamma$ and $\gamma \cdot \alpha$).

<1>7. Therefore $[\alpha][\gamma] = [\gamma][\alpha]$, i.e. $hg = gh$ for all $h$.
Proof: <1>6.

<1>8. Hence $g$ is in the center of $\pi_1(X, x_0)$.
Proof: <1>7.

<1>9. Q.E.D.
Proof: <1>8.
:::
