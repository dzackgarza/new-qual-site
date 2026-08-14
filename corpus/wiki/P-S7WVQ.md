---
schema: qual/card@1
id: P-S7WVQ
kind: problem
title: "Show that $S^2 \\cross \\RP^4 \\not\\homotopic S^4 \\cross \\RP^2$."
classification:
  areas:
  - topology
  topics:
  - cohomology
  - homotopy
  - product-topology
relations: []
review: draft
---
:::{.problem title="?"}
Show that $S^2 \cross \RP^4 \not\homotopic S^4 \cross \RP^2$.
:::

:::{.solution}
Take coefficients in $\FF_2$, apply Kunneth to get
\[
H^*(X_1; \FF_2) = \Extalgebra_{\FF_2}{x_2} \tensor_{\FF_2} {\FF_2\adjoin{y_1} \over \gens{ y_1^5 }} \\
H^*(X_2; \FF_2) = \Extalgebra_{\FF_2}{w_4} \tensor_{\FF_2} {\FF_2\adjoin{z_1} \over \gens{ z_1^3 }}
.\]

Now use that any homotopy equivalence induces a graded ring isomorphism $f$, where $f(y_1) = z_1$ in $H^1$, but these have different orders.

:::
