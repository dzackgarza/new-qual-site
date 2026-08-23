---
schema: qual/card@1
id: P-RAF11B
kind: problem
title: "Weak topology on infinite-dimensional Banach spaces"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
(a) Let $X$ be an infinite dimensional Banach space.
Prove that $X$ endowed with the weak topology is not a complete metric space.

Hint: Begin by showing that any norm bounded set in $X$ is nowhere dense in the weak topology.

(b) Let $X$ be a Banach space and $X^*$ its dual.
Suppose that there exists countably many linear functionals $L_n \in X^*$ with the following property: any sequence $x_j, x \in X$ converges weakly $x_j \to x$ iff $L_n(x_j) \to L_n(x)$ for all $n$.
Show that $X$ must be finite dimensional.

Hint: Consider the function $d(x,y) = \sum_n 2^{-n} \frac{|L_n(x-y)|}{1 + |L_n(x-y)|}$.
:::
