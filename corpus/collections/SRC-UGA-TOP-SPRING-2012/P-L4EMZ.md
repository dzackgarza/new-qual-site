---
schema: qual/card@1
id: P-L4EMZ
kind: problem
title: Compactness of $\{0\}\cup\{1/n\}$ and of $(0,1]$
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
---

::: {.problem title="?"}
Let $X$ be a topological space.

a. State what it means for $X$ to be compact.

b. Let $X = \theset{0} \cup \theset{{1\over n} \mid n \in \ZZ^+ }$.
Is $X$ compact?

c. Let $X = (0, 1]$.
Is $X$ compact?
:::

::: {.remark}
Incomplete proof for part 3.
:::

::: {.concept}
See Munkres p.164, especially for (ii).
:::

::: {.solution}
\envlist

a. See definitions in review doc.

b. Direct proof:

- Let $\theset{U_i \suchthat j\in J}\covers X$; then $0\in U_j$ for some $j\in J$.

- In the subspace topology, $U_i$ is given by some $V\in \tau(\RR)$ such that $V\intersect X = U_i$

  - A basis for the subspace topology on $\RR$ is open intervals, so write $V$ as a union of open intervals $V = \union_{k\in K} I_k$.

  - Since $0\in U_j$, $0\in I_k$ for some $k$.

- Since $I_k$ is an interval, it contains infinitely many points of the form $x_n = {1 \over n} \in X$

- Then $I_k \intersect X \subset U_j$ contains infinitely many such points.

- So there are only *finitely* many points in $X\setminus U_j$, each of which is in $U_{j(n)}$ for some $j(n) \in J$ depending on $n$.

c. Todo

::: {.remark}
Need direct proof
:::
:::
