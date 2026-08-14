---
schema: qual/card@1
id: D-IGUUS
kind: definition
title: "Wedge Product"
classification:
  areas:
  - topology
  topics:
  - cell-complexes
  - homology
  - quotient-spaces
relations: []
review: draft
---

::: {.definition title="Wedge Product"}
The wedge sum: for based spaces, $X \wedgeprod Y$ is the quotient of $X\disjoint Y$ obtained by identifying $x_0$ with $y_0$, and more generally $\bigvee_\alpha X_\alpha$ collapses one chosen basepoint in each summand to a single point.
For a CW complex, $X^n/X^{n-1} \cong \bigvee_\alpha S^n_\alpha$ with one sphere per $n\dash$cell, and reduced homology takes wedges to direct sums, $\tilde H_n\qty{\bigvee_\alpha X_\alpha}\cong \bigoplus_\alpha \tilde H_n(X_\alpha)$ for well-based $X_\alpha$.
:::

::: {.concept}
See Hatcher, pp. 10 and 126.
:::
