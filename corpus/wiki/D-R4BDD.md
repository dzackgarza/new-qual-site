---
schema: qual/card@1
id: D-R4BDD
kind: definition
title: "Poles (and associated terminology)"
classification:
  areas:
  - complex-analysis
  topics:
  - poles
  - singularities
relations: []
review: draft
---
:::{.definition title="Poles (and associated terminology)"}
A *pole* $z_0$ of a function $f(z)$ is a zero of $g(z) \definedas {1\over f(z)}$.
Equivalently, $\lim_{z\to z_0} f(z) = \infty$.
In this case there exists a minimal $n$ and a holomorphic $h$ such that
\[
f(z) = \qty{z-z_0}^{-n} h(z)
.\]
Such an $n$ is the *order* of the pole.
A pole of order 1 is said to be a *simple pole*.
:::
