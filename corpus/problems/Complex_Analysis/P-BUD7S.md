---
schema: qual/card@1
id: P-BUD7S
kind: problem
title: Distance between disjoint compact sets in $\RR^n$ is attained
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Euclidean Spaces
relations: []
review: draft
---

::: {.problem}
Suppose $A, B \subseteq \RR^n$ are disjoint and compact.
Prove that there exist $a\in A, b\in B$ such that
$$
\norm{a - b} = \inf\theset{\norm{x-y} \suchthat x\in A,\, y\in B}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #continuous}
The function $d:A\times B\to\RR$, $d(x,y)\coloneqq\norm{x-y}$, is continuous on the compact space $A\times B$.

::: pf-proof
$d$ is the composition of the continuous maps $(x,y)\mapsto x-y$ and $\norm{\cdot}$, and a finite product of compact spaces is compact.
:::

:::

::: pf-step
There exist $a\in A$ and $b\in B$ with $\norm{a-b}=\inf\theset{\norm{x-y}\suchthat x\in A,\,y\in B}$.

::: pf-proof
By step [](#continuous){.pf-ref} and the extreme value theorem, $d$ attains its infimum at some $(a,b)\in A\times B$.
:::

:::

:::

:::

::: {.remark}
Disjointness is not needed for the existence of $a$ and $b$; it guarantees that the minimum distance $\norm{a-b}$ is positive.
:::
