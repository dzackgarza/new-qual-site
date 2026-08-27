---
schema: qual/card@1
id: D-6BUWA
kind: definition
title: Singular Homology
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.definition}
A **singular $n\dash$simplex** in $X$ is a map $\sigma: \Delta^n \to X$, and $C_n(X)$ is the free abelian group on the singular $n\dash$simplices.
The boundary map is
\[
\del_n \sigma \da \sum_{i=0}^n (-1)^i \ro{\sigma}{[v_0,\cdots, \hat v_i, \cdots, v_n]}
,\]
which satisfies $\del_n \circ \del_{n+1} = 0$.
The **singular homology** of $X$ is
\[
H_n(X) \da \ker \del_n / \im \del_{n+1}
.\]
:::

::: {.concept}
See Hatcher, §2.1, p. 108.
:::
