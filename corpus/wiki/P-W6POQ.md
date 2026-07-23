---
schema: qual/card@1
id: P-W6POQ
kind: problem
title: "Show that $P(z) \\da z^4 + 6z + 3$ has 3 zeros in $\\ts{1\\leq \\abs{z} \\l\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that $P(z) \da z^4 + 6z + 3$ has 3 zeros in $\ts{1\leq \abs{z} \leq 2}$.

#complex/exercise/completed

:::

:::{.solution}
\envlist

- Take $P(z) = z^4 + 6z + 3$.
- On $\abs{z} < 2$:
  - Set $f(z) = z^4$ and $g(z) = 6z + 3$, then $\abs{g(z)} \leq 6\abs{z} + 3 = 15 < 16= \abs{f(z)}$.
  - So $P$ has 4 zeros here.
- On $\abs{z} < 1$:
  - Set $f(z) = 6z$ and $g(z) = z^4 + 3$.
  - Check $\abs{g(z)} \leq \abs{z}^4 + 3 = 4 < 6 = \abs{f(z)}$.
  - So $P$ has 1 zero here.
:::
