---
schema: qual/card@1
id: E-WNTXK
kind: exercise
title: "Suppose $f$ is entire and $f(\\CC) \\subseteq \\HH$."
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose $f$ is entire and $f(\CC) \subseteq \HH$.
Show that $f$ must be constant.
:::

::: {.solution}
Write $T:\CC \to \DD$ for the Cayley map, then $F\da f\circ T$ satisfies $F(\CC) = T(f(\CC)) \subseteq  T(\HH) = \DD$, so $F$ is a bounded entire function and thus constant.
So $c = F(z) = T(f(z)) \implies f(z) = T\inv(c)$, making $f$ constant.
:::
