---
schema: qual/card@1
id: E-5I2NN
kind: exercise
title: Using the estimates
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Fixed Points
  - Blaschke Factors
relations: []
review: draft
solved: true
---

:::{.exercise title="Using the estimates"}
Let $f\in \Hol(\DD)$.
Show that if $f$ has a fixed point $a$ then $\abs{f'(a)} \leq 1$, and that 
\[
\abs{f(0)}^2 + \abs{f'(0)}^2 \leq 1
.\]

:::

:::{.solution}
Set $f(a) = a$ in Schwarz-Pick:
\[
\left|f^{\prime}(a)\right| \leq \frac{1-|f(a)|^{2}}{1-|a|^{2}} \implies 
\abs{f'(a)} \leq {1 - \abs{a}^2 \over 1 - \abs{a}^2} \leq 1
.\]
Set $a=0$:
\[
\left|f^{\prime}(0)\right| \leq \frac{1-|f(0)|^{2}}{1-|0|^{2}} \implies \abs{f'(0)}^2 \leq 1 - \abs{f(0)}^2
.\]
:::
