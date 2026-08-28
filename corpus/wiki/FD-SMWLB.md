---
schema: qual/card@1
id: FD-SMWLB
kind: definition
title: Nowhere Dense
prompts:
- What does it mean for a set to be nowhere dense?
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Closure
relations: []
review: draft
---

::: {.definition}
A set is $A$ **nowhere dense** if its closure has empty interior $\qty{\bar A}^\circ$, equivalently it is not dense in *any* nonempty open set.
For $\RR$, every interval $I$ contains a subinterval $S\subset I$ with $S\intersect A = \emptyset$, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
:::
