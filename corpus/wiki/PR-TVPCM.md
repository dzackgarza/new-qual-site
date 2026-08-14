---
schema: qual/card@1
id: PR-TVPCM
kind: proposition
title: "Holomorphic iff delbar vanishes"
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-riemann
  - holomorphic-functions
relations: []
review: draft
---
:::{.proposition title="Holomorphic iff delbar vanishes"}
$f$ is holomorphic at $z_0$ iff $\delbar f(z_0) = 0$:
\[
2\delbar f
&\da (\del_x + i \del_y) (u+iv) \\
&= u_x + iv_x + iu_y - v_y \\
&= (u_x - v_y) + i(u_y + v_x) \\
&= 0 && \text{by Cauchy-Riemann}
.\]
:::
