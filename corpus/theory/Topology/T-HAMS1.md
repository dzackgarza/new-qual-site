---
schema: qual/card@1
id: T-HAMS1
kind: theorem
title: Ham sandwich theorem
slogan: 'One hyperplane bisects $n$ compact sets in $\RR^n$ at once.'
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fixed Points
relations: []
review: draft
---

::: {.theorem}
Let $A_1,\ldots,A_n\subseteq\RR^n$ be compact.
Then there is an affine hyperplane $P$ that divides each $A_i$ into two pieces of equal $n$-dimensional measure.
:::

::: {.remark}
For $n=3$ this is [@Hat02, §1.1 Exercise 9].
In general it is the standard consequence of Borsuk--Ulam [@Hat02, Corollary 2B.7], applied to the volumes $\vol(A_i\intersect V_\lambda)$ of the half-spaces $V_\lambda=\theset{x\in\RR^n\st\inner{\lambda}{(x,1)}\geq 0}$ for $\lambda\in S^n$.
:::
