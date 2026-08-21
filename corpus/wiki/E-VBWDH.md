---
schema: qual/card@1
id: E-VBWDH
kind: exercise
title: Uniform boundedness principle
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §48.10"}


Prove the following.

Theorem (Uniform boundedness principle). Let $X$ be a complete metric space, and let $\mathcal{F}$ be a subset of $\mathcal{C}(X, \mathbb{R})$ such that for each $a \in X$, the set

$$
\mathcal{F}_a = \ts{f(a) \mid f \in \mathcal{F}}
$$

is bounded. Then there is a nonempty open set $U$ of $X$ on which the functions in $\mathcal{F}$ are uniformly bounded, that is, there is a number $M$ such that $\abs{f(x)} \leq M$ for all $x \in U$ and all $f \in \mathcal{F}$. [Hint: Let $A_N = \ts{x \mid \abs{f(x)} \leq N \text{ for all } f \in \mathcal{F}}$.]
:::
