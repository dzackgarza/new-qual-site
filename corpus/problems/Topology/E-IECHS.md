---
schema: qual/card@1
id: E-IECHS
kind: problem
title: A closed subset of a Hausdorff space need not be compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Show that a closed subset of a Hausdorff space need not be compact.
:::

::: {.solution}
<1>1. Take $X=\mathbb R$ with its usual topology and $A=\mathbb R$.
::: {.proof}
The real line is Hausdorff, and $A=X$ is closed in $X$.
:::

<1>2. The set $A$ is not compact.
::: {.proof}
The open cover $\{(-n,n):n\ge1\}$ has no finite subcover, since every finite subfamily is contained in $(-N,N)$ for some $N$.
:::

<1>3. Thus a closed subset of a Hausdorff space need not be compact.
::: {.proof}
The example in <1>1--<1>2 has all the required properties.
:::
:::
