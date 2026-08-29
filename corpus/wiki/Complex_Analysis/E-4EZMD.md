---
schema: qual/card@1
id: E-4EZMD
kind: exercise
title: A conformal equivalence from the quarter-disc to the first quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
relations: []
review: draft
---

::: {.problem}
Define $A \da \ts{\Re(z) > 0, \Im(z) > 0}$.
Find a conformal equivalence $\Delta \intersect A \to A$.
:::

::: {.solution}
In steps:

- Unfold with $z\mapsto z^2$ to get $\DD \intersect \HH$.

- Joukowski it with $z\mapsto -{1\over 2}(z+z\inv)$ to get $\HH$.

- Fold with $z\mapsto z^{1\over 2}$ to get $Q_1 = A$.
:::
