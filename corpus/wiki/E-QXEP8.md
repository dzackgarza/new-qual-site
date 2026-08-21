---
schema: qual/card@1
id: E-QXEP8
kind: exercise
title: Lens spaces
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §81.5"}


Consider $S^3$ as the space of all pairs of complex numbers $(z_1, z_2)$ satisfying the equation $\abs{z_1}^2 + \abs{z_2}^2 = 1$. Given relatively prime positive integers $n$ and $k$, define $h: S^3 \to S^3$ by the equation

$$
h(z_1, z_2) = (z_1 e^{2\pi i/n}, z_2 e^{2\pi i k/n}).
$$

(a) Show that $h$ generates a subgroup $G$ of the homeomorphism group of $S^3$ that is cyclic of order $n$, and that only the identity element of $G$ has a fixed point. The orbit space $S^3/G$ is called the lens space $L(n, k)$.

(b) Show that if $L(n, k)$ and $L(n', k')$ are homeomorphic, then $n = n'$. [It is a theorem that $L(n, k)$ and $L(n', k')$ are homeomorphic if and only if $n = n'$ and either $k \equiv k' \pmod{n}$ or $kk' \equiv 1 \pmod{n}$. The proof is decidedly nontrivial.]

(c) Show that $L(n, k)$ is a compact 3-manifold.
:::
