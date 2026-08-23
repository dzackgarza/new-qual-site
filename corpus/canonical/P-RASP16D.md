---
schema: qual/card@1
id: P-RASP16D
kind: problem
title: "Convergence of Riemann-Stieltjes sums and the norm of Riemann-Stieltjes functionals"
classification:
  areas:
  - real-analysis
  topics:
  - Riemann-Stieltjes Integration
  - Uniform Boundedness Principle
  - Riesz Representation
relations: []
review: draft
solved: false
---

::: problem
Let $0 = x_0^{(k)} < x_1^{(k)} < \cdots < x_k^{(k)} = 1$ ($k = 1, 2, \ldots$) and $0 \neq A_j^{(k)} \in \mathbb{R}$ ($j = 0, \ldots, k$, $k = 1, 2, \ldots$). Define for any $f \in C([0, 1])$
$$
I[f] = \int_0^1 f(x) \, dx \quad \text{and} \quad I_k[f] = \sum_{j=0}^{k} A_j^{(k)} f(x_j^{(k)}) \quad (k = 1, 2, \ldots).
$$

(1) Assume $\sup_{k \geq 1} \sum_{j=0}^{k} |A_j^{(k)}| < \infty$ and $\lim_{k \to \infty} I_k[p] = I[p]$ for any polynomial $p$. Prove $\lim_{k \to \infty} I_k[f] = I[f]$ for $f \in C([0, 1])$.

(2) (a) For any $k > 1$, $I_k$ is a linear functional on the Banach space $C([0, 1])$ with the uniform norm. Prove that $\|I_k\| = \sum_{j=0}^{k} |A_j^{(k)}|$.

(b) Assume $\lim_{k \to \infty} I_k[f] = I[f]$ for any $f \in C([0, 1])$. Prove $\sup_{k \geq 1} \sum_{j=0}^{k} |A_j^{(k)}| < \infty$.
:::