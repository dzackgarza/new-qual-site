---
schema: qual/card@1
id: E-FUIDU
kind: problem
title: Using the estimates
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
  - Counterexamples
relations: []
review: draft
---

:::{.exercise}
Does there exist a map $f: \DD\to \DD$ with

- $f\qty{1\over 2} = {3\over 4}$
- $f'\qty{1\over 2} = {2\over 3}$

:::

:::{.solution}
Apply Schwarz-Pick:
\[
\abs{f'\qty{1\over 2} } \leq {1 - \abs{f\qty{1\over 2}}^2 \over 1 - \abs{1\over 2}^2 } = {7\over 2}< {2\over 3}
,\]
so this is not possible.
:::
