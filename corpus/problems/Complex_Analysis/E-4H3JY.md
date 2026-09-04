---
schema: qual/card@1
id: E-4H3JY
kind: problem
title: Disc to upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from $\DD$ to $\HH$.
:::

::: {.solution}
The inverse of the standard Cayley map $w\mapsto(w-i)/(w+i)$ is
\[
T(z)=i{1+z\over1-z}.
\]
For $z\in\DD$,
\[
\Im T(z)
=\Re {1+z\over1-z}
={1-|z|^2\over |1-z|^2}>0,
\]
so $T(\DD)\subseteq\HH$.
Its inverse is
\[
T^{-1}(w)={w-i\over w+i},
\]
which maps $\HH$ into $\DD$.
Thus $T:\DD\to\HH$ is biholomorphic, hence conformal.
:::
