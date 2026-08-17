---
schema: qual/card@1
id: E-AHBVF
kind: exercise
title: "Cosine expansion in $z\\inv$"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - trigonometry
relations: []
review: draft
solved: true
---
:::{.exercise title="Cosine expansion in $z\inv$"}
Expand $f(z) = z^2\cos\qty{z\over 3}$ about $z=0$.
:::

:::{.solution}
\[
f(z) = z^2\qty{ 1 + {1\over 2!}\qty{1\over 3z}^2 + {1\over 4!}\qty{1\over 3z}^4 } = z^2 + {1\over 2! \cdot 3^2} + {1\over 4! \cdot 3^4}z^{-2} + \cdots
.\]
:::

