---
schema: qual/card@1
id: D-BYIZA
kind: definition
title: Ext Group
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Cohomology
relations: []
review: draft
---

::: {.definition}
For $A$ an abelian group and $G$ a coefficient group, choose a free resolution
\[
\cdots \to F_2 \to F_1 \to F_0 \to A \to 0
,\]
apply $\Hom(\wait, G)$, drop the term $\Hom(A,G)$, and take cohomology of the resulting cochain complex; the result is $\Ext^n(A, G)$, independent of the resolution.
Over $\ZZ$ one has $\Ext^0(A,G) = \Hom(A,G)$, $\Ext^n = 0$ for $n\geq 2$, and
\[
\Ext^1(\ZZ, G) = 0, \qquad \Ext^1(\ZZ/m, G) = G/mG
.\]
:::

::: {.concept}
See Hatcher, §3.1, p. 195.
:::
