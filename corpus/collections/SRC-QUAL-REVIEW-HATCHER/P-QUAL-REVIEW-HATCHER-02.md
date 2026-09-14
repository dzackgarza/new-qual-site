---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-02
kind: problem
title: Total Hom complexes preserve chain homotopies
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 2 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Suppose $C_*$ and $D_*$ are bounded-below chain complexes.
Form the double complex having $\operatorname{Hom}(C_i,D_j)$ in bidegree $(i,j)$, and write
\[
\underline{\operatorname{Hom}}(C_*,D_*)
\]
for its total complex.
The following facts are given:

1. If $C_*$ is free, then the functor
   \[
   D_*\longmapsto \underline{\operatorname{Hom}}(C_*,D_*)
   \]
   preserves all quasi-isomorphisms.

2. For any $D_*$, the functor
   \[
   C_*\longmapsto \underline{\operatorname{Hom}}(C_*,D_*)
   \]
   preserves chain homotopies.

Prove (2).

If
\[
H_0(C)=\mathbb Z,\qquad H_1(C)=\mathbb Z/3\oplus\mathbb Z,\qquad H_2(C)=\mathbb Z/4,\qquad H_3(C)=\mathbb Z/2,
\]
and
\[
H_0(D)=\mathbb Z/8,\qquad H_1(D)=\mathbb Z\oplus\mathbb Z/6,\qquad H_2(D)=\mathbb Z/2,
\]
with all other homology groups zero, determine the homology groups of $\underline{\operatorname{Hom}}(C_*,D_*)$.
Use the same circle of ideas used in proving the Künneth theorem.
:::
