---
schema: qual/card@1
id: P-CASP04D
kind: problem
title: "Basin of attraction of a fixed point with contraction coefficient"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G$ be an open connected and bounded subset of $\mathbb{C}$, and $f: G \to \mathbb{C}$ an analytic function with $f(G) \subset G$.
Let $f^n$ denote the $n$th iterate of $f$.
Suppose that $a \in G$ is a fixed point of $f$ (i.e.\ $f(a) = a$) and $|f'(a)| < 1$.
Define the basin of attraction of $z = a$ to be the set $$\Omega := \{z \in G : \lim_{n \to \infty} f^n(z) = a\}.$$

(a) Show that there is a $\delta > 0$ such that $\{z : |z - a| < \delta\} \subset \Omega$.

(b) Show, using part (a), that in fact $\Omega = G$.
:::
