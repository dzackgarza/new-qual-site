---
schema: qual/card@1
id: P-PRACT20-W3-19
kind: problem
title: Volume between the paraboloids $z=6-x^2-2y^2$ and $z=-2+x^2+2y^2$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Multiple Integrals
relations: []
review: draft
---

::: {.problem}
Set up an area integral (i.e. an integral in $xy$-space) which represents the volume of the solid bounded above by the graph of $z = 6 - x^{2} - 2y^{2}$ and below by the graph of $z = -2 + x^{2} + 2y^{2}$.
:::

::: {.solution}
The two graphs meet where $6-x^2-2y^2=-2+x^2+2y^2$, that is, over the ellipse $x^2+2y^2=4$, and inside it the upper graph lies above the lower one. The height of the solid is $(6-x^2-2y^2)-(-2+x^2+2y^2)=8-2x^2-4y^2$. Thus the volume is

$$
\int_{-2}^{2}\int_{-\sqrt{(4-x^2)/2}}^{\sqrt{(4-x^2)/2}}(8-2x^2-4y^2)\,dy\,dx.
$$
:::
