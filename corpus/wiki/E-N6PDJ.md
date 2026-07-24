---
schema: qual/card@1
id: E-N6PDJ
kind: exercise
title: "Nonconstant entire functions have dense image"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Nonconstant entire functions have dense image"}
Show that if $f:\CC\to \CC$ is nonconstant and entire then $f(\CC)$ is dense in $\CC$.

:::

:::{.solution}
Supposing not, then there is some $\DD_R(w) \intersect f(\CC)$ empty.
Then $g(z) \da {1\over f(z) - w}$ is bounded in this disc and reflects to an entire bounded function, thus constant.
Then if $g$ is constant, $f$ is constant.
:::

