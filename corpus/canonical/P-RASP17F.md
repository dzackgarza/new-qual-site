---
schema: qual/card@1
id: P-RASP17F
kind: problem
title: "Approximate identities, mollified indicators, and weak derivatives imply absolute continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Approximate Identity
  - Weak Derivatives
  - Absolute Continuity
relations: []
review: draft
solved: false
---

::: problem
Let $\varphi \in C_c^\infty(\mathbb{R}, [0, \infty))$ satisfy $\int_\mathbb{R} \varphi \, dm = 1$ and for $\varepsilon > 0$ let $\delta_\varepsilon(x) = \frac{1}{\varepsilon}\varphi\left(\frac{x}{\varepsilon}\right)$.

1. If $-\infty < a < b < \infty$ and $h_\varepsilon(x) := \mathbf{1}_{[a,b]} * \delta_\varepsilon$, show $h_\varepsilon'(x) = \delta_\varepsilon(x - a) - \delta_\varepsilon(x - b)$.

2. If $f \in C_c(\mathbb{R}, \mathbb{R})$ and $g \in L^1(\mathbb{R}, m)$ satisfy
$$
\int_\mathbb{R} f h' \, dm = -\int_\mathbb{R} g h \, dm \quad \text{for all } h \in C_c^\infty(\mathbb{R}),
$$
show $f$ is absolutely continuous and $f' = g$ $m$-a.e.
:::
