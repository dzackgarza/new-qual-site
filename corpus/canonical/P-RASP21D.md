---
schema: qual/card@1
id: P-RASP21D
kind: problem
title: "Separately bounded bilinear maps on Banach spaces are jointly bounded"
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
Let $X, Y, Z$ be Banach spaces and $B : X \times Y \to Z$ be a map such that for any fixed $x \in X$ we have $B(x, \cdot) \in L(Y, Z)$ and for any fixed $y \in Y$ we have $B(\cdot, y) \in L(X, Z)$.
Show that there is $C \geq 0$ such that $\|B(x, y)\| \leq C \|x\| \|y\|$ for all $(x, y) \in X \times Y$.
:::
