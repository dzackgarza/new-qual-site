---
schema: qual/card@1
id: D-GY7ZN
kind: definition
title: "Special Orthogonal Group"
classification:
  areas:
  - algebra
  topics:
  - matrix-groups
relations: []
review: draft
---
:::{.definition title="Special Orthogonal Group"}
\[
\SO_n(\RR) = \ts{ A \st  AA^t = I \text{ and } \det A = 1} = \Orth_n(\RR) \intersect \SL_n(\RR)
.\]

Both conditions are needed.
The single equation $AA^t = I$ cuts out the full orthogonal group $\Orth_n(\RR)$, whose elements have $\det A = \pm 1$, so it is too big by an index of two.
And $\ker\qty{\GL_n(\RR) \mapsvia{\det} \RR\units} = \SL_n(\RR)$, which is too big in the other direction: it imposes no orthogonality.

:::
