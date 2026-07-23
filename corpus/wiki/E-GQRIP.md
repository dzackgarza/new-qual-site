---
schema: qual/card@1
id: E-GQRIP
kind: exercise
title: "Let $f$ be entire with $\\im(f) \\intersect \\DD_r(z_0)$ empty."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Let $f$ be entire with $\im(f) \intersect \DD_r(z_0)$ empty. 
Show $f$ must be constant without using the Casorati-Weierstrass or Picard theorems.

#complex/exercise/completed

:::

:::{.solution}
Write $g(z) \da f(z) - z_0$, so $\abs{g(z)} \geq r$.
Now $\abs{1/g(z)} \leq 1/r$ for all $z$, so $1/g$ is bounded. 
Moreover it is entire since $f(z) \neq z_0$ for any $z$, and so $1/g = c$ is constant.
Now unwind to get $f(z) = z_0 + {1\over c}$, which is also constant.
:::

