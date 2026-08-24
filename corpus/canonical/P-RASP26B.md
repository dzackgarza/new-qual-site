---
schema: qual/card@1
id: P-RASP26B
kind: problem
title: "Metric on L^1 via antiderivatives and compactness via Arzela-Ascoli"
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
Consider the function
$$
d(f, g) := \sup_{0 \leq x \leq 1} \left|\int_0^x (f(t) - g(t))\,dt\right|, \qquad f, g \in L^1([0,1]).
$$
Let $C := \{f \in L^1([0,1]) : |f(t)| \leq 1 \text{ for a.e. } t \in [0,1]\}$.

(1) Prove that $d$ is a metric on $L^1([0,1])$.

(2) Prove that $C$ is compact in $(L^1([0,1]), d)$.

Hint: Let $\tilde{C} = \{F(x) := \int_0^x f : f \in C\}$ and use Arzelà-Ascoli.
:::
