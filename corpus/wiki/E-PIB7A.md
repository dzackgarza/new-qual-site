---
schema: qual/card@1
id: E-PIB7A
kind: exercise
title: "Cancelling poles"
classification:
  areas:
  - complex-analysis
  topics:
  - blaschke-factors
  - poles
  - meromorphic-functions
relations: []
review: draft
---
:::{.exercise title="Cancelling poles"}
Let $f$ be meromorphic on $\DD$ with no poles on $\bd\DD$.
Show that there exists a meromorphic $g$ with *no* poles in $\DD$ such that $\abs{f(z)} = \abs{g(z)}$ when $\abs{z} = 1$.

:::

:::{.solution}
Write $\ts{a_1,\cdots, a_n}$ for all of the poles of $f$, indexed with multiplicity, and define
\[
g(z) \da \prod_{1\leq k\leq n} \psi_{a_k}(z) f(z) 
\da \qty{ \prod_{1\leq k \leq n}{z-a_k\over 1 -\bar{a_k} z}} f(z)
.\]
Then $g$ has no poles, and since $\abs{ \psi_{a_k} } = 1$ on $\bd \DD$, this works.
:::
