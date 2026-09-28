---
schema: qual/card@1
id: D-VWYRN
kind: definition
title: Pullback of spaces
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $f\colon X\to Z$ and $g\colon Y\to Z$ be continuous maps of topological spaces.
The \dfn{pullback} of $f$ and $g$ is the subspace
$$
X \cross_Z Y \coloneqq \ts{ (x,y) \in X\cross Y \st f(x) = g(y) }
$$
of the product space $X\cross Y$, together with the restrictions $p_X\colon X\cross_Z Y\to X$ and $p_Y\colon X\cross_Z Y\to Y$ of the two projections.
:::

::: {.proposition}
In the setting of the definition, $f\circ p_X = g\circ p_Y$, and for every topological space $W$ and continuous maps $a\colon W\to X$ and $b\colon W\to Y$ with $f\circ a = g\circ b$ there is a unique continuous map $u\colon W\to X\cross_Z Y$ with $p_X\circ u = a$ and $p_Y\circ u = b$, namely $u(w) = (a(w), b(w))$.
Thus $X\cross_Z Y$ is the [[D-QXER7|limit]] of the diagram $X\xrightarrow{f} Z \xleftarrow{g} Y$ in $\Top$.
If $Z$ is a point, then $X\cross_Z Y = X\cross Y$.
:::

::: {.concept}
[@Hat02].
:::
