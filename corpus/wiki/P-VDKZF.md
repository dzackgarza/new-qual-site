---
schema: qual/card@1
id: P-VDKZF
kind: problem
title: An entire function omitting a bounded open set is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
relations: []
review: draft
---

::: {.problem title="?"}
Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded* open set $\Omega$.
Show without using Picard's theorems that $f(z)$ is a constant.
:::

::: {.solution}
Choose $w_0 \in \Omega$ and $\varepsilon > 0$ with $\overline{D_\varepsilon(w_0)} \subseteq \Omega$.
Then $\abs{f(z) - w_0} \geq \varepsilon$ for every $z$, so $g(z) \da 1/(f(z)-w_0)$ is entire and bounded by $1/\varepsilon$.
By Liouville, $g$ is constant, hence $f$ is constant.
:::
