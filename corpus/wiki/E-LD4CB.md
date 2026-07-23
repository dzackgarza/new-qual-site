---
schema: qual/card@1
id: E-LD4CB
kind: exercise
title: "Show that $\\sum_{k\\geq 0}z^k/k!$ converges locally uniformly to $e^z$."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that $\sum_{k\geq 0}z^k/k!$ converges locally uniformly to $e^z$.

#complex/exercise/completed

:::

:::{.solution}
Apply the $M\dash$test on a compact set $K$ with $z\in K \implies \abs{z} \leq M$:
\[
\norm{e^z - \sum_{0\leq k \leq n} z^k/k!}_\infty 
&= \norm{\sum_{k\geq n+1}z^k/k! }_{\infty} \\
&\leq \sum_{k\geq n+1} \norm{z}_\infty^k /k! \\
&\leq \sum_{k\geq 0} \norm{z}_\infty^k /k! \\
&= e^{\norm{z}_\infty} \\
&\leq e^{\abs{M}} \\
&< \infty
.\]


:::

