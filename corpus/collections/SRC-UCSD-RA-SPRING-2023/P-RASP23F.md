---
schema: qual/card@1
id: P-RASP23F
kind: problem
title: "Interpolation of weak-type bounds"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $1 \leq p < \infty$.
Recall that $\lambda_g(\alpha) = \mu(\{x : |g(x)| > \alpha\})$.
Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 \leq q_1 < q_2$ such that $\lambda_{Tf}(\alpha) \leq (C_1 \|f\|_p / \alpha)^{q_1}$ and $\lambda_{Tf}(\alpha) \leq (C_2 \|f\|_p / \alpha)^{q_2}$.
Prove that for any $q_1 < q < q_2$, $\|Tf\|_q \leq C_q \|f\|_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::
