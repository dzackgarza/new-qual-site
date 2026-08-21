---
schema: qual/card@1
id: P-A33VH
kind: problem
title: Setwise distance of compact sets is attained, and vanishes only on a nonempty
  intersection
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
solved: false
---

:::{.problem}
For nonempty subsets $A, B$ of a metric space $(X, d)$, define the **setwise distance** as 
\[
d(A, B) \da \inf \ts{ d(a, b) \st a\in A,\, b\in B } 
.\]

a. 
Suppose that $A$ and $B$ are compact.
Show that there is an $a\in A$ and $b\in B$ such that $d(A, B) = d(a, b)$.

b.
Suppose that $A$ is closed and $B$ is compact.
Show that if $d(A, B) = 0$ then $A \intersect B \neq \emptyset$.

c. 
Give an example in which $A$ is closed, $B$ is compact, and $d(a, b) > d(A, B)$ for all $a\in A$ and $b\in B$.

> Hint: take $X = \ts{ 0 } \union (1, 2] \subset \RR$.
> Throughout this problem, you may use without proof that the map $d:X\cross X\to \RR$ is continuous.

:::
