---
schema: qual/card@1
id: E-CHCXA
kind: exercise
title: "Zero derivative implies constant"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Zero derivative implies constant"}
Show that if $f' = 0$ on a domain $\Omega$, then $f$ is constant on $\Omega$

#complex/exercise/completed

:::

:::{.solution}
Write $f = u + iv$, then $0 = 2 f' = u_x + iv_x = u_y - iu_y$, so $\grad u = \grad v = 0$.
Show $f$ is constant along every straight line segment $L$ by computing the directional derivative $\grad u \cdot \vector v = 0$ along $L$ connecting $p, q$.
Then $u(p) = u(q) = a$ some constant, and $v(p) = v(q) = b$, so $f(z) = a+bi$ everywhere.
:::
