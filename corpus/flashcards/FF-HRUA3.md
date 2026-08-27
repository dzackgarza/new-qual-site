---
schema: qual/card@1
id: FF-HRUA3
kind: fact
title: What does it mean for a set to be nowhere dense?
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Closure
relations: []
review: draft
---

::: {.fact}
A set is $ A $ **nowhere dense** if its closure has empty interior $ \qty{\overline{A}}^\circ $, equivalently it is not dense in *any* nonempty open set.

For $ {\mathbf{R}} $, every interval $ I $ contains a subinterval $ S\subset I $ with $ S\cap A = \emptyset $, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.
:::
