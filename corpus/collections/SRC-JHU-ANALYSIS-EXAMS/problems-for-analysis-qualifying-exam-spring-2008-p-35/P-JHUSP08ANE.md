---
schema: qual/card@1
id: P-JHUSP08ANE
kind: problem
title: "Entire functions bounded by a nonvanishing entire function are constant multiples"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
5) Prove the following statement: If f and g are entire functions, $g ( z ) \neq 0$ and $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C } .$ , then $f ( z ) = C g ( z )$ for some constant C.
:::

::: {.solution}
<1>1. $h\da f/g$ is entire and $\abs h\le1$.

::: {.proof}
$g$ has no zeros, so $h$ is holomorphic on $\CC$, and $\abs{h}=\abs f/\abs g\le1$ by hypothesis.
:::

<1>2. Q.E.D.

::: {.proof}
By step <1>1 and Liouville's theorem, $h$ is a constant $C$, so $f=Cg$.
:::
:::
