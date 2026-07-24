---
schema: qual/card@1
id: S-JSWSW
kind: solution
title: Solution to P-4QQGN
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-4QQGN
review: draft
---

:::{.solution}
$f'(x) = \lim_{n\to\infty} n(f(x+1/n) - f(x))$ if the limit exists. Then Module a null set, $f'$ is measurable. Thus, it is measurable.

For the second part, By the similar argument, We know that $D^+f$, $D^-f$, $D_+f$ and $D_-f$ are measurable. Then $\{x : f'(x) \text{ exsits}\} = \{x : D^+f(x) = D^-f(x) = D_+f(x) = D_-f(x)\}$ is measurable.
:::
