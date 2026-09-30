---
schema: qual/card@1
id: E-4EZMD
kind: problem
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
Define $A \definedas \theset{\Re(z) > 0, \Im(z) > 0}$.
Find a conformal equivalence $\Delta \intersect A \to A$.
:::

::: {.solution}
The composite of the following three maps is a conformal equivalence $\Delta\intersect A\to A$.

- The squaring map $z\mapsto z^2$ sends $\Delta\intersect A$ onto $\DD \intersect \HH$.

- The negated Joukowski map $z\mapsto -{1\over 2}(z+\inverseof{z})$ sends $\DD\intersect\HH$ onto $\HH$.

- The principal branch of $z\mapsto z^{1\over 2}$ sends $\HH$ onto the first quadrant $A$.
:::
