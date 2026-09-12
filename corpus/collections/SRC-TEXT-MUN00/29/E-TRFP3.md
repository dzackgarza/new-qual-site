---
schema: qual/card@1
id: E-TRFP3
kind: problem
title: Directed sets without antisymmetry
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
---

::: {.exercise}

Check that the preceding exercises remain correct if condition (2) is omitted from the definition of directed set.
Many mathematicians use the term "directed set" in this more general sense.
:::

::: {.solution}
The antisymmetry condition is never used in the constructions involving nets. What is needed is only reflexivity, transitivity, and the directedness condition that every two indices admit a common upper bound.

In particular, the proofs of convergence, subnet convergence, closure detection, and accumulation-point detection use only comparisons of the form \(\alpha\preceq\beta\), passage to common upper bounds, and transitivity. If two distinct indices satisfy both \(\alpha\preceq\beta\) and \(\beta\preceq\alpha\), nothing in any argument changes. Hence all preceding exercises remain valid for directed preorders.
:::
