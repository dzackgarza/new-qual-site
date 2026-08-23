---
schema: qual/card@1
id: P-RAF16B
kind: problem
title: "Limits involving sin^k x, convergence in measure, and distributional derivatives"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
(1) Let $f \in C(\mathbb{R})$ with $f(0) = 1$.
Calculate with justification the limit $\lim_{k \to \infty} \int_0^\pi f(\sin^k x)\,dx$.

(2) Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Assume that $f$ and $f_k$ ($k = 1, 2, \ldots$) are all real-valued, $\mu$-measurable functions on $X$, and $f_k \to f$ in measure.
Let $F \in C(\mathbb{R})$ be uniformly continuous.
Prove that $F(f_k) \to F(f)$ in measure.

(3) Let $m$ denote the Lebesgue measure on $\mathbb{R}^n$.
Assume $g_k \to g$ weakly in $L^1(m)$.
Prove that $\partial^\alpha g_k \to \partial^\alpha g$ in $\mathcal{D}'(\mathbb{R}^n)$ for any multi-index $\alpha$.
:::
