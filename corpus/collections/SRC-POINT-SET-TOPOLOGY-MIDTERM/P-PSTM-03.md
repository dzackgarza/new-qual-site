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
Write $I = [0,1]$ and $A = \left(\frac14, \frac34\right)$, so $X = I/A = (I \setminus A) \sqcup \{*\}$. The open sets of $I/A$ are of two types:

(1) an open subset of $I$ contained in $I \setminus A$; or

(2) a set $\{*\} \cup (W \cap (I \setminus A))$, where $W$ is an open subset of $I$ containing $A$.

Take $x = \frac14$ and $y = \frac34$, viewed as elements of $I/A$. Suppose $U$ and $V$ are open, disjoint subsets of $I/A$ containing $x$ and $y$, respectively.
Then both $U$ and $V$ are of type (2), since an open subset of $I$ containing an endpoint of the interval $\left(\frac14, \frac34\right)$ meets that interval.
But then both $U$ and $V$ contain the point $*$, and so they are not disjoint, a contradiction.
:::
