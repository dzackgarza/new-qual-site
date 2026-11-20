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

This is the construction of [@SS03, ch. 3, §6, The complex logarithm], which after defining a logarithm on a simply connected domain defines $z^\alpha=e^{\alpha\log z}$ there, with $\log 1=0$; the card states it for an arbitrary branch $L$ rather than the one normalised at $1$, which gives the same family of branches.
:::

::: {.remark}
When no branch is specified, $L$ is the [[D-4CSPM|principal branch]] $\Log$ on $\CC\setminus(-\infty,0]$.
:::
