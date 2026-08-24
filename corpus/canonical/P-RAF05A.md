---
schema: qual/card@1
id: P-RAF05A
kind: problem
title: "Three applications of major theorems: monotone convergence, Stone-Weierstrass, Baire category"
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Stone-Weierstrass Theorem
  - Baire Category Theorem
  - L1 Spaces
relations: []
review: draft
solved: false
---

::: problem
Prove the following.
Each follows in a straightforward way by applying theorems.
Be sure to name each theorem when you use it.

(a) Let $\{f_j\}$ be a sequence of real-valued functions in $L^1(\mu)$ such that $f_1 \geq f_2 \geq \cdots \geq 0$.
Then $\lim_j \int f_j \, d\mu = \int \lim_j f_j \, d\mu$.

(b) Let $f : [a, b] \times [c, d] \to \mathbb{R}$ be continuous.
Then for all $\varepsilon > 0$ there exists $N > 0$ and continuous functions $g_j, h_j : [a, b] \to \mathbb{R}$ such that $\left|f(x, y) - \sum_j g_j(x) h_j(y)\right| < \varepsilon$ for all $(x, y) \in [a, b] \times [c, d]$.

(c) Let $C([0, 1], \mathbb{R})$ be the space of all real-valued functions on $[0, 1]$ with the uniform norm topology.
Suppose that $C([0, 1], \mathbb{R}) = \bigcup_j F_j$ where each $F_j$ is closed.
Then there exists $\varepsilon > 0$, $j_0 \in \mathbb{N}$, and $f_0 \in F_{j_0}$ such that $\sup_{x \in [0,1]} |f(x) - f_0(x)| < \varepsilon \implies f \in F_{j_0}$.
:::
