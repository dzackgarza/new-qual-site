---
schema: qual/card@1
id: FF-TBIC5
kind: fact
title: $\sin\theta$ and $d\theta$ under the substitution $z=e^{i\theta}$
prompts:
- How is $\sin(\theta)$ written in $z$ for a contour integral on the unit circle, and what is $d\theta$?
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Contour Integration
  - Residues
relations: []
review: draft
---

::: {.fact}
For $\theta\in\RR$ and $z=e^{i\theta}$ on the unit circle,
$$
\begin{aligned}
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i}, \\
d\theta &= \frac{dz}{iz}.
\end{aligned}
$$
:::
