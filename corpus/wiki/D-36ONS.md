---
schema: qual/card@1
id: D-36ONS
kind: definition
title: "Chain Map"
classification:
  areas:
  - topology
  topics:
  - homological-algebra
relations: []
review: draft
---

::: {.definition title="Chain Map"}
A map between chain complexes $(C_*, \del_{C}) \mapsvia{f} (D_*, \del_{D})$ is a chain map iff each component $C_{i} \mapsvia{f_{i}} D_{i}$ satisfies
$$
f_{i-1}\circ\del_{C, i} = \del_{D,i} \circ f_{i}
$$
(i.e this forms a commuting ladder)

<!--![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Chain_{map}.svg/650px-Chain_{map}.svg.png)-->
:::
