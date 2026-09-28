---
schema: qual/card@1
id: FR-6AHGM
kind: proof
title: If $\int\abs{f}\,d\mu = 0$ then $f = 0$ almost everywhere
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to\CC$ be [[D-DHFN4|measurable]] with $\int_X \abs{f}\dmu = 0$.
Then $f = 0$ $\mu$-almost everywhere.
:::

::: {.proof}
For each $n \geq 1$ put $E_n \coloneqq \theset{x\in X \suchthat \abs{f(x)} \geq \frac1n}\in\mcm$.
On $E_n$ we have $\abs{f} \geq \frac1n$, so
$$
0 = \int_X \abs{f}\dmu \geq \int_{E_n} \abs{f}\dmu \geq \int_{E_n} \frac1n\dmu = \frac1n \mu(E_n),
$$
and hence $\mu(E_n) = 0$ for every $n$.
Now $\theset{x\in X \suchthat f(x) \neq 0} = \bigcup_{n \geq 1} E_n$ is a countable union of null sets, hence null.
Therefore $f = 0$ almost everywhere.
:::
