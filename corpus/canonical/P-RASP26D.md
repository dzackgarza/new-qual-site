---
schema: qual/card@1
id: P-RASP26D
kind: problem
title: "Relative weak* openness of a set of probability measures"
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
Let $\mathcal{M}([0,1])$ denote the space of all complex Radon measures on $[0,1]$, and $\mathcal{P}([0,1])$ the subset of probability measures. Let $f : [0,1] \times [0,1] \to \mathbb{R}$ be a continuous function, and let $U$ be the set of all $\mu \in \mathcal{P}([0,1])$ satisfying
$$
\forall y \in [0,1] \qquad \left|\int_0^1 f(x, y)\,d\mu(x)\right| < 1.
$$
Prove that $U$ is a relatively open subset of $\mathcal{P}([0,1])$ with respect to the weak* topology.
:::
