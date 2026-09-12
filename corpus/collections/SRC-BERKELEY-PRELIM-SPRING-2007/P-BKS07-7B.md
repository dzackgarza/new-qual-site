---
schema: qual/card@1
id: P-BKS07-7B
kind: problem
title: UC Berkeley Spring 2007 prelim 7B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Given any group G, define a binary operation ∗ on the set $H = G \times G$ by $( g _ { 1 } , h _ { 1 } )$ ∗ $( g _ { 2 } , h _ { 2 } ) = ( g _ { 1 } g _ { 2 } , g _ { 2 } ^ { - 1 } h _ { 1 } g _ { 2 } h _ { 2 } )$

(a) Show that $( H , * )$ is group.

(b) In the case that G is the alternating group $A _ { n }$ on n letters with $n \geq 5$ , prove that H has no subgroup of index 2.
:::

::: {.solution}
(a) $( H , * )$ is the semidirect product $G \ltimes G$ where $G$ acts on itself by conjugation.

(b) By the solution to part (a), H contains a normal subgroup N such that $N \cong H / N \cong$ $A _ { n }$ . Since $A _ { n }$ is simple, the Jordan-H¨older theorem implies that $H / M \cong A _ { n }$ for every nontrivial proper normal subgroup $M \subseteq H$ . In particular, H cannot have a subgroup M of index 2, since such a subgroup is always normal.

(Alternatively, one could “avoid” the Jordan-H¨older theorem by essentially proving it in the special case needed, considering first the intersection of M with N, and then the image of M in $H / N . )$
:::
