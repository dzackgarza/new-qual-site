---
schema: qual/card@1
id: FD-BACTZ
kind: definition
title: Essential singularity and the limit at the singularity
prompts:
- What is an essential singularity?
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$.
The [[D-IWIA5|isolated singularity]] $z_0$ is an \dfn{essential singularity} of $f$ if it is neither a [[D-BQLJV|removable singularity]] nor a [[D-AUD6K|pole]].
:::

::: {.proposition}
The isolated singularity $z_0$ is essential if and only if $\lim_{z\to z_0}f(z)$ does not exist in $\CC$ and $\abs{f(z)}\not\to\infty$ as $z\to z_0$.
:::

::: {.proof}
If $z_0$ is removable, $f$ agrees near $z_0$ with a holomorphic $g$, so $f(z)\to g(z_0)\in\CC$; if $z_0$ is a pole, $\abs{f(z)}\to\infty$ by the proposition on [[D-AUD6K]].
Conversely, if $f(z)$ has a limit in $\CC$, then $f$ is bounded near $z_0$ and $z_0$ is removable by [[D-BQLJV|Riemann's removable singularity theorem]]; if $\abs{f(z)}\to\infty$, then $z_0$ is a pole by the proposition on [[D-AUD6K]].
:::
