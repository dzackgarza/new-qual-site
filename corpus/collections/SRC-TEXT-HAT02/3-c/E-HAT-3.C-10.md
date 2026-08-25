---
schema: qual/card@1
id: E-HAT-3.C-10
kind: exercise
title: "Product of maps in an H-space"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

Let $X$ be a path-connected H-space with $H^*(X; R)$ free and finitely generated in each dimension.
For maps $f, g: X \to X$, the product $fg: X \to X$ is defined by $(fg)(x) = f(x)g(x)$, using the H-space product.

(a) Show that $(fg)^*(\alpha) = f^*(\alpha) + g^*(\alpha)$ for primitive elements $\alpha \in H^*(X; R)$.

(b) Deduce that the $k$-th power map $x \mapsto x^k$ induces the map $\alpha \mapsto k\alpha$ on primitive elements $\alpha$.
In particular the quaternionic $k$-th power map $S^3 \to S^3$ has degree $k$.

(c) Show that every polynomial $a_n x^n + \dotsb + a_1 x + a_0$ of nonzero degree with coefficients in $\mathbb{H}$ has a root in $\mathbb{H}$.
[See Theorem 1.8.]
