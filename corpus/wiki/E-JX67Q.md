---
schema: qual/card@1
id: E-JX67Q
kind: exercise
title: The Cantor set
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §27.6"}

Let $A_0$ be the closed interval $[0, 1]$ in $\mathbb{R}$.
Let $A_1$ be the set obtained from $A_0$ by deleting its "middle third" $(\tfrac{1}{3}, \tfrac{2}{3})$.
Let $A_2$ be the set obtained from $A_1$ by deleting its "middle thirds" $(\tfrac{1}{9}, \tfrac{2}{9})$ and $(\tfrac{7}{9}, \tfrac{8}{9})$.
In general, define $A_n$ by the equation

$$
A_n = A_{n-1} - \bigcup_{k=0}^{\infty} \left( \frac{1+3k}{3^n}, \frac{2+3k}{3^n} \right).
$$

The intersection

$$
C = \bigcap_{n \in \mathbb{Z}_+} A_n
$$

is called the Cantor set; it is a subspace of $[0, 1]$.

(a) Show that $C$ is totally disconnected.

(b) Show that $C$ is compact.

(c) Show that each set $A_n$ is a union of finitely many disjoint closed intervals of length $1/3^n$; and show that the end points of these intervals lie in $C$.

(d) Show that $C$ has no isolated points.

(e) Conclude that $C$ is uncountable.
:::
