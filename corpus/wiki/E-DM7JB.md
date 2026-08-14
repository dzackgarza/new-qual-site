---
schema: qual/card@1
id: E-DM7JB
kind: exercise
title: "Find all functions on the Riemann sphere that have a simple\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
  - poles
  - principal-parts
  - riemann-surfaces
relations: []
review: draft
---
:::{.problem title="?"}
Find all functions on the Riemann sphere that have a simple pole at $z=2$ and a double pole at $z=\infty$, but are analytic elsewhere.
:::

:::{.solution}
Write $f(z) = P_2(z) + g(z)$ where $P_2$ is the principal part of $f$ at $z=2$ and $g$ is holomorphic at $z=2$.
Then $g$ is an entire function with a double pole at $\infty$, and is thus a polynomial of degree at most $2$, so $g(z) = c_2z^2 + c_1 z + c_0$.
Since the pole of $f$ at $z=2$ is simple, $P_2(z) = \sum_{k\geq -1} d_k (z-2)^k$.
Combining these, we can write
\[
f(z) = d_{-1}(z-2)\inv + \sum_{0\leq k\leq 3} (d_k + c_k)(z-2)^k + \sum_{k\geq 3}d_k (z-2)^k 
.\]
However, if $d_k\neq 0$ for any $k\geq 3$, this results in a higher order pole at $\infty$, so $f$ must be of the form
\[
f(z) = d_{-1}(z-2)\inv + \sum_{0\leq k\leq 3} (d_k + c_k)(z-2)^k 
.\]
:::

