---
schema: qual/card@1
id: E-WVNJ2
kind: exercise
title: Orbit spaces of compact group actions inherit separation properties
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Quotient Topology
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §31.8"}

Let $X$ be a space; let $G$ be a topological group.
An action of $G$ on $X$ is a continuous map $\alpha: G \times X \to X$ such that, denoting $\alpha(g \times x)$ by $g \cdot x$, one has:

(i) $e \cdot x = x$ for all $x \in X$.

(ii) $g_1 \cdot (g_2 \cdot x) = (g_1 \cdot g_2) \cdot x$ for all $x \in X$ and $g_1, g_2 \in G$.

Define $x \sim g \cdot x$ for all $x$ and $g$; the resulting quotient space is denoted $X/G$ and called the orbit space of the action $\alpha$.

Theorem.
Let $G$ be a compact topological group; let $X$ be a topological space; let $\alpha$ be an action of $G$ on $X$.
If $X$ is Hausdorff, or regular, or normal, or locally compact, or second-countable, so is $X/G$.

[Hint: See Exercise 13 of §26.]
:::
