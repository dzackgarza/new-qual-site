---
schema: qual/card@1
id: P-RAF18F
kind: problem
title: "A bounded linear functional on L^infinity not arising from L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Consider the Banach space $L^\infty([0,1], m)$ and its vector subspace
$$
V = \{f \in L^\infty([0,1], m) : \text{the limit } \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm \text{ exists}\}.
$$

1. Prove that there exists $\varphi \in L^\infty([0,1], m)^*$ such that $\varphi(f) = \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm$ for every $f \in V$.

2. Let $\varphi \in L^\infty([0,1], m)^*$ such that $\varphi(f) = \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm$ for every $f \in V$.
   Prove that there does not exist $g \in L^1([0,1], m)$ such that $\varphi(f) = \int fg\,dm$ for every $f \in L^\infty([0,1], m)$.
:::
