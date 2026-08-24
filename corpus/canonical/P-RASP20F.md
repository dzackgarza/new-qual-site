---
schema: qual/card@1
id: P-RASP20F
kind: problem
title: "Hausdorff moment problem characterization via polynomial inequalities"
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
Let $\{c_n\} \in \mathbb{R}$ ($n = 0, 1, 2, \ldots$). Prove that the following two conditions (1) and (2) are equivalent:

(1) There exists a signed Radon measure $\mu$ on $[0,1]$ such that
$$
\int_{[0,1]} t^n\,d\mu(t) = c_n \qquad (n = 0, 1, \ldots);
$$

(2) There exists $M \geq 0$ such that for any $N \in \mathbb{N}$ and any $a_n \in \mathbb{R}$ ($n = 0, \ldots, N$),
$$
\left|\sum_{n=0}^{N} a_n c_n\right| \leq M \max_{0 \leq t \leq 1} \left|\sum_{n=0}^{N} a_n t^n\right|.
$$
:::
