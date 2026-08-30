---
schema: qual/card@1
id: FD-C7EQD
kind: definition
title: 'Definition: A pole $a$ of order $m$'
prompts:
- What does it mean for $f$ to have a pole of order $m$ at $a$?
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Singularities
relations: []
review: draft
---

::: {.definition}
The smallest $m$ such that 
$$
\lim_{z\to a}(z-a)^{m+1}f(z) < \infty \text{ but } \lim_{z\to a}(z-a)^{k} f(z) = \infty \text{ for } k < m
.$$
:::
