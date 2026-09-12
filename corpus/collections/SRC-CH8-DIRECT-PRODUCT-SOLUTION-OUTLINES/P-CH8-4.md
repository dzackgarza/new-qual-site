---
schema: qual/card@1
id: P-CH8-4
kind: problem
title: Chapter 8 exercise 4
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that $G \oplus H$ is Abelian if and only if G and H are Abelian. State the general case.
:::

::: {.solution}
Let $G \oplus H$ be Abelian.
Then $x y = y x$ for all $x , y \in G \oplus H$ . By definition of external direct product, $x = ( g _ { 1 } , h _ { 1 } )$ and $y = ( g _ { 2 } , h _ { 2 } )$ for $g _ { 1 } , g _ { 2 } \in G$ and $h _ { 1 } , h _ { 2 } \in H$ . Thus $x y = y x$ implies $\left( g _ { 1 } g _ { 2 } , h _ { 1 } h _ { 2 } \right) = \left( g _ { 2 } g _ { 1 } , h _ { 2 } h _ { 1 } \right)$ . Hence, $g _ { 1 } g _ { 2 } = g _ { 2 } g _ { 1 }$ and $h _ { 1 } h _ { 2 } = h _ { 2 } h _ { 1 }$ . Since $x , y$ are arbitrary, all elements of G commute as do all elements in H, and both groups are Abelian.
This argument reverses entirely to show that G and H are Abelian implies $G \oplus H$ is Abelian.

In general, the external direct product of a finite number of groups is Abelian if and only if each group in the product is Abelian.
:::
