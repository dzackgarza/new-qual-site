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

::: pf

::: {.pf-step #s1}

Take $X=\mathbb R$ with its usual topology and $A=\mathbb R$.

::: pf-proof

The real line is Hausdorff, and $A=X$ is closed in $X$.

:::

:::

::: {.pf-step #s2}

The set $A$ is not compact.

::: pf-proof

The open cover $\{(-n,n):n\ge1\}$ has no finite subcover, since every finite subfamily is contained in $(-N,N)$ for some $N$.

:::

:::

::: pf-step

Thus a closed subset of a Hausdorff space need not be compact.

::: pf-proof

The example in steps [](#s1){.pf-ref} and [](#s2){.pf-ref} has all the required properties.

:::

:::

:::

:::
