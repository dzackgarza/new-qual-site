---
schema: qual/card@1
id: D-V6UQJ
kind: definition
title: Analytic function
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $f\colon\Omega\to\CC$, and let $z_0\in\Omega$.
The function $f$ is \dfn{analytic} at $z_0$ if there exist a power series $\sum_{n\ge0}a_n(z-z_0)^n$ with radius of convergence $R>0$ and an open neighborhood $U\subseteq\Omega$ of $z_0$ with $\abs{z-z_0}<R$ for all $z\in U$, such that
$$
f(z)=\sum_{n\ge0}a_n(z-z_0)^n\qquad\text{for all } z\in U.
$$
The function $f$ is analytic on $\Omega$ if it is analytic at every point of $\Omega$.
:::

::: {.remark}
The book's definition is [@Ahl73, ch. 2, §1.2, Analytic Functions]: the analytic functions are those that possess a derivative wherever they are defined, and the term holomorphic is used there with the same meaning. The definition above is equivalent to it. A power series represents an analytic function in its disc of convergence, and may be differentiated termwise there, by [@Ahl73, ch. 2, §2.4, Theorem 2], which is the direction from the series to the derivative. Conversely an analytic function is represented by its Taylor series in the largest open disc about the point that lies in its region, by [@Ahl73, ch. 5, §1.2, Theorem 3], which is the direction from the derivative to the series; the neighbourhood $U$ of the definition may therefore be taken to be that disc.
:::
