---
schema: qual/card@1
id: E-P2PEF
kind: exercise
title: Holomorphic iff delbar vanishes
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

:::{.exercise title="Holomorphic iff delbar vanishes"}
Show that $f$ is holomorphic iff $\delbar f = 0$.
:::

:::{.solution}
\[
2\delbar f 
&\da (\del_x + i \del_y) (u+iv) \\
&= u_x + iv_x + iu_y - v_y \\
&= (u_x - v_y) + i(u_y + v_x) \\
&= 0 && \text{by Cauchy-Riemann}
.\]
:::
