---
schema: qual/card@1
id: E-6RQWT
kind: problem
title: Contractibility and the one-point homotopy type
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Recall that a space $X$ is said to be contractible if the identity map of $X$ to itself is nulhomotopic.
Show that $X$ is contractible if and only if $X$ has the homotopy type of a one-point space.
:::

::: {.solution}
**Goal:** Prove that a topological space $X$ is contractible (i.e. $\operatorname{id}_X$ is nullhomotopic) if and only if $X$ is homotopy equivalent to a one-point space $P = \{p_0\}$.

::: pf

::: pf-step

Direct implication ($\implies$): If $X$ is contractible, then $X \simeq \{p_0\}$.
    *Proof:*

::: pf-proof

::: pf-step

By definition of contractibility, $\operatorname{id}_X$ is nullhomotopic: there exists a point $x_0 \in X$ and a continuous homotopy $H: X \times I \to X$ such that $H(x, 0) = x$ and $H(x, 1) = x_0$ for all $x \in X$.

:::

::: pf-step

Let $P = \{p_0\}$ be the one-point space.

:::

::: pf-step

Define continuous maps $f: X \to P$ by $f(x) = p_0$ for all $x \in X$, and $g: P \to X$ by $g(p_0) = x_0$.

:::

::: pf-step

The composition $f \circ g: P \to P$ is the identity map $\operatorname{id}_P$.

:::

::: pf-step

The composition $g \circ f: X \to X$ is the constant map $(g \circ f)(x) = x_0$.

:::

::: pf-step

The homotopy $H$ provides $g \circ f \simeq \operatorname{id}_X$.

:::

::: pf-step

Thus $f$ and $g$ are homotopy inverse equivalences, so $X$ has the homotopy type of a one-point space.

:::

:::

:::

::: pf-step

Converse implication ($\impliedby$): If $X \simeq \{p_0\}$, then $X$ is contractible.
    *Proof:*

::: pf-proof

::: pf-step

Suppose there exist continuous maps $f: X \to P$ and $g: P \to X$ such that $g \circ f \simeq \operatorname{id}_X$.

:::

::: pf-step

Let $x_0 = g(p_0) \in X$.

:::

::: pf-step

Since $P = \{p_0\}$, the only possible value for $f(x)$ is $p_0$, which means:
        $$(g \circ f)(x) = g(f(x)) = g(p_0) = x_0 \quad \text{for all } x \in X.$$

:::

::: pf-step

Thus $g \circ f$ is the constant map $c_{x_0}: X \to X$.

:::

::: pf-step

Because $g \circ f \simeq \operatorname{id}_X$, the identity map $\operatorname{id}_X$ is homotopic to the constant map $c_{x_0}$.

:::

::: pf-step

By definition, $\operatorname{id}_X$ is nullhomotopic, so $X$ is contractible.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    $X$ is contractible if and only if $X$ has the homotopy type of a one-point space. Q.E.D.
:::
