---
schema: qual/card@1
id: P-RASP23D
kind: problem
title: "Radon measure on a non-standard metric space"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Define the distance function between $(x_1, y_1)$ and $(x_2, y_2)$ in the plane to be
$$
d = \begin{cases} |y_1 - y_2| & \text{if } x_1 = x_2, \\ 1 + |y_1 - y_2| & \text{if } x_1 \neq x_2. \end{cases}
$$

(i) Prove that this is indeed a metric.

(ii) The corresponding metric space $(X, d)$ is locally compact.

(iii) For any $f \in C_c(X)$, let $F$ be the set of $x$ such that there exists $y$ with $f(x,y) \neq 0$.
Prove that $F$ is a finite set $\{x_1, x_2, \ldots, x_n\}$.

(iv) For $f$ in (iii) define $I(f) = \sum_{i=1}^{n} \int_{-\infty}^{\infty} f(x_i, y)\,dy$.
Then $I(f)$ induces a Radon measure $\mu$ on $X$.
Is $\mu$ inner regular for all Borel sets?
If yes, prove it.
If no, find a Borel set which is not inner regular.
:::
