---
schema: qual/card@1
id: P-CASP05C
kind: problem
title: "Schwarz lemma variants: identity for simply connected and bounded domains"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $G \subset \mathbb{C}$ be a connected open set with $0 \in G$, and $f \in H(G)$, with $f(0) = 0$, $f'(0) = 1$ and $f(G) \subset G$.

(a) Show that if $G \neq \mathbb{C}$ and $G$ is simply connected (not necessarily bounded) then $f(z) \equiv z$.
Does the same conclusion hold for $G = \mathbb{C}$?

(b) Show that if $G$ is bounded (not necessarily simply connected) then $f(z) \equiv z$.

Hint for (b): Prove by contradiction.
Consider the $n$th iterate $f_n := f \circ f \circ \cdots \circ f$ ($n$ times), and compute the first non-vanishing coefficient of the Taylor series of $f_n(z) - z$ at 0 in terms of that of $f(z) - z$.
:::
