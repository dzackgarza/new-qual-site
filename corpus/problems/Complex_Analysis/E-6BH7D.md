---
schema: qual/card@1
id: E-6BH7D
kind: problem
title: A conformal map from the upper half-disk onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from the upper half-disc to the upper half-plane.
:::

::: {.solution}

- The map $z\mapsto {1+z\over 1-z}$ sends $\DD$ onto the right half-plane $\theset{\Re w>0}$. Since $\Im{1+z\over 1-z}={2\Im z\over\abs{1-z}^2}$, it sends $\DD \intersect \HH$ onto the first quadrant $Q_1=\theset{\Re w>0,\ \Im w>0}$.

- The map $z\mapsto z^2$ sends $Q_1$ onto $\HH$.
:::
