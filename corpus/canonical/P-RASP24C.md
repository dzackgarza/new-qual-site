---
schema: qual/card@1
id: P-RASP24C
kind: problem
title: "Hölder space is a Banach space with compact unit ball"
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
Let $0 < \alpha \leq 1$ and let $\Lambda_\alpha([0,1])$ denote the space of Hölder continuous functions of exponent $\alpha$ on $[0,1]$. Specifically, $\Lambda_\alpha([0,1]) = \{f \in C([0,1]) : \|f\|_{\Lambda_\alpha} < \infty\}$ where
$$
\|f\|_{\Lambda_\alpha} = |f(0)| + \sup_{x \neq y \in [0,1]} \frac{|f(x) - f(y)|}{|x - y|^\alpha}.
$$

(a) Show that $\|\cdot\|_{\Lambda_\alpha}$ is a norm on $\Lambda_\alpha([0,1])$ and that with this norm $\Lambda_\alpha([0,1])$ is a Banach space.

(b) Let $B = \{f \in \Lambda_\alpha([0,1]) : \|f\|_{\Lambda_\alpha} \leq 1\}$ be the closed unit ball. Show that $B$ is compact with respect to the uniform norm.
:::
