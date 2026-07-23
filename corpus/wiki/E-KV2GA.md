---
schema: qual/card@1
id: E-KV2GA
kind: exercise
title: "Power series are continuous"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Power series are continuous"}
Show that any power series is continuous on its domain of convergence. 

#complex/exercise/completed

:::

:::{.solution}
Let $f(z) = \lim_{N\to\infty} \sum_{k\leq N} c_k (z-z_0)^k$.
Use that power series converge uniformly and absolutely within their disc of convergence, each term is a continuous function, and finite sums of continuous functions are again continuous.
So the partial sums $S_N$ are continuous, and since $S_N\to f$ uniformly, $f$ is continuous by the uniform limit theorem.

:::

