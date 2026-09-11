---
schema: qual/card@1
id: P-PRACT20-W6-25
kind: problem
title: "Week 6: Miscellaneous Topics, problem 25"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let S, T, U be nonempty sets and $f : S \to T , g : T \to U$ be functions such that $g \circ f : S  U$ is one-to-one.
Prove that f is one-to-one.
Show by example that g need not be one-to-one.
:::

::: {.solution}
If f is not one-to-one, there are x, $, y \in S , x \neq y$ such that $f ( x ) = f ( y )$ . But then $( g \circ f ) ( x ) = g ( f ( x ) ) = g ( f ( y ) ) = ( g \circ f ) ( y )$ shows that $g \circ f$ is not one-to-one.
Contrapositively, if $g \circ f$ is one-to-one, then so is f . The latter part of the problem is a bit tricky because it seems false at first glance.
However, if $g \circ f$ is one-to-one, we can only guarantee that g is one-to-one on the range of $f ;$ it may not be one-to-one on the entirety of T . Indeed, let $S = T = U = \mathbb { R }$ and take $f ( x ) = e ^ { x }$ and $g ( x ) = x ^ { 2 }$ for $x \in \mathbb { R }$ . Then $( g \circ f ) ( x ) = e ^ { 2 x }$ for $x \in \mathbb { R }$ is a one-to-one function while g is not a one-to-one function.
:::
