---
schema: qual/card@1
id: E-ZXKDY
kind: exercise
title: "Show that if $f$ is not surjective then $\\deg f = 0$."
classification:
  areas:
  - topology
  topics:
  - degree
  - homology
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that if $f$ is not surjective then $\deg f = 0$.
:::

::: {.solution}
In this case $f$ factors as $S^n \mapsvia{f_1} S^n\smts{\pt}\mapsvia{f_2} S_n$.
But $S^n\smts{\pt} \homotopic \RR^n$, to $H_*(f_1) = 0$ and $\deg f_1 = 0$.
Then apply $\deg f = \qty{\deg f_1} \qty{\deg f_2}$.
:::
