---
schema: qual/card@1
id: P-PSTM-03
kind: problem
title: A non-Hausdorff quotient of the unit interval
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $X = [ 0 , 1 ] / ( \frac { 1 } { 4 } , \frac { 3 } { 4 } )$ be the quotient space of the unit interval, where the open interval $\left( \textstyle { \frac { 1 } { 4 } } , \frac { 3 } { 4 } \right)$ is identified to a single point.
Show that X is not a Hausdorff space.
:::

::: {.solution}
Recall that in a quotient space $X / A = ( X \setminus A ) \coprod [ \{ * \}$ , the open sets are of one of two types:

(1) either an open set in $X \setminus A ;$ ; or

(2) of the form $\{ * \} \cup ( W \cap ( X \setminus A ) )$ , where W is an open set in X, containing A. In our situation, $X = \left\lceil 0 , 1 \right\rceil$ and $\begin{array} { r } { A = \left( \frac { 1 } { 4 } , \frac { 3 } { 4 } \right) } \end{array}$ . Take $\textstyle x = { \frac { 1 } { 4 } }$ and $\begin{array} { r } { y = \frac { 3 } { 4 } } \end{array}$ , viewed as elements of $X / A$ Suppose U and and V are open, disjoint subsets of $X / A _ { ; }$ containing x and y, respectively.
Then, necessarily, both U and V must be of type (2), since an open subset of [0, 1] containing one of the endpoints of the interval $\textstyle { \left( { \frac { 1 } { 4 } } , { \frac { 3 } { 4 } } \right) }$ must intersect that interval.
But then both U and V must contain the element $\{ * \}$ , and thus cannot be disjoint—a contradiction.
:::
