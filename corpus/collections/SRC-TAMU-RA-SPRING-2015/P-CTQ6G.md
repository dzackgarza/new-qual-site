---
schema: qual/card@1
id: P-CTQ6G
kind: problem
title: Isolated points iff the complement is not dense; countable complete metric
  spaces have dense isolated points
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Completeness
  - Density
relations: []
review: draft
---

::: {.problem}
(1) $Y$ is metric space.
Prove $y\in Y$ is isolated iff the complement $\{y\}^c$ is not dense in $Y$

(2) Let $X$ be a countable nonempty complete metric space.
Prove that the set of isolated points is dense in $X$.
:::

:::{.solution}
If $\{y\}$ is open, then $\{y\}\cap\{y\}^c=\varnothing$, which implies that $\{y\}^c$ is not dense. In the converse, $\{y\}^c$ being not dense implies that there is an open set $O$ such that $\{y\}^c\cap O=\varnothing$. Then $\{y\}=O$ and thus $y$ is an isolated point.

For (2), If not, there is an open set $O$ such that $O\cap\{y\in X:y\ \text{is isolated}\}=\varnothing$. It is not hard to see since $X$ is complete, $O$ itself is a Baire space, say, given a sequence $O_n\subset O$, in which memebers $O_n$ are open and dense in $O$, then $\bigcap_n O_n$ is also dense in $O$ (consider $U_n=O_n\cup \overline{O}^c$). Then, for all $y\in O$, $y$ is not isolated. It implies that $O\setminus\{y\}$ is dense in $O$. Then by Baire category theorem, $\emptyset=\bigcap_{y\in O}(O\setminus\{y\})$ is also dense in $O$. A contradiction.
:::
