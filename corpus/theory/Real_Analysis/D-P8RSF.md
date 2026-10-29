---
schema: qual/card@1
id: D-P8RSF
kind: definition
title: $\sigma$-algebras and measurable spaces
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $X$ be a set.
A \dfn{$\sigma$-algebra} on $X$ is a collection $\mcm$ of subsets of $X$ such that $X\in\mcm$, $E^c\in\mcm$ whenever $E\in\mcm$, and $\bigcup_{j\geq1}E_j\in\mcm$ whenever $E_j\in\mcm$ for all $j$.
A \dfn{measurable space} is a pair $(X,\mcm)$ with $\mcm$ a $\sigma$-algebra on $X$.
:::

::: {.remark}
By De Morgan's laws, a $\sigma$-algebra is also closed under countable intersections.
:::
