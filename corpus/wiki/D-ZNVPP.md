---
schema: qual/card@1
id: D-ZNVPP
kind: definition
title: Connected space
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

:::{.definition}
A space $X$ is **connected** iff there does not exist a disconnection $X = A\disjoint B$ with $A, B$ nonempty open sets.
I.e. $X$ can not be written as the disjoint union of two proper nonempty open sets.
Equivalently, $X$ contains no proper nonempty clopen sets.

Note that there is an additional condition for a subspace $Y\subset X$ to be connected:
\[
\cl_{Y}(A) \intersect B = A \intersect \cl_{Y}(B) = \emptyset
.\]
:::
