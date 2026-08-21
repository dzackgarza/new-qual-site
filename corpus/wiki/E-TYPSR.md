---
schema: qual/card@1
id: E-TYPSR
kind: exercise
title: An entire function with bounded $n$th derivative is a polynomial of degree
  at most $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Polynomials
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Suppose $f$ is entire and $f^{(n)}$ is bounded on $\CC$.
Show that $f$ is a polynomial of degree at most $n$.
:::

::: {.solution}
By Liouville or MMP, $f^{(n)}$ is bounded and entire and thus constant.
Integrating a constant $n$ times yields a polynomial of degree t most $n$.
:::
