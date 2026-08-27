---
schema: qual/card@1
id: FD-F3UU4
kind: definition
title: Uniform Convergence of a sequence of functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
$\theset{f_n} \converges{u}\to f$ on $E$ iff for every $\varepsilon>0$ that exists an $N(\varepsilon)$ such that for all $n\geq N$ and for all $x\in E$, $\abs{f_n(x) - f(x)} < \varepsilon$.
Equivalently, $\norm{f_n - f}_\infty \definedas \sup_{x\in E}\abs{f_n(x) - f(x)} < \varepsilon$.
:::
