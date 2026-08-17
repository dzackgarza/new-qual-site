---
schema: qual/card@1
id: PR-OF7ZW
kind: proposition
title: Equivalent conditions for a finite-dimensional linear operator to be cyclic
classification:
  areas:
  - algebra
  topics:
  - minimal-and-characteristic-polynomials
  - rational-canonical-form
  - structure-theorem
relations: []
review: draft
---

::: {.proposition title="?"}
For a linear operator on a vector space of nonzero finite dimension, TFAE:

- The minimal polynomial is equal to the characteristic polynomial.

- The list of invariant factors has length one.

- The Rational Canonical Form has a single block.

- The operator has a matrix similar to a companion matrix.

- There exists a *cyclic vector* $\vector v$ such that $\spanof_k\theset{T^j \vector v \suchthat j = 0, 1, 2, \cdots} = V.$

**Not** equivalent: "$T$ has $\dim V$ distinct eigenvalues".
That is sufficient but not necessary: a single Jordan block of size $\dim V$ has minimal polynomial equal to its characteristic polynomial and only one eigenvalue.
:::
