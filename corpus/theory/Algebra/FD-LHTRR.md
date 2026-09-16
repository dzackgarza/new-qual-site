---
schema: qual/card@1
id: FD-LHTRR
kind: definition
title: Splitting field of a polynomial
prompts:
- What is the splitting field of a polynomial $f \in k[x]$?
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Polynomials
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
Let $k$ be a [[D-UI6CU|field]] and $f\in k[x]$ a nonzero polynomial.
A \dfn{splitting field} of $f$ over $k$ is a field extension $F/k$ such that $f$ splits into linear factors in $F[x]$ and $f$ does not split into linear factors in $E[x]$ for any proper subfield $E\subsetneq F$ containing $k$.
:::

::: {.remark}
Equivalently, $f$ splits in $F[x]$ as $f=c\prod_{i=1}^n(x-\alpha_i)$ and $F=k(\alpha_1,\ldots,\alpha_n)$: a subfield of $F$ containing $k$ over which $f$ splits contains every root $\alpha_i$, and $k(\alpha_1,\ldots,\alpha_n)$ is such a subfield.
:::
