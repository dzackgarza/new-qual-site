---
schema: qual/card@1
id: P-SLWIE
kind: problem
title: "Show that $\\pi^2/\\sin^2(\\pi z)$ and $\\sum_{n\\in\\ZZ}(z-n)^{-2}$ agree, by comparing their singularities and singular parts"
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
  - poles
  - principal-parts
  - identity-theorem
  - trigonometry
relations: []
review: draft
---
Define
\[
f(z) &= {\pi^2 \over \sin^2 \qty{\pi z} } \\
g(z) &= \sum_{n\in \ZZ} {1\over (z-n)^2}
.\]

a. Show that $f$ and $g$ have the same singularities in $\CC$.
b. Show that $f$ and $g$ have the same singular parts at each of their singularities.
c. Show that $f, g$ each have period one and approach zero uniformly on $0\leq x \leq 1$ as $\abs{y}\to \infty$.
d. Conclude that $f = g$.

:::{.solution}
\hfill
:::{.concept}
\hfill
Idea: show their $f-g$ is analytic by taking away all of the negative powers, and bounded by (c).
:::

:::

