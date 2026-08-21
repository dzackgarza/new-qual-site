---
schema: qual/card@1
id: P-FPMMA
kind: problem
title: The gradient of $xy$ is orthogonal to its level curves
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
relations: []
review: draft
solved: true
---

::: problem
Let $f(x,y) = xy$.
Show that $\nabla f$ is orthogonal to the level curves of $f$.
:::

::: {.solution}
$\nabla f = (y, x)$.
Along a level curve $f(x,y) = c$ one may take a parametrization $\gamma$ with $f(\gamma(t)) = c$, so $\frac{d}{dt}f(\gamma(t)) = 0$.
By the chain rule this inner product is $\langle \nabla f(\gamma(t)), \gamma'(t)\rangle$, hence $\nabla f$ is orthogonal to every tangent of the level curve.

![](../../assets/00_Prelims/figures/2019-06-16-23-42-19.png)
:::
