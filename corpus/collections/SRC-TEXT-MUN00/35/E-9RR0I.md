---
schema: qual/card@1
id: E-9RR0I
kind: problem
title: The universal extension property
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

A space $Y$ is said to have the universal extension property if for each triple consisting of a normal space $X$, a closed subset $A$ of $X$, and a continuous function $f: A \to Y$, there exists an extension of $f$ to a continuous map of $X$ into $Y$.

(a) Show that $\mathbb{R}^J$ has the universal extension property.

(b) Show that if $Y$ is homeomorphic to a retract of $\mathbb{R}^J$, then $Y$ has the universal extension property.
:::

::: {.solution}
**Goal:** Prove that the product space $\mathbb{R}^J$ and all retracts of $\mathbb{R}^J$ satisfy the Universal Extension Property (UEP).

::: pf

::: pf-step
Part (a): $\mathbb{R}^J$ has the Universal Extension Property.

::: pf-proof

::: pf-step
Let $X$ be a normal space, $A \subseteq X$ a closed subset, and $f: A \to \mathbb{R}^J$ a continuous map.
:::

::: pf-step
For each $\alpha \in J$, let $\pi_\alpha: \mathbb{R}^J \to \mathbb{R}$ be the canonical projection onto the $\alpha$-th coordinate.
:::

::: pf-step
The coordinate map $f_\alpha = \pi_\alpha \circ f: A \to \mathbb{R}$ is continuous.
:::

::: pf-step
By the Tietze Extension Theorem (Theorem 35.1), because $X$ is normal and $A$ is closed, there exists a continuous map $g_\alpha: X \to \mathbb{R}$ extending $f_\alpha$, so $g_\alpha|_A = f_\alpha$.
:::

::: pf-step
Define $g: X \to \mathbb{R}^J$ by $g(x) = (g_\alpha(x))_{\alpha \in J}$.
:::

::: pf-step
By the universal property of the product topology, $g$ is continuous because each coordinate function $\pi_\alpha \circ g = g_\alpha$ is continuous.
:::

::: pf-step
For any $a \in A$, $\pi_\alpha(g(a)) = g_\alpha(a) = f_\alpha(a) = \pi_\alpha(f(a))$ for all $\alpha \in J$, so $g(a) = f(a)$.
:::

::: pf-step
Thus $g$ is a continuous extension of $f$ to $X$.
:::

:::

:::

::: pf-step
Part (b): Retracts of $\mathbb{R}^J$ have the Universal Extension Property.

::: pf-proof

::: pf-step
Let $Y$ be a retract of $\mathbb{R}^J$ (the case where $Y$ is homeomorphic to a retract follows by composing with the homeomorphism).
:::

::: pf-step
Let $i: Y \hookrightarrow \mathbb{R}^J$ be the inclusion map, and let $r: \mathbb{R}^J \to Y$ be a continuous retraction, so $r \circ i = \operatorname{id}_Y$.
:::

::: pf-step
Let $X$ be normal, $A \subseteq X$ closed, and $f: A \to Y$ continuous.
:::

::: pf-step
The composite map $i \circ f: A \to \mathbb{R}^J$ is continuous.
:::

::: pf-step
By Part (a), $i \circ f$ extends to a continuous map $G: X \to \mathbb{R}^J$ such that $G|_A = i \circ f$.
:::

::: pf-step
Define $g: X \to Y$ by $g = r \circ G$.
:::

::: pf-step
$g$ is continuous as the composition of continuous maps.
:::

::: pf-step
For all $a \in A$:
$$g(a) = r(G(a)) = r((i \circ f)(a)) = (r \circ i)(f(a)) = \operatorname{id}_Y(f(a)) = f(a).$$
:::

::: pf-step
Thus $g$ is a continuous extension of $f$ to $X$.
:::

:::

:::

::: pf-step
Conclusion:
$\mathbb{R}^J$ and all its retracts satisfy the Universal Extension Property. Q.E.D.
:::

:::

:::
