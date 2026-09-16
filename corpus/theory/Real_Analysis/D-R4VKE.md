---
schema: qual/card@1
id: D-R4VKE
kind: definition
title: Lebesgue integral of a nonnegative function
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space.
For a nonnegative [[D-553MO|simple function]] $s = \sum_{j=1}^n c_j \chi_{E_j}$ with $c_j\in[0,\infty)$ and $E_j\in\mcm$, put
$$
\int_X s \dmu \coloneqq \sum_{j=1}^n c_j \mu(E_j),
$$
with the convention $0\cdot\infty=0$.
For $f\in$ [[D-BF5L2|$L^+$]], the \dfn{Lebesgue integral} of $f$ is
$$
\int_X f \dmu \coloneqq \sup \theset{ \int_X s \dmu \suchthat s \text{ simple and } 0\leq s \leq f }.
$$
:::
