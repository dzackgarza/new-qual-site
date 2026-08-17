---
schema: qual/card@1
id: E-GPFKM
kind: exercise
title: "Estimating and conformal maps"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
solved: true
---
:::{.exercise title="Estimating and conformal maps"}
Suppose $f:\HH\to \CC$ with $\abs{f(z)}< 1$ and $f(i) = 0$.
Find an upper bound for $f(2i)$.

:::

:::{.solution}
Compose with the inverse Cayley map $g(z) \da i{1+z\over 1-z}$ so $g: \DD\to \HH$ to get $F\da f\circ g:\DD\to \DD$, where $F(0) =f(g(0))=f(i) = 0$.
So Schwarz applies and $\abs{F(z)}\leq \abs{z}$.
Now a small trick:
\[
\abs{f(2i)} = \abs{(f\circ g\circ g\inv)(2i)} = \abs{ F \qty{z+i\over z-i}\evalfrom_{z=2i} } = \abs{F \qty{1\over 3} } \leq {1\over 3}
.\]
:::
