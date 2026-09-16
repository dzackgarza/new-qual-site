---
schema: qual/card@1
id: FD-Q3XHG
kind: definition
title: Lebesgue integral of a nonnegative measurable function
prompts:
- How is the Lebesgue integral of $f$ defined from simple functions?
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to[0,\infty]$ be [[D-DHFN4|measurable]].
The \dfn{Lebesgue integral} of $f$ is
$$
\int f \coloneqq \sup \theset{\int \phi \suchthat \phi \text{ a simple function with } 0 \leq \phi \leq f},
$$
where a nonnegative [[D-553MO|simple function]] $\phi=\sum_{j=1}^n c_j\chi_{E_j}$ has integral $\int\phi\coloneqq\sum_{j=1}^n c_j\,\mu(E_j)$.
:::
