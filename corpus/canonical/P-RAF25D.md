---
schema: qual/card@1
id: P-RAF25D
kind: problem
title: "Orthogonal projection onto the mean-zero subspace of L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Orthogonal Projection
  - L2 Spaces
relations: []
review: draft
solved: false
---

::: problem
Let $\Omega$ be a bounded, Lebesgue measurable subset of $\mathbb{R}^n$ such that $L^n(\Omega) > 0$, where $L^n$ is the Lebesgue measure on $\mathbb{R}^n$. Let
$$
C := \left\{f \in L^2(\Omega) : \int_\Omega f(x) \, dx = 0\right\}.
$$

(1) Prove that $C$ is a closed subspace of $L^2(\Omega)$.

(2) Prove that for every $g \in L^2(\Omega)$ we have
$$
P_C(g) = g - \frac{1}{L^n(\Omega)} \int_\Omega g(x) \, dx,
$$
where $P_C(g)$ denotes the orthogonal projection of $g$ onto $C$.

(3) Prove that $C^\perp = \{g \in L^2(\Omega) : g = c \text{ a.e. in } \Omega \text{ for some } c \in \mathbb{C}\}$.
:::