---
schema: qual/card@1
id: E-SS7.EX-1
kind: exercise
title: "Bounded partial sums give convergence of the Dirichlet series for Re(s) > 0"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
---

::: exercise
1. Suppose that $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ is a sequence of real numbers such that the partial sums

$$
A _ {n} = a _ {1} + \dots + a _ {n}
$$

are bounded.
Prove that the Dirichlet series

$$
\sum_ {n = 1} ^ {\infty} \frac {a _ {n}}{n ^ {s}}
$$

converges for $\operatorname { R e } ( s ) > 0$ and defines a holomorphic function in this half-plane.

[Hint: Use summation by parts to compare the original (non-absolutely convergent) series to the (absolutely convergent) series $\sum A _ { n } ( n ^ { - s } - ( n + 1 ) ^ { - s } )$ . An estimate for the term in parentheses is provided by the mean value theorem. To prove that the series is analytic, show that the partial sums converge uniformly on every compact subset of the half-plane $\operatorname { R e } ( s ) > 0 . ]$
:::
