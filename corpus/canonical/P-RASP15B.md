---
schema: qual/card@1
id: P-RASP15B
kind: problem
title: "L^p characterization via distribution function"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space.
Prove that for any $0 < p < \infty$, $f \in L^p$ if and only if
$$
\sum_{k=-\infty}^{\infty} 2^{kp} \lambda_f(2^k) < \infty
$$
where $\lambda_f(\alpha) = \mu(\{x : |f|(x) > \alpha\})$.
:::
