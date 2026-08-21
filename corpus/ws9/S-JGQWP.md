---
schema: qual/card@1
id: S-JGQWP
kind: solution
title: Solution to P-C53SG
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations:
- kind: solves
  target: P-C53SG
review: draft
---

:::{.solution}
To apply the Fubini's thm, it suffices to show $\int_0^1\int_0^1|\frac{(x-y)\sin(xy)}{x^2+y^2}|dxdy<\infty$. We integrate this on the quarter of a disk of radius $\sqrt 2$ in the first quadrant, which contains $[0,1]\times[0,1]$. We see that $\int_0^{\pi/2}\int_0^{\sqrt2}|\frac{r\cos(\theta)-r\sin(\theta)}{r^2}|rdrd\theta\le 2\int_0^{\pi/2}\int_0^{\sqrt2}drd\theta=\sqrt2\pi$.
:::
