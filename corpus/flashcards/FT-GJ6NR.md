---
schema: qual/card@1
id: FT-GJ6NR
kind: theorem
title: 'Fundamental Theorem of Galois Theory'
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - normal-subgroups
relations: []
review: draft
---

::: {.theorem title="Fundamental Theorem of Galois Theory"}
Let $K/F$ and $G = \mathrm{Gal}(K/F)$, then there is an inclusion-reversing bijection
$$\begin{align*}
\{E \suchthat K/E/F\} \quad&\iff\quad \{H \suchthat 1\leq H \leq G\} \\
E &\mapsto \{\tau\in G \suchthat \tau\mid_E = \mathrm{id}\} \\
H &\mapsto \text{Fixed field of } H
\end{align*}$$
such that

1. Inclusion reversing: $E_1 \subseteq E_2 \iff H_2 \leq H_1$.
2. $\abs{H} = [K: E]$ and $[E:F] = [G: H]$.
3. $K/E$ is always Galois with $G(K/E) = H$.
4. $E/F$ is Galois $\iff$ $H\normal G$, in which case $G(E/F) \cong G/H$.
5. Compositum correspondences:
  - $E_1\intersect E_2$ corresponds to $\gens{H_1, H_2}$.
  - $E_1 E_2$ corresponds to $H_1\intersect H_2$.
:::
