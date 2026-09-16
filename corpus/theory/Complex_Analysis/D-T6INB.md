---
schema: qual/card@1
id: D-T6INB
kind: definition
title: Complex powers $z^\alpha$ along a branch of the logarithm
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC\setminus\{0\}$ be open.
A \dfn{branch of the logarithm} on $\Omega$ is a continuous function $L\colon\Omega\to\CC$ with $e^{L(z)}=z$ for all $z\in\Omega$.
For such $L$ and $\alpha\in\CC$, the \dfn{branch of $z^\alpha$} determined by $L$ is
$$
z^\alpha\coloneqq e^{\alpha L(z)},\qquad z\in\Omega.
$$
:::

::: {.remark}
When no branch is specified, $L$ is the [[D-4CSPM|principal branch]] $\Log$ on $\CC\setminus(-\infty,0]$.
:::
