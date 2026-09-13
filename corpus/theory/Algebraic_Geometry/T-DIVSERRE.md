---
schema: qual/card@1
id: T-DIVSERRE
kind: theorem
title: Serre's criterion for ampleness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Globally Generated Sheaves
  - Cohomological Criteria
relations:
- kind: uses
  target: D-DIVAMPLE
review: draft
prompts:
- State a criterion for a sheaf to be ample.
- What is the cohomological characterisation of ampleness?
---

::: {.theorem}
Let $X$ be a scheme of finite type over a Noetherian ring $A$ and $\mcl$ invertible.
The following agree:

- $\mcl$ is ample;

- for every coherent $\mcf$ there is $n_0$ with $\mcf \tensor \mcl\tensorpower{}{n}$ globally generated for all $n \geq n_0$.

If $X$ is proper over $A$, both are equivalent to: for every coherent $\mcf$ there is $n_0$ with $H^i(X, \mcf \tensor \mcl\tensorpower{}{n}) = 0$ for all $i > 0$ and all $n \geq n_0$.
:::

::: {.remark}
This is the definition of ampleness worth carrying, because it is the one that gets used: ampleness is the licence to kill higher cohomology by twisting enough.
Every argument that starts "twist by $\OO(n)$ for $n \gg 0$" is an appeal to it.

On a projective scheme $\OO(1)$ is ample, and the criterion is then Serre vanishing.
The proper case is where the equivalence has content — it is how ampleness gets checked without exhibiting an embedding, and it is why ampleness is detectable from numerical data such as intersection numbers.
:::
