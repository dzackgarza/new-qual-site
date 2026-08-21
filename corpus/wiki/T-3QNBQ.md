---
schema: qual/card@1
id: T-3QNBQ
kind: theorem
title: Weierstrass Approximation
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

::: {.theorem title="Weierstrass Approximation"}
If $[a, b] \subset \RR$ is a closed interval and $f$ is continuous, then for every $\eps> 0$ there exists a polynomial $p_\eps$ such that $\norm{f- p_\eps}_{L^\infty([a, b])} \converges{\eps \to 0}\to 0$.

Equivalently, polynomials are dense in the Banach space $C([0, 1], \norm{\wait}_\infty)$.
:::
