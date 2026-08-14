---
schema: qual/card@1
id: D-ASXW6
kind: definition
title: "Closure of a set"
classification:
  areas:
  - topology
  topics:
  - closure
  - point-set
relations: []
review: draft
---
:::{.definition title="Closure of a set"}
For $U \subseteq X$, the **closure of $U$ in $X$** is given by 
\[
\cl_X(U) = \Intersect_{\substack{ B\supseteq U \\ \text{ closed} }} B
,\]
the intersection of all closed sets in $X$ containing $U$. 
For $Y\subseteq X$ a subspace containing $U$, the closure of $U$ in $Y$ is 
\[
\cl_Y(U) = \cl_X(U) \intersect Y
.\].[^closure_relative_theorem]
In general, we write $\bar{U} \da \cl_X(U)$.

An equivalent condition: $x\in \cl_X(U) \iff$ every neighborhood of $x$ in $X$ intersects $U$.[^munkres_pt_in_closure]
This is theorem 17.4 in Munkres
Munkres 17.5

:::

[^closure_relative_theorem]:

[^munkres_pt_in_closure]:
