---
schema: qual/card@1
id: PR-QDIOC
kind: proposition
title: Exactness of $A\to B\to C$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.proposition}
A sequence of homomorphisms $A \mapsvia{f_1} B \mapsvia{f_2} C$ is [[D-STPAM|exact]] at $B$ if and only if $\im f_1 = \ker f_2$.
In that case $f_2 \circ f_1 = 0$; the converse fails, since $f_2\circ f_1 = 0$ only gives $\im f_1\subseteq\ker f_2$.
:::
