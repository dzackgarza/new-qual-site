---
schema: qual/card@1
id: E-WKY7C
kind: problem
title: Entire functions agreeing with $e^x$ on $\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Find all entire functions $f$ such that $f(x) = e^x$ on $\RR$.
:::

::: {.solution}
::: pf

::: pf-step
The only such function is $\boxed{f(z) = e^z}$.

::: pf-proof
$e^z$ is entire and equals $e^x$ on $\RR$.
Conversely, $g(z) \definedas f(z) - e^z$ is entire and vanishes on $\RR$, a set with a limit point in $\CC$, so $g\equiv0$ by the identity theorem.
:::

:::

:::

:::
