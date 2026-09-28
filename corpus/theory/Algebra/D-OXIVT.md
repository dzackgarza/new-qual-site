---
schema: qual/card@1
id: D-OXIVT
kind: definition
title: Field of fractions
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Integral Domains
  - Fields
relations: []
review: draft
---

::: {.definition}
Let $R$ be an [[D-QJ3QL|integral domain]].
On $R \times (R\setminus\theset{0})$ define $(a,s)\sim (b, t)$ if $at = bs$, and write $a/s$ for the class of $(a,s)$.
The \dfn{field of fractions} of $R$ is the set of classes
$$
\ff(R) \coloneqq \bigl(R \times (R\setminus\theset{0})\bigr)/{\sim},
$$
with operations $\frac as+\frac bt=\frac{at+bs}{st}$ and $\frac as\cdot\frac bt=\frac{ab}{st}$.
:::

::: {.remark}
Transitivity of $\sim$ uses that $R$ has no nonzero zero divisors: if $at=bs$ and $bu=ct$, then $aut=bsu=cst$, so $t(au-cs)=0$, and $t\neq0$ gives $au=cs$.
The same hypothesis gives $st\neq 0$, so the operations are defined on $R\times(R\setminus\theset{0})$.
:::
