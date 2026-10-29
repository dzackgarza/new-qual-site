---
schema: qual/card@1
id: P-R9XZL
kind: problem
title: Every maximal ideal is prime, so $\operatorname{MaxSpec}R\subseteq\Spec R$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
Show that $\operatorname{MaxSpec}R\subseteq\operatorname{Spec}R$, and give an example of strict containment and one of equality.
:::

::: {.solution}
::: pf

::: pf-step
$\operatorname{MaxSpec}R\subseteq\Spec R$.

::: pf-proof
If $I$ is a maximal ideal, then $R/I$ is a field, hence an integral domain, so $I$ is prime.
:::

:::

::: pf-step
For $R=\ZZ$ the containment is strict.

::: pf-proof
$(0)$ is prime because $\ZZ$ is a domain, and it is not maximal because $(0)\subsetneq(2)\subsetneq\ZZ$.
:::

:::

::: pf-step
For a field $k$, $\Spec k=\operatorname{MaxSpec}k=\{(0)\}$.

::: pf-proof
The only ideals of $k$ are $(0)$ and $k$, and $(0)$ is maximal.
:::

:::

:::
:::
