---
schema: qual/card@1
id: P-MDFEL
kind: problem
title: "Suppose that $X$ is a Hausdorff topological space and that $A \\subset\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Suppose that $X$ is a Hausdorff topological space and that $A \subset X$. 
Prove that if $A$ is compact in the subspace topology then $A$ is closed as a subset of X.
:::

:::{.solution}
\envlist

- Let $A \subset X$ be compact, and pick a fixed $x\in X\setminus A$.
- Since $X$ is Hausdorff, for arbitrary $a\in A$, there exists opens $U_{a} \ni a$ and $U_{x,a}\ni x$ such that $V_{a} \intersect U_{x,a} = \emptyset$.
- Then $\theset{U_{a} \suchthat a\in A} \rightrightarrows A$, so by compactness there is a finite subcover $\theset{U_{a_i}} \rightrightarrows A$.

- Now take $U = \union_i U_{a_i}$ and $V_x = \intersect_i V_{a_i, x}$, so $U\intersect V = \emptyset$.
  - Note that both $U$ and $V_x$ are open.

- But then defining $V \definedas \union_{x\in X\setminus A} V_x$, we have $X\setminus A \subset V$ and $V\intersect A = \emptyset$, so $V = X\setminus A$, which is open and thus $A$ is closed.

:::

