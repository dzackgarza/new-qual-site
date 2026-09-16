---
schema: qual/card@1
id: FT-ITKJU
kind: theorem
title: Weierstrass approximation theorem
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
Let $I=[a,b]\subseteq\RR$ be a compact interval and let $f\colon I\to \RR$ be continuous.
For every $\varepsilon>0$ there exists a polynomial $p_\varepsilon$ with real coefficients such that
$$
\norm{f - p_\varepsilon}_\infty \coloneqq \sup_{x\in I}\abs{f(x)-p_\varepsilon(x)} < \varepsilon.
$$
Equivalently, the polynomials are [[D-KJBAK|dense]] in $C([a,b])$ with the norm $\norm{\cdot}_\infty$.
:::
