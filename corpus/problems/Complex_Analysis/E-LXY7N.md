---
schema: qual/card@1
id: E-LXY7N
kind: problem
title: A non-equicontinuous sequence
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Counterexamples
  - Sequences of Functions
relations: []
review: draft
---

:::{.exercise}
Exhibit a sequence of functions that is not equicontinuous.
:::

:::{.solution}
The family $f_k(x) = x^k$ is not equicontinuous, since fixing $x_0 \in (0, 1)$ we have 
\[
\abs{f_k(x_0) - f_k(1)} \convergesto{k\to \infty} 1 > \eps
.\]
:::

