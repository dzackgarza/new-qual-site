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

::: solution
**Goal:** Prove that the product space $\mathbb{R}^J$ and all retracts of $\mathbb{R}^J$ satisfy the Universal Extension Property (UEP).

<1>1. Part (a): $\mathbb{R}^J$ has the Universal Extension Property.
    *Proof:*
    <2>1. Let $X$ be a normal space, $A \subseteq X$ a closed subset, and $f: A \to \mathbb{R}^J$ a continuous map.
    <2>2. For each $\alpha \in J$, let $\pi_\alpha: \mathbb{R}^J \to \mathbb{R}$ be the canonical projection onto the $\alpha$-th coordinate.
    <2>3. The coordinate map $f_\alpha = \pi_\alpha \circ f: A \to \mathbb{R}$ is continuous.
    <2>4. By the Tietze Extension Theorem (Theorem 35.1), because $X$ is normal and $A$ is closed, there exists a continuous map $g_\alpha: X \to \mathbb{R}$ extending $f_\alpha$, so $g_\alpha|_A = f_\alpha$.
    <2>5. Define $g: X \to \mathbb{R}^J$ by $g(x) = (g_\alpha(x))_{\alpha \in J}$.
    <2>6. By the universal property of the product topology, $g$ is continuous because each coordinate function $\pi_\alpha \circ g = g_\alpha$ is continuous.
    <2>7. For any $a \in A$, $\pi_\alpha(g(a)) = g_\alpha(a) = f_\alpha(a) = \pi_\alpha(f(a))$ for all $\alpha \in J$, so $g(a) = f(a)$.
    <2>8. Thus $g$ is a continuous extension of $f$ to $X$.

<1>2. Part (b): Retracts of $\mathbb{R}^J$ have the Universal Extension Property.
    *Proof:*
    <2>1. Let $Y$ be a retract of $\mathbb{R}^J$ (the case where $Y$ is homeomorphic to a retract follows by composing with the homeomorphism).
    <2>2. Let $i: Y \hookrightarrow \mathbb{R}^J$ be the inclusion map, and let $r: \mathbb{R}^J \to Y$ be a continuous retraction, so $r \circ i = \operatorname{id}_Y$.
    <2>3. Let $X$ be normal, $A \subseteq X$ closed, and $f: A \to Y$ continuous.
    <2>4. The composite map $i \circ f: A \to \mathbb{R}^J$ is continuous.
    <2>5. By Part (a), $i \circ f$ extends to a continuous map $G: X \to \mathbb{R}^J$ such that $G|_A = i \circ f$.
    <2>6. Define $g: X \to Y$ by $g = r \circ G$.
    <2>7. $g$ is continuous as the composition of continuous maps.
    <2>8. For all $a \in A$:
        $$g(a) = r(G(a)) = r((i \circ f)(a)) = (r \circ i)(f(a)) = \operatorname{id}_Y(f(a)) = f(a).$$
    <2>9. Thus $g$ is a continuous extension of $f$ to $X$.

<1>3. Conclusion:
    $\mathbb{R}^J$ and all its retracts satisfy the Universal Extension Property. Q.E.D.
:::
