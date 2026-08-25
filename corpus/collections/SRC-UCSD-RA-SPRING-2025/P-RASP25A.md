---
schema: qual/card@1
id: P-RASP25A
kind: problem
title: "L^2 membership characterized by integral inequality with absolutely continuous function"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $f \in L^1([0,1])$.
Prove that the following are equivalent:

(1) $f \in L^2([0,1])$.

(2) There exists $g$ absolutely continuous on $[0,1]$ such that for every $x, y \in [0,1]$ it holds
$$
\left|\int_x^y f(t)\,dt\right|^2 \leq (g(y) - g(x))(y - x).
$$
:::
