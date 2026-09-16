---
schema: qual/card@1
id: D-SDMMS
kind: definition
title: Lebesgue number of an open cover
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
Let $(X,d)$ be a metric space and $\mathcal U$ an open [[D-AOJG3|cover]] of $X$.
A real number $\delta>0$ is a \dfn{Lebesgue number} for $\mathcal U$ if every subset $A\subseteq X$ with [[D-B7CYY|diameter]] $\diam(A)<\delta$ is contained in some $U\in\mathcal U$.
:::

::: {.theorem title="Lebesgue number lemma"}
Every open cover of a [[D-EILKJ|compact]] metric space has a Lebesgue number [@Mun00, Lemma 27.5].
:::
