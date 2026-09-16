---
schema: qual/card@1
id: PR-GSDKO
kind: proposition
title: Orbit-stabilizer bijection for a transitive action
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.proposition}
Let a group $G$ [[D-WYC7C|act]] transitively on a set $X$, and let $x \in X$ with stabilizer $G_x$.
Then
$$
\begin{aligned}
\Phi\colon G/G_{x} &\to X \\
gG_{x} &\mapsto g \cdot x
\end{aligned}
$$
is a well-defined bijection from the set of left cosets of $G_x$ to $X$, and $\Phi(h \cdot gG_x) = h \cdot \Phi(gG_x)$ for all $g, h \in G$.
:::
