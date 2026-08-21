---
schema: qual/card@1
id: D-SOVXO
kind: definition
title: Homotopy
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition title="Homotopy"}
Let $X, Y$ be topological spaces and $f,g: X \to Y$ continuous maps.
Then a **homotopy** from $f$ to $g$ is a continuous function

$F: X \cross I \into Y$

such that

$F(x, 0) = f(x)$ and  $F(x,1) = g(x)$

for all $x\in X$.
If such a homotopy exists, we write $f\homotopic g$.
This is an equivalence relation on $\text{Hom}(X,Y)$, and the set of such classes is denoted $[X,Y] \definedas \hom (X,Y)/\homotopic$.
:::
