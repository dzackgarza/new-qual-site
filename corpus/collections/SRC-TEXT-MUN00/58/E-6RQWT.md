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

::: solution
**Goal:** Prove that a topological space $X$ is contractible (i.e. $\operatorname{id}_X$ is nullhomotopic) if and only if $X$ is homotopy equivalent to a one-point space $P = \{p_0\}$.

<1>1. Direct implication ($\implies$): If $X$ is contractible, then $X \simeq \{p_0\}$.
    *Proof:*
    <2>1. By definition of contractibility, $\operatorname{id}_X$ is nullhomotopic: there exists a point $x_0 \in X$ and a continuous homotopy $H: X \times I \to X$ such that $H(x, 0) = x$ and $H(x, 1) = x_0$ for all $x \in X$.
    <2>2. Let $P = \{p_0\}$ be the one-point space.
    <2>3. Define continuous maps $f: X \to P$ by $f(x) = p_0$ for all $x \in X$, and $g: P \to X$ by $g(p_0) = x_0$.
    <2>4. The composition $f \circ g: P \to P$ is the identity map $\operatorname{id}_P$.
    <2>5. The composition $g \circ f: X \to X$ is the constant map $(g \circ f)(x) = x_0$.
    <2>6. The homotopy $H$ provides $g \circ f \simeq \operatorname{id}_X$.
    <2>7. Thus $f$ and $g$ are homotopy inverse equivalences, so $X$ has the homotopy type of a one-point space.

<1>2. Converse implication ($\impliedby$): If $X \simeq \{p_0\}$, then $X$ is contractible.
    *Proof:*
    <2>1. Suppose there exist continuous maps $f: X \to P$ and $g: P \to X$ such that $g \circ f \simeq \operatorname{id}_X$.
    <2>2. Let $x_0 = g(p_0) \in X$.
    <2>3. Since $P = \{p_0\}$, the only possible value for $f(x)$ is $p_0$, which means:
        $$(g \circ f)(x) = g(f(x)) = g(p_0) = x_0 \quad \text{for all } x \in X.$$
    <2>4. Thus $g \circ f$ is the constant map $c_{x_0}: X \to X$.
    <2>5. Because $g \circ f \simeq \operatorname{id}_X$, the identity map $\operatorname{id}_X$ is homotopic to the constant map $c_{x_0}$.
    <2>6. By definition, $\operatorname{id}_X$ is nullhomotopic, so $X$ is contractible.

<1>3. Conclusion:
    $X$ is contractible if and only if $X$ has the homotopy type of a one-point space. Q.E.D.
:::
