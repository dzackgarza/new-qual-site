---
schema: qual/card@1
id: E-P7SIB
kind: problem
title: $\cos 4\theta$ in terms of $\sin\theta$ and $\cos\theta$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Find an identity for $\cos(4\theta)$ in terms of $\sin(\theta)$ and $\cos(\theta)$.
:::

::: {.solution}

Write $x=\cos(\theta)$ and $y= \sin(\theta)$, so $e^{i\theta} = x+iy$.

::: pf

::: {.pf-step #expand}
$\cos(4\theta) + i\sin(4\theta) = (x^4 - 6x^2y^2 + y^4) + i(4x^3y - 4xy^3)$.

::: pf-proof
By de Moivre's formula and the binomial theorem,
$$
\cos(4\theta) + i\sin(4\theta) = e^{4i\theta} = (x+iy)^4 = \sum_{k=0}^{4} \binom{4}{k} x^{4-k} (iy)^{k} = x^4 + 4ix^3y - 6x^2y^2 - 4ixy^3 + y^4.
$$
:::

:::

::: pf-step
$\boxed{\cos(4\theta) = \cos^4(\theta) - 6\cos^2(\theta)\sin^2(\theta) + \sin^4(\theta)}$.

::: pf-proof
Take real parts in step [](#expand){.pf-ref}; $x$ and $y$ are real.
:::

:::

:::

:::
