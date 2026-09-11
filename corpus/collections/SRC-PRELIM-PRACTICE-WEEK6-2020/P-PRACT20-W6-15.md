---
schema: qual/card@1
id: P-PRACT20-W6-15
kind: problem
title: "Week 6: Miscellaneous Topics, problem 15"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $S \subset [ 0 , 1 ] \times [ 0 , 1 ]$ consist of all points $( x , y ) \in [ 0 , 1 ] \times [ 0 , 1 ]$ such that x or y or both is irrational.
Which of the following is true (with respect to the standard topology on $\mathbb { R } ^ { 2 } ) ?$

(A) S is open (B) S is closed (C) S is connected (D) S is totally disconnected (E) S is compact
:::

::: {.solution}
(A) is false.
By density of $\mathbb { Q } ^ { 2 }$ in $\mathbb { R } ^ { 2 }$ , any open ball centered at a point in S contains a point with rational coordinates which is not in S.

(B) is false.
By density of $( \mathbb { R } \setminus \mathbb { Q } ) ^ { 2 }$ in $\mathbb { R } ^ { 2 }$ , S doesn’t contain all its limit points since we can take a sequence of points in $S$ converging to a point with rational coordinates which is not in S.

(E) is false.
S is not compact since it is not closed.

(C) is true.
In fact this set is path-connected.
Consider for any $( x , y ) \in S .$ , one of x or $y$ is irrational.
If x is irrational then the vertical line $V _ { x } = \{ ( x , t ) : t \in [ 0 , 1 ] \}$ is contained in S. Then we can travel along this line to the point $( x , \pi / 4 )$ . But the entire horizontal line $H _ { \pi / 4 } = \{ ( t , \pi / 4 )$ : $t \in [ 0 , 1 ] \}$ is contained in S and so we can then travel along this line to $( \pi / 4 , \pi / { \dot { 4 } } )$ . Likewise, if y is irrational, we can travel along the horizontal line $H _ { y }$ to the point $( \pi / 4 , y )$ and then along the vertical line $V _ { \pi / 4 }$ to the point $( \pi / 4 , \pi / 4 )$ . This shows that any point can be connected by a continuous path to $( \pi / 4 , \pi / 4 )$ , but then by composing paths, any two points can be connected to each other by a continuous path.

(D) is false since (C) is true.
:::
