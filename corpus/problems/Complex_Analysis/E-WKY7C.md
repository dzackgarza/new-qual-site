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
The function $g(z) \da f(z) - e^z$ is entire and identically zero on $\RR$, which contains a limit point.
So $g(z) \equiv 0$ on $\CC$, meaning $f(z) = e^z$ is the only such function.
:::
