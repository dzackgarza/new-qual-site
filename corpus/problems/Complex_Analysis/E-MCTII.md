---
schema: qual/card@1
id: E-MCTII
kind: problem
title: Estimating and conformal maps
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is holomorphic and $\abs{f(z)}\leq 1$ for $\Re(z) > 0$ with $f(1) = 0$.
Find an upper bound for $\abs{f(2)}$.
:::

::: {.solution}
Use
\[
\phi(z)={z-1\over z+1},
\]
which maps the right half-plane biholomorphically onto $\DD$ and satisfies $\phi(1)=0$.
Set
\[
F=f\circ\phi^{-1}:\DD\to\DD.
\]
Then $F(0)=f(1)=0$, so Schwarz's lemma gives $|F(w)|\le|w|$.
Since
\[
\phi(2)={1\over3},
\]
we obtain
\[
|f(2)|=|F(\phi(2))|=|F(1/3)|\le {1\over3}.
\]
:::
