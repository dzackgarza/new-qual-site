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

::: solution
By definition, a contraction satisfies
\[
d(f(x),f(y))\le c\,d(x,y)
\]
for some constant $0\le c<1$ and for all $x,y$ in its domain. Thus $f$ is
Lipschitz. Given $\varepsilon>0$, if $c=0$ then $f$ is constant; otherwise
take $\delta=\varepsilon/c$. Whenever $d(x,y)<\delta$,
\[
d(f(x),f(y))\le c\,d(x,y)<\varepsilon.
\]
Therefore $f$ is uniformly continuous. Differentiability is not needed.
:::
