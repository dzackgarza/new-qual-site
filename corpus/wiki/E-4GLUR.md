---
schema: qual/card@1
id: E-4GLUR
kind: exercise
title: Singularities of of $\sin(z)/z$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Laurent Series
  - Trigonometry
  - Singularities
relations: []
review: draft
---

:::{.exercise}
Show that $\sin(z)/z$ has no poles.

:::

:::{.solution}
Heuristic: $\sin(z)$ has a zero of order 1, so the $z$ in the denominator exactly cancels it.
Explicitly, this is evident from the Laurent expansion about zero:
\[
z\inv \sin(z) = z\inv\qty{ z - {z^3 \over 3!} + {z^5\over 5!} - \cdots} = 1 - {z^2\over 3!} + {z^4 \over 5!} - \cdots
,\]
which has no factors of $z^{-k}$.
So $z=0$ is a removable singularity.
:::
