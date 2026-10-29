---
schema: qual/card@1
id: D-HWLVG
kind: definition
title: Valuation ring
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Integral Domains
  - Localization
relations: []
review: draft
---

::: {.definition}
An [[D-QJ3QL|integral domain]] $R$ with [[D-OXIVT|field of fractions]] $K$ is a \dfn{valuation ring} if for every nonzero $x\in K$, $x\in R$ or $x^{-1} \in R$.
:::

::: {.definition title="Valuation"}
Let $K$ be a field and $G$ a totally ordered abelian group.
A \dfn{valuation} of $K$ with values in $G$ is a group homomorphism $v \colon K^\times \to G$ such that $v(x+y) \geq \min(v(x), v(y))$ for all $x, y \in K^\times$ with $x + y \neq 0$.
The valuation is \dfn{discrete} if $v$ maps $K^\times$ onto $\ZZ$.
[@Har10a, §I.6]
:::

::: {.proposition}
For a valuation $v$ of $K$, the ring $R_v=\theset{x \in K^\times \st v(x) \geq 0} \cup \theset{0}$ is a valuation ring with fraction field $K$. Conversely, every valuation ring $R$ with fraction field $K$ is $R_v$ for the valuation $v\colon K^\times\to K^\times/R^\times$, where $K^\times/R^\times$ is ordered by $xR^\times\le yR^\times$ if and only if $y/x\in R$.
[@AM18, Chapter 5, Exercise 31]
:::
