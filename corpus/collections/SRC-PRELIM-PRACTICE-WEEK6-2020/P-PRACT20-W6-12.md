---
schema: qual/card@1
id: P-PRACT20-W6-12
kind: problem
title: "Week 6: Miscellaneous Topics, problem 12"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $d ( x , y ) = { \left\{ \begin{array} { l l } { 0 , x = y , } \\ { 1 , x \neq y . } \end{array} \right. }$ Which of the following hold in the metric space $( \mathbb { R } , d ) ?$

(A) $\{ x \}$ is open for each $x \in \mathbb { R }$ (B) Every subset of R is closed

(C) If $d ^ { \prime }$ is the ordinary metric on R, then the identity map $( \mathbb { R } , d ) \to ( \mathbb { R } , d ^ { \prime } )$ is continuous

(D) If $d ^ { \prime }$ is the ordinary metric on R, then the identity map $( \mathbb { R } , d ^ { \prime } )  ( \mathbb { R } , d )$ is continuous
:::

::: {.solution}
This is the discrete metric which generates the discrete topology on R; thus every set is open.
If every set is open, then every set is closed as well.
Thus (A) and (B) are true.

For (C) and (D), consider any space X with two topologies $\tau _ { 1 } , \tau _ { 2 }$ Recall the identity $\iota :$ $( X , \tau _ { 1 } )  ( X , \tau _ { 2 } )$ is continuous iff $\iota ^ { - 1 } ( V ) \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ But $\iota ^ { - 1 } ( V ) = V$ Thus the identity is continuous iff $V \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ . rephrasing yet again, the identity is continuous iff $\tau _ { 2 } \subset \tau _ { 1 }$ which is true iff $\tau _ { 1 }$ is finer than $\tau _ { 2 }$ . The discrete topology is finer than any other topology on R so (D) is false while (C) is true.
:::
