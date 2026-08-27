---
schema: qual/card@1
id: D-ZJJ7G
kind: definition
title: Torsion and torsionfree
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
---

::: {.definition}
An element $m\in M$ is a **torsion element** if there exists a nonzero $r\in R$ such that $rm = 0_M$.
A module \( M \) is **torsion-free** if and only if for every \( x\in M \), \( mx = 0_M \implies m=0_M \), i.e. $M$ has no nonzero torsion elements.
Equivalently, defining $M_t \da \ts{ m\in M \st \exists r\in R, rm = 0_M }$ as the set of all torsion elements, $M$ is torsion free iff $M_t = 0$.
If $M_t = M$, we say $M$ is a **torsion module**.
:::
