---
schema: qual/card@1
id: P-4FVOI
kind: problem
title: Isomorphic but unequal fields
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
What is an example of isomorphic but not equal fields?
:::

::: {.solution}
Let $\omega$ be a primitive cube root of unity.
The fields $\QQ(\sqrt[3]2)$ and $\QQ(\omega\sqrt[3]2)$ are isomorphic, because $\sqrt[3]2$ and $\omega\sqrt[3]2$ have the same minimal polynomial $x^3-2$ over $\QQ$, so both fields are isomorphic to $\QQ[x]/(x^3-2)$.
They are not equal inside $\CC$: $\QQ(\sqrt[3]2)\subset\RR$, while $\omega\sqrt[3]2\notin\RR$.
See [[P-3VHPO]] for the full argument.
:::
