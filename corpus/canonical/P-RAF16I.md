---
schema: qual/card@1
id: P-RAF16I
kind: problem
title: "Ratio of L^k norms converges to L^infinity norm"
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
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$. Let $f \in L^\infty(\mu)$ with $\|f\|_\infty > 0$. Define
$$
\alpha_k = \int_X |f|^k\,d\mu \qquad \text{for } k = 1, 2, \ldots.
$$
Prove that
$$
\lim_{k \to \infty} \frac{\alpha_{k+1}}{\alpha_k} = \|f\|_\infty.
$$
:::
