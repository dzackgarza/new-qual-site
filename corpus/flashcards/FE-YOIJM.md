---
schema: qual/card@1
id: FE-YOIJM
kind: example
title: Is a composition of Lebesgue measurable functions measurable?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Cantor Set
  - Counterexamples
relations: []
review: draft
---

::: {.example}
No:

- Take $f: [0, 1]\to [0, 1]$ the Cantor-Lebesgue function (monotonic and cts) and $C$ the Cantor set
- $f(C) = [0, 1]$, so define $g(x) = f(x) +x$ so $g:[0, 1] \to [0, 2]$ (strictly monotonic and cts, so a homeomorphism), so $g\inv$ is cts and thus measurable.
- $\mu(g(C)) = 1>0$ (because $f$ is constant on every interval in $C^c$) so $g(C) \supseteq A$ a non-measurable subset
- $g\inv(A) \subset C$ with $\mu(C) = 0$ implies $g\inv(A)$ is a measurable set, so $\chi_{g\inv(A)}$ is a measurable function
- Then $k\definedas \chi_{g\inv(A)} \circ g\inv$ isn't measurable since 
  $$ 
  k\inv(1) = \qty{ (g\inv)\inv \circ \chi_{g\inv(A)} }(1) = g(g\inv(A)) = A
  $$
  is not a measurable set.
:::
