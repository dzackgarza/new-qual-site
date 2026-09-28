---
schema: qual/card@1
id: P-BKS04-5B
kind: problem
title: UC Berkeley Spring 2004 prelim 5B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $n _ { 1 } , \ldots , n _ { r }$ be integers $\geq 2$ . Prove that there is a finite group G containing elements $g _ { 1 } , \ldots , g _ { r }$ such that $g _ { i }$ has exact order $n _ { i }$ for each $i ,$ and $g _ { i } g _ { j } \neq g _ { j } g _ { i }$ for $i \neq j$
:::

::: {.solution}
Let $T _ { 1 } , \ldots , T _ { r }$ be disjoint sets with $\# T _ { i } = n _ { i } - 1$ . Let S be the union of the $T _ { i }$ together with one more element x outside all the $T _ { i }$ . Let G be the set of permutations of S.

Choose $g _ { i } \in G$ such that $g _ { i }$ acts as an $n _ { i } { \mathrm { - } } \mathrm { C y }$ cle on $T _ { i } \cup \{ x \}$ , and acts as the identity on the complement.
Then $g _ { i }$ has order $n _ { i }$ . If $i \neq j$ , then $( g _ { i } g _ { j } ) ( x ) = g _ { i } ( g _ { j } ( x ) ) \in g _ { i } ( T _ { j } ) = T _ { j }$ , and similarly $( g _ { j } g _ { i } ) ( x ) \in T _ { i }$ , so $g _ { i } g _ { j } \neq g _ { j } g _ { i }$ .
:::
