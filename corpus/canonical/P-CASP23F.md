---
schema: qual/card@1
id: P-CASP23F
kind: problem
title: "Green's function on D\\{a} and failure of the Dirichlet problem"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Dirichlet Problem
  - Green's Function
  - Boundary Values
relations: []
review: draft
---

::: problem
Let $a \in \mathbb{D}$ and $G = \mathbb{D} \setminus \{a\}$.

(a) Construct a harmonic function $v$ on $G$ such that the following two conditions are satisfied: $\lim_{z \to z^*} v(z) = 0$ for all $z^* \in \mathbb{T}$ and $\lim_{z \to a} v(z) = +\infty$.
Write down an explicit formula for the function $v$ you constructed.

(b) Let $f \in C(\partial G)$ be defined as $f(z) = 0$ for $z \in \mathbb{T}$ and $f(a) = 2$.
Prove that the Dirichlet problem on $G$ with boundary data $f$ has no solution: there is no harmonic function $u$ on $G$ such that $\lim_{z \to z_0} u(z) = f(z_0)$ for all $z_0 \in \partial G$.
:::
