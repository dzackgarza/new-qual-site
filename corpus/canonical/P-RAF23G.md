---
schema: qual/card@1
id: P-RAF23G
kind: problem
title: "Ratio of L^n norms converges to L^infinity norm"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $(X, \mu)$ be a nonempty measurable space with $\mu(X) < \infty$, $f \in L^\infty(\mu)$ and $\|f\|_\infty > 0$.
Define $\alpha_n := \int_X |f|^n$ for $n = 1, 2, 3, \ldots$.
Prove that
$$
\lim_{n \to \infty} \frac{\alpha_{n+1}}{\alpha_n} = \|f\|_\infty.
$$
:::
