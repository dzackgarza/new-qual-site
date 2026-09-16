---
schema: qual/card@1
id: P-UCLAB12-04
kind: problem
title: Baire category theorem
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
A subset K of a metric space $( X , d )$ is called nowhere dense if K has empty interior, (i. e., if $U \subseteq K$ , U open in X imply $U = \emptyset .$ Prove the Baire theorem that if $( X , d )$ is a complete metric space, then X is not a countable union of closed nowhere dense sets.
Hint: Assume $X = \textstyle \bigcup _ { n } K _ { n }$ where each $K _ { n }$ is closed and nowhere dense.
Show there is $x _ { 1 } \in X$ and $0 < \delta _ { 1 } < 1 / 2$ such that $B _ { 1 } = B ( x _ { 1 } , \delta _ { 1 } ) = \{ y \in X : d ( y , x ) < \delta _ { 1 } \}$ satisfies $B _ { 1 } \cap K _ { 1 } = \emptyset$ and there is $x _ { 2 } \in X$ and $\begin{array} { r } { 0 < \delta _ { 2 } < \frac { \delta _ { 1 } } { 2 } } \end{array}$ such that $B _ { 2 } = B ( x _ { 2 } , \delta _ { 2 } )$ satisfies $B _ { 2 } \subset B _ { 1 }$ and $B _ { 2 } \cap K _ { 2 } = \emptyset$ . Then continue by induction to find a sequence $\{ x _ { n } \}$ in X that converges to $x \in X \backslash \bigcup _ { n = 1 } ^ { \infty } K _ { n }$
:::
