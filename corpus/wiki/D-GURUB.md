---
schema: qual/card@1
id: D-GURUB
kind: definition
title: "Ring"
classification:
  areas:
  - algebra
  topics:
  - rings
relations: []
review: draft
---

::: {.definition title="Ring"}
A **ring** is a triple $(R, +, \cdot) \in \Ring$ such that

- $(R, +)\in \Ab\Grp$,

- $(R, \cdot) \in \Monoid$

- Distributivity: $a(b+c) = ab + ac$ and $(b+c)a = ba + ca$.

A ring is **commutative**, i.e. an object of $\CRing$, iff additionally $ab = ba$ for all $a, b\in R$.
:::
