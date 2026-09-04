---
schema: qual/card@1
id: E-GPFKM
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
Suppose $f:\HH\to \CC$ with $\abs{f(z)}< 1$ and $f(i) = 0$.
Find an upper bound for $\abs{f(2i)}$.
:::

::: {.solution}
Compose with the inverse Cayley map $g(z) \da i{1+z\over 1-z}$ so $g: \DD\to \HH$ to get $F\da f\circ g:\DD\to \DD$, where $F(0) =f(g(0))=f(i) = 0$.
So Schwarz applies and $\abs{F(z)}\leq \abs{z}$.
The inverse of $g$ is
\[
g^{-1}(w)={w-i\over w+i},
\qquad
g^{-1}(2i)={1\over3}.
\]
Therefore
\[
\abs{f(2i)}
=\abs{F(g^{-1}(2i))}
=\abs{F(1/3)}
\le {1\over3}.
\]
:::
