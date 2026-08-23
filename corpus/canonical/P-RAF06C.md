---
schema: qual/card@1
id: P-RAF06C
kind: problem
title: "Range and nullspace of T and T*: orthogonal complements and closed range"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Bounded Operators
  - Adjoints
  - Closed Range
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a Hilbert space, $T : H \to H$ a bounded linear operator, $T^* : H \to H$ its adjoint (i.e. $(Tx, y) = (x, T^*y)$ for all $x, y \in H$), and $R(T)$, $N(T)$ its range and nullspace, respectively.

(a) Show that $N(T^*) = R(T)^\perp$ and $R(T^*) = N(T)^\perp$.

(b) Show that $R(T^*)$ is closed if $R(T)$ is closed.

Hint for (b): Show that, for every $y \in N(T)^\perp$, there is a bounded linear functional $\Lambda : R(T) \to \mathbb{C}$ with the property that $\Lambda(Tx) = (x, y)$. Use this to show that $N(T)^\perp \subset R(T^*)$.
:::