---
schema: qual/card@1
id: P-RAF18D
kind: problem
title: "Integral of |f(x) - f(y)| over a thin diagonal strip"
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
Let $f \in L^1([0,1], m)$, $m^2$ be Lebesgue measure on $\mathbb{R}^2$, and
$$
A_\varepsilon = \{(x,y) \in [0,1] \times [0,1] : |x - y| \leq \varepsilon\} \quad \text{for all } \varepsilon > 0.
$$
Prove that

1) $\displaystyle\int_{A_\varepsilon} |f(x) - f(y)|\,dm^2(x,y) \leq 4\varepsilon \cdot \|f\|_{L^1([0,1], m)}$ and

2) $\displaystyle\lim_{\varepsilon \downarrow 0} \varepsilon^{-1} \int_{A_\varepsilon} |f(x) - f(y)|\,dm^2(x,y) = 0.$
:::
