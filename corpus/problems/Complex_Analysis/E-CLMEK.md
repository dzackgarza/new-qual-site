---
schema: qual/card@1
id: E-CLMEK
kind: problem
title: Differentiable contractions are uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is a differentiable contraction, $f$ is uniformly continuous.
:::

::: {.solution}
A contraction is a map $f$ between metric spaces with $d(f(x),f(y))\le c\,d(x,y)$ for some constant $0\le c<1$ and all $x,y$ in its domain.
Differentiability is not used.

::: pf

::: pf-step
$f$ is uniformly continuous.

::: pf-proof
Let $\varepsilon>0$ and put $\delta=\varepsilon$.
If $d(x,y)<\delta$, then $d(f(x),f(y))\le c\,d(x,y)\le d(x,y)<\varepsilon$.
:::

:::

:::

:::
