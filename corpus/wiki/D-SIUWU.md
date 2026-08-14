---
schema: qual/card@1
id: D-SIUWU
kind: definition
title: "Short exact sequence"
classification:
  areas:
  - topology
  topics:
  - homological-algebra
relations: []
review: draft
---

::: {.definition title="Short exact sequence"}
An exact sequence of the form
\[
0 \to A \mapsvia{i} B \mapsvia{j} C \to 0
,\]
equivalently: $i$ is injective, $j$ is surjective, and $\im i = \ker j$, so that $C \cong B/i(A)$.
It **splits** iff there is $s: C\to B$ with $j\circ s = \id_C$, equivalently a retraction $r: B\to A$ with $r\circ i = \id_A$, and then $B \cong A \oplus C$.
:::

::: {.concept}
See Hatcher, pp. 114 and 147.
:::
