---
schema: qual/card@1
id: P-CAF08C
kind: problem
title: "Pointwise limit of analytic functions with uniformly bounded derivatives is analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be open and connected, and let $h \in H(G)$.
Suppose that $\{f_n(z)\} \subset H(G)$ is a sequence of analytic functions for which $\lim_{n \to \infty} f_n(z)$ exists (and is finite) for every $z \in G$.
Put $f(z) := \lim_{n \to \infty} f_n(z)$.
Suppose that $|f_n'(z)| \leq |h(z)|$ for all $z \in G$.
Prove that $f \in H(G)$.
:::
