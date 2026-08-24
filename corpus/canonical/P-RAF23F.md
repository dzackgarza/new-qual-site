---
schema: qual/card@1
id: P-RAF23F
kind: problem
title: "L^p characterization via distribution function and interpolation of weak-type bounds"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
(i) Prove that for $p \geq 1$, $f \in L^p$ if and only if $\sum_{-\infty}^{+\infty} \beta^{kp} \lambda_f(\beta^k) < \infty$ for all $\beta > 1$.
Here $\lambda_f(\alpha) = \mu(\{x : |f|(x) > \alpha\})$.

(ii) Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 < q_1 < q_2$ such that $\lambda_{Tf}(2^k) \leq (C_1 \|f\|_p / 2^k)^{q_1}$ for integers $k \leq 0$; and $\lambda_{Tf}(2^\ell) \leq (C_2 \|f\|_p / 2^\ell)^{q_2}$ for integers $\ell \geq 0$.
Prove that for any $q_1 < q < q_2$, $\|Tf\|_q \leq C_q \|f\|_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::
