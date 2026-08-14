---
schema: qual/card@1
id: D-GFM35
kind: definition
title: "Simply Connected"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - homotopy
  - connectedness
relations: []
review: draft
---

::: {.definition title="Simply Connected"}
A space $X$ is **simply connected** if and only if $X$ is path-connected and every loop \( \gamma : S^1 \mapsvia{} X \) can be contracted to a point.

Equivalently, there exists a lift \( \hat \gamma : D^2 \mapsvia{} X \) such that \( \ro{\hat \gamma}{\bd D^2} = \gamma  \).

Equivalently, for any two paths \( p_1, p_2: I \mapsvia{} X \) such that \( p_1(0) = p_2(0) \) and \( p_1(1) = p_2(1) \), there exists a homotopy \( F: I^2 \mapsvia{} X \) such that \( \ro{F}{0} = p_1,\, \ro{F}{0} = p_2 \).

Equivalently, \( \pi _1 X = 1 \) is trivial.
:::
