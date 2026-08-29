---
schema: qual/card@1
id: FT-ITKJU
kind: theorem
title: Weierstrass Approximation Theorem
prompts:
- State the Weierstrass approximation theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - Polynomials
relations: []
review: draft
---

::: {.theorem}
If $f: I\to \RR$ is continuous, then for every $\varepsilon$ there exists a polynomial $p_\varepsilon(x)$ such that $\norm{f - p_\varepsilon}_\infty < \varepsilon$.

> Slogan: polynomials are dense in $C([0, 1], \norm{\wait}_\infty)$.
:::
