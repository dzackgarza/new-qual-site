---
schema: qual/card@1
id: E-1FRQL
kind: exercise
title: Thomae-type function continuous at each irrational
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Let $g: \mathbb{Z}_+ \to \mathbb{Q}$ be a bijective function; let $x_n = g(n)$.
Define $f: \mathbb{R} \to \mathbb{R}$ as follows:

$$
\begin{array}{ll}
f(x_n) = 1/n & \text{for } x_n \in \mathbb{Q}, \\
f(x) = 0 & \text{for } x \notin \mathbb{Q}.
\end{array}
$$

Show that $f$ is continuous at each irrational and discontinuous at each rational.
Can you find a sequence of continuous functions $f_n$ converging to $f$?
:::
