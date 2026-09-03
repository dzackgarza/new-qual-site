---
schema: qual/card@1
id: E-WNTXK
kind: problem
title: An entire function with values in $\HH$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is entire and $f(\CC) \subseteq \HH$.
Show that $f$ must be constant.
:::

::: {.solution}
Let $T:\HH\to\DD$ be a Cayley transform, for example
\[
T(w)=\frac{i-w}{i+w}.
\]
Then
\[
F\da T\circ f:\CC\to\DD
\]
is entire and bounded.
By Liouville's theorem, $F\equiv c$ for some $c\in\DD$.
Since $T$ is injective,
\[
f\equiv T^{-1}(c),
\]
so $f$ is constant.
:::
