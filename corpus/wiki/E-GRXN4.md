---
schema: qual/card@1
id: E-GRXN4
kind: exercise
title: True/false
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Essential Singularities
  - Laurent Series
  - Counterexamples
relations: []
review: draft
---

:::{.exercise title="True/false"}
Prove that the following statements or true, or find a counterexample:

- If $f,g$ have a pole at $a$, then $f+g$ has a pole at $a$.
- If $f,g$ have a pole at $a$, then $fg$ has a pole at $a$.
- If $f$ has an essential singularity at $z_0$ at $g$ is has a pole at $z_0$, then $z_0$ is an essential singularity for $f+g$.
- If $f$ has a pole of order $N$ at $z_0$ then $f^2$ has a pole of order $2N$ at $z_0$.

 

:::

:::{.solution}
\envlist

- False: $f(z) \da 1/z, g(z) \da -1/z \implies f+g = 0$.
- False: $f(z) = g(z) = 1/z \implies fg = 1/z^2$.
- True: write $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$, which has infinitely many negative coefficients, and $g(z) = \sum_{k\geq -N}d_k (z-z_0)^k$.
  Then 
  \[
  f(z) + g(z) = \sum_{k\leq -N-1}c_k(z-z_0)^k + \sum_{k\geq -N} (c_k + d_k)(z-z_0)^k
  ,\] 
  which again has infinitely many negative coefficients.
- True: check the Laurent expansion directly:
\[
  \qty{ \sum_{k\geq -N} c_k (z-z_0)_k }^2 
  &= {c_{-N}(z-z_0)^{-N} + \bigo((z-z_0)^{-N+1})}^2 \\
  &= (c_{-N})^2 (z-z_0)^{-2N} + \bigo((z-z_0)^{-2N+1})
.\]
  An easier alternative, use theorem 1.2 from S&S: write $f(z) = (z-z_0)^{-N} g(z)$ where $g$ is holomorphic and (importantly) nonvanishing in a neighborhood of $z_0$.
  Then $f(z)^2 = (z-z_0)^{-2N}(g(z))^2$, where $g^2$ is again nonvanishing in a neighborhood of $z_0$ since $\CC$ is an integral domain.
:::
