---
schema: qual/card@1
id: FD-D2QPH
kind: definition
title: Limit definition of exponential function
prompts:
- What is the limit definition of $e^x$?
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
---

::: {.definition}
The \dfn{exponential function} $\RR\to\RR$, $x\mapsto e^x$, is given by
$$
e^x \coloneqq \lim_{n \to \infty} \qty{1 + \frac{x}{n}}^n,
$$
the limit existing for every $x\in\RR$.
:::
