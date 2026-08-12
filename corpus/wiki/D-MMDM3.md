---
schema: qual/card@1
id: D-MMDM3
kind: definition
title: "CW Cell"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="CW Cell"}
An $n\dash$cell of $X$, say $e^n$, is the image of a map $\Phi: B^n \to X$.
That is, $e^n = \Phi(B^n)$.
Attaching an $n\dash$cell to $X$ is equivalent to forming the space $B^n \coprod_{f} X$ where $f: \del B^n \to X$.

- A $0\dash$cell is a point.

- A $1\dash$cell is an interval $[-1, 1] = B^1 \subset \RR^1$.
  Attaching requires a map from $S^0 =\theset{-1, +1} \to X$

- A $2\dash$cell is a solid disk $B^2 \subset \RR^2$ in the plane.
  Attaching requires a map $S^1 \to X$.

- A $3\dash$cell is a solid ball $B^3 \subset \RR^3$.
  Attaching requires a map from the sphere $S^2 \to X$.
:::
