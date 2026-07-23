---
schema: qual/card@1
id: E-QKXE7
kind: exercise
title: "Expanding Laurent series in different regions"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Expanding Laurent series in different regions"}
Expand $f(z) = {1\over z(z-1)}$ in both

- $\abs{z} < 1$
- $\abs{z} > 1$

#complex/exercise/completed

:::

:::{.solution}
\[
{1\over z(z-1)} = -{1\over z}{1 \over 1-z} = -{1\over z}\sum z^k
.\]
and
\[
{1\over z(z-1)} = {1\over z^2(1 - {1\over z})} = {1\over z^2} \sum \qty{1\over z}^k
.\]
:::

