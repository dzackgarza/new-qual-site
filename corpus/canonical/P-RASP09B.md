---
schema: qual/card@1
id: P-RASP09B
kind: problem
title: "Bilinear maps on Banach spaces: separate boundedness implies joint continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Bilinear Maps
  - Uniform Boundedness Principle
relations: []
review: draft
solved: false
---

::: problem
Assume that $X, Y, Z$ are Banach spaces. Assume $\Phi : X \times Y \to Z$ is bilinear, namely for every $x \in X$, $\Phi(x, \cdot) : Y \to Z$ is linear and for every $y \in Y$, $\Phi(\cdot, y) : X \to Z$ is linear. Show that if for every $z^* \in Z^*$, $z^*(\Phi(x, \cdot)) \in Y^*$ and $z^*(\Phi(\cdot, y)) \in X^*$, then:

(1) $\Phi_x(\cdot) = \Phi(x, \cdot) : Y \to Z$ and $\Phi_y(\cdot) = \Phi(\cdot, y) : X \to Z$ are bounded linear maps;

(2) there exists $M$ such that
$$
\|\Phi(x, y)\| \leq M \|x\| \|y\|.
$$
:::