---
schema: qual/card@1
id: P-RAF22G
kind: problem
title: "A distribution supported at the origin is a finite linear combination of derivatives of delta"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
  - Dirac Delta
  - Support of Distributions
relations: []
review: draft
---

::: problem
Let $F$ be a distribution on $\mathbb{R}^n$ such that the support of $F$, $\operatorname{supp}(F) = \{0\}$.
Let $\alpha = (\alpha_1, \cdots, \alpha_n)$ with $\alpha_i$ nonnegative integers, and $\delta$ be the delta distribution centered at $0$.

1. Prove that there exists a natural number $N$ and $C > 0$ such that
$$
|\langle F, \varphi \rangle| \leq C \sum_{|\alpha| \leq N} \sup_x |\partial^\alpha \varphi(x)|, \quad \forall \varphi \in C_c^\infty.
$$

2. If $\varphi \in C_c^\infty$ and $\partial^\alpha \varphi(0) = 0$ for all $|\alpha| \leq N$, then $\langle F, \varphi \rangle = 0$.

3. There exist constants $c_\alpha$ ($|\alpha| \leq N$) such that $F = \sum_{|\alpha| \leq N} c_\alpha \partial^\alpha \delta$.
:::
