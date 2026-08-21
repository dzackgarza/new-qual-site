---
schema: qual/card@1
id: PR-TLPVU
kind: proposition
title: Converting between elementary divisors and invariant factors
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.proposition title="Converting between elementary divisors and invariant factors"}
Given any presentation of a group as a product of cyclic groups $G = \prod \ZZ_i/m_i$, with the $m_i$ not necessarily distinct,

- Factor all of the $m_i$ into prime powers, keeping the exponents intact.

- Organize into a table whose columns correspond to individual primes $p_i$.

  - Within an individual column for the prime $p_k$, write all terms of the form $p_k^{e_k}$ (with exponents intact)

  - Arrange the terms from lowest at the top to highest at the bottom.
    Push everything down so that the bottom-most rows are all filled out.

- For **elementary divisors**, just list out all of elements of the table individually, running across rows.

- For **invariant factors**, iterate a process of taking the largest of each prime power (i.e. the bottom row) at each step, deleting that row, and continuing in the same fashion.

> Note: this sounds much more complicated than it actually is.
> Try it!
:::
