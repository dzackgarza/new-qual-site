---
schema: qual/card@1
id: P-RASP15A
kind: problem
title: "True/false on weak convergence, Fubini, L^p membership, and limit of integrals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Determine if the statements below are True or False.

(a) (10 points) In an infinite-dimensional Hilbert space $H$, for any weakly convergent sequence $\{x_n\}$, there exists a subsequence that is convergent with respect to the norm.

(b) (10 points) Since two iterated integrals exist and
$$
\int_{(0,1)} \int_{(0,1)} \frac{x^2 - y^2}{(x^2 + y^2)^2}\,dm(x)\,dm(y) = \int_{(0,1)} \int_{(0,1)} \frac{x^2 - y^2}{(x^2 + y^2)^2}\,dm(y)\,dm(x)
$$
we can conclude, via the Tonelli-Fubini theorem, that the double integral exists.

(c) (10 points) There exists a function $f \geq 0$ on $(0, \infty)$ such that $f \in L^p((0, \infty))$ if and only if $p = 1$.

(d) (10 points)
$$
\lim_{n \to \infty} \int_0^\infty \frac{\sin(x/n)}{(1 + x/n)^n}\,dm(x) = 0.
$$
:::
