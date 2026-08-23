---
schema: qual/card@1
id: P-RASP11B
kind: problem
title: "Dyadic averaging operators converge to the identity in L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Approximate Identity
  - Lebesgue Points
  - Maximal Function
relations: []
review: draft
solved: false
---

::: problem
For each integer $k > 0$ denote by $\Delta_k(j) = [j 2^{-k}, (j+1) 2^{-k})]$ where $j \in \mathbb{Z}$, the dyadic rational interval of length $2^{-k}$ starting at $j 2^{-k}$.
Let $f \in L^1(\mathbb{R})$, and define
$$
A_k(f)(x) = \sum_j a_k(j) \mathbf{1}_{\Delta_k(j)}(x), \quad a_k(j) = \frac{1}{|\Delta_k(j)|} \int_{\Delta_k(j)} f(y) \, dy.
$$

(a) Prove that $\|A_k f\|_{L^1(\mathbb{R})} \leq \|f\|_{L^1(\mathbb{R})}$ for all $k > 0$, $f \in L^1(\mathbb{R})$.

(b) Show that if $f \in L^1(\mathbb{R})$ then $A_k(f) \to f$ in $L^1(\mathbb{R})$ as $k \to \infty$.
:::
