---
schema: qual/card@1
id: D-JRPTK
kind: definition
title: "Equivalent Matrices"
classification:
  areas:
  - algebra
  topics:
  - matrices
  - canonical-forms
  - linear-algebra
relations: []
review: draft
---

::: {.definition title="Equivalent Matrices"}
Two matrices $A, B$ over a PID $R$ are **equivalent** iff $A = PBQ$ for some invertible $P, Q$.
This happens iff

- They have the same invariant factors, equivalently the same Smith normal form.

The rank is determined by the invariant factors, so equivalent matrices have equal rank; over a field the invariant factors carry no information beyond the rank.

The Jordan canonical form is *not* an invariant of equivalence.
It is preserved by **similarity**, $A = PBP\inv$, which is the strictly finer relation.
:::
