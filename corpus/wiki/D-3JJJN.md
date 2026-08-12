---
schema: qual/card@1
id: D-3JJJN
kind: definition
title: "Split Exact Sequences"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.definition title="Split Exact Sequences"}
A short exact sequence 
\[
\xi: 0 \to A \mapsvia{d_1} B \mapsvia{d_2} C \to 0
\]
has a **right-splitting** iff there exists a map $s: C\to B$ such that $d_2 \circ s = \id_{C}$.
$\xi$ has a **left-splitting** iff there exists a map $t:B\to A$ such that $t \circ d_1 = \id_A$.
:::
