---
schema: qual/card@1
id: P-AGH54INTMULT
kind: problem
title: Intersection multiplicity $(Y \cdot Z)_P$ and Bézout for a line
classification:
  areas:
  - algebraic-geometry
  topics:
  - Intersection Theory
  - Plane Curves
  - Multiplicity
relations: []
review: draft
---

::: problem
Let $Y, Z \subseteq \AA^2$ be two distinct curves, given by equations $f = 0$ and $g = 0$.
For $P \in Y \intersect Z$, define the *intersection multiplicity* $(Y \cdot Z)_P$ of $Y$ and $Z$ at $P$ to be the length of the $\mco_P\da$module $\mco_P / \gens{f, g}$.

1. Show that $(Y \cdot Z)_P$ is finite, and that $(Y \cdot Z)_P \geq \mu_P(Y) \cdot \mu_P(Z)$.

2. If $P \in Y$, show that for almost all lines $L$ through $P$, that is, all but a finite number, one has $(L \cdot Y)_P = \mu_P(Y)$.

3. If $Y$ is a curve of degree $d$ in $\PP^2$, and $L$ is a line in $\PP^2$ with $L \neq Y$, show that $(L \cdot Y) = d$.
   Here $(L \cdot Y) = \sum (L \cdot Y)_P$, summed over all points $P \in L \intersect Y$, where $(L \cdot Y)_P$ is computed using a suitable affine cover of $\PP^2$.
:::
