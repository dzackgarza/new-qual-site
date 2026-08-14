---
schema: qual/card@1
id: T-6ABNR
kind: theorem
title: "Characterizations of Diagonalizability"
classification:
  areas:
  - algebra
  topics:
  - diagonalization
  - minimal-and-characteristic-polynomials
relations: []
review: draft
---

::: {.theorem title="Characterizations of Diagonalizability"}
$M$ is diagonalizable over $\FF \iff \min_M(x, \FF)$ splits into **distinct** linear factors over $\FF$.

Splitting alone is not enough: $\begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$ has $\min_M(x) = (x-1)^2$, whose only root lies in $\FF$, and it is not diagonalizable.
The distinctness of the factors is what does the work.
:::
