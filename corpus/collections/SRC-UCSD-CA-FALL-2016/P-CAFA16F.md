---
schema: qual/card@1
id: P-CAFA16F
kind: problem
title: "Infinite Blaschke product converges but cannot be extended past the boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
For $k \geq 1$, let $a_k = 1 - 1/k^2$.
For $n \geq 1$, define $f_n: \mathbb{D} \to \mathbb{D}$ by $f_n(z) = \prod_{k=1}^{n} \frac{a_k - z}{1 - a_k z}$.

(a) Prove that the sequence $\{f_n\}$ converges to an analytic function $f: \mathbb{D} \to \mathbb{D}$, uniformly on compact subsets of $\mathbb{D}$.

(b) Prove that there do not exist an open set $U \subset \mathbb{C}$ and an analytic function $g: U \to \mathbb{C}$ such that $\overline{\mathbb{D}} \subset U$ and $g(z) = f(z)$ for every $z \in \mathbb{D}$.
:::
