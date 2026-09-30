---
schema: qual/card@1
id: E-2X3VM
kind: problem
title: Behavior of path connectedness under products, closures, images, and unions
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

(a) Is a product of path-connected spaces necessarily path connected?

(b) If $A \subset X$ and $A$ is path connected, is $\overline{A}$ necessarily path connected?

(c) If $f: X \to Y$ is continuous and $X$ is path connected, is $f(X)$ necessarily path connected?

(d) If $\theset{A_\alpha}$ is a collection of path-connected subspaces of $X$ and if $\bigcap A_\alpha \neq \varnothing$, is $\bigcup A_\alpha$ necessarily path connected?
:::

::: {.solution}
::: pf

::: {.pf-step #part-a}
(a) $\boxed{\text{Yes}}$: a product $\prod_{\alpha\in J}X_\alpha$ of path-connected spaces is path connected.

::: pf-proof
Given $\mathbf x,\mathbf y$ in the product, choose paths $\gamma_\alpha\colon[0,1]\to X_\alpha$ from $x_\alpha$ to $y_\alpha$.
The map $\gamma(t)=(\gamma_\alpha(t))_\alpha$ is continuous because its coordinates are, and it is a path from $\mathbf x$ to $\mathbf y$.
:::

:::

::: {.pf-step #part-b}
(b) $\boxed{\text{No}}$: the closure of a path-connected set need not be path connected.

::: pf-proof
The set $A=\{(x,\sin(1/x)):0<x\le1\}\subseteq\mathbb R^2$ is the image of $(0,1]$ under a continuous map, hence path connected.
Its closure $\overline A=A\cup(\{0\}\times[-1,1])$ is the topologist's sine curve, which is not path connected: no path in $\overline A$ joins $(0,0)$ to a point of $A$.
:::

:::

::: {.pf-step #part-c}
(c) $\boxed{\text{Yes}}$: if $f\colon X\to Y$ is continuous and $X$ is path connected, $f(X)$ is path connected.

::: pf-proof
For $f(x_1),f(x_2)\in f(X)$, choose a path $\gamma$ in $X$ from $x_1$ to $x_2$; then $f\circ\gamma$ is a path in $f(X)$ from $f(x_1)$ to $f(x_2)$.
:::

:::

::: {.pf-step #part-d}
(d) $\boxed{\text{Yes}}$: if the $A_\alpha$ are path connected and $p\in\bigcap_\alpha A_\alpha$, then $\bigcup_\alpha A_\alpha$ is path connected.

::: pf-proof
For $x\in A_\beta$ and $y\in A_\delta$, choose a path in $A_\beta$ from $x$ to $p$ and a path in $A_\delta$ from $p$ to $y$; their concatenation is a path in $\bigcup_\alpha A_\alpha$ from $x$ to $y$.
:::

:::

::: pf-qed
Steps [](#part-a){.pf-ref} through [](#part-d){.pf-ref} answer (a) through (d).
:::

:::

:::
