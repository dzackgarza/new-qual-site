---
schema: qual/card@1
id: D-HOCNK
kind: definition
title: "Homotopy Lifting Property"
classification:
  areas:
  - topology
  topics:
  - homotopy
  - covering-spaces
relations: []
review: draft
---

::: {.definition title="Homotopy Lifting Property"}
A map $p: E\to B$ has the **homotopy lifting property** with respect to $Y$ iff, given a homotopy $g_t: Y \to B$ and a lift $\tilde g_0: Y\to E$ of $g_0$, there is a homotopy $\tilde g_t: Y\to E$ lifting $g_t$ and starting at $\tilde g_0$.
A **fibration** is a map with this property for every space $Y$.
Covering spaces have it for every $Y$, and there the lift is unique.
:::

::: {.concept}
See Hatcher, pp. 60 and 375; for covers, Proposition 1.30, p. 60.
:::
