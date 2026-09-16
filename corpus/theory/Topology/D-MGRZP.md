---
schema: qual/card@1
id: D-MGRZP
kind: definition
title: Nullhomotopic map
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A continuous map $f\colon X\to Y$ is \dfn{nullhomotopic} if it is [[D-Z7I7F|homotopic]] to a constant map: there are $y_0\in Y$ and a continuous map $F\colon X\times[0,1]\to Y$ with $F(x, 0) = f(x)$ and $F(x, 1) = y_0$ for all $x\in X$.
:::

::: {.proposition}
If $f\colon X\to Y$ is nullhomotopic, then $f_*\colon\tilde H_n(X)\to\tilde H_n(Y)$ is zero for every $n$.
:::

::: {.concept}
See [@Hat02, p. 4 and Theorem 2.10].
:::
