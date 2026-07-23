---
schema: qual/card@1
id: E-JLDSM
kind: exercise
title: "Using the estimates"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Using the estimates"}
Does there exist a map $f: \DD\to \DD$ with

- $f\qty{1\over 2} = {3\over 4}$
- $f'\qty{1\over 2} = {2\over 3}$

#complex/exercise/completed

:::

:::{.solution}
Apply Schwarz-Pick:
\[
\abs{f'\qty{1\over 2} } \leq {1 - \abs{f\qty{1\over 2}}^2 \over 1 - \abs{1\over 2}^2 } = {7\over 2}< {2\over 3}
,\]
so this is not possible.
:::
