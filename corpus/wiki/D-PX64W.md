---
schema: qual/card@1
id: D-PX64W
kind: definition
title: "Centralizer: The centralizer of an element is defined as $Z(h) \\da C_G(h) \\da \\ts{ g\\in G \\st ghg\\inv = h }$ the elements of\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.definition title="Centralizer"}
The **centralizer of an element** is defined as 
\[
Z(h) \da C_G(h) \da \ts{ g\in G \st ghg\inv = h } 
,\]
the elements of $G$ the stabilize $h$ under conjugation.

The **centralizer of a subset** $H$ is defined as
\[
Z(H) \da C_G(H) \da \Intersect_{h\in H} C_G(h) \da \theset{g\in G \suchthat ghg\inv = h ~\forall h\in H}
,\]
the elements of $G$ that simultaneously stabilize all of $H$ pointwise under conjugation.
:::
