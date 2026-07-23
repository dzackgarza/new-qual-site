---
schema: qual/card@1
id: P-X7AK4
kind: problem
title: "If $L/K$ is a finite field extension which is both separable and a spl\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
If $L/K$ is a finite field extension which is both separable and a splitting field of some polynomial in $K[x]$, then $[L: K] = \abs{\Gal}{L/ K}$.

### Part 2

The extension $\QQ(\zeta_{43})$ is the splitting field of the cyclotomic polynomial $\Phi_{43}(x) = \sum_{i=1}^42 x^i$, which is degree $\phi(43) = 42$ since $43$ is prime.

Moreover, the Galois group is isomorphic to $\ZZ_{43}\units \cong \ZZ_{42}$.

### Part 3

Since proper subfields will correspond to intermediate extensions which will correspond to subgroups of the Galois group, this problem is reduced to counting the number of distinct subgroups of $\ZZ_{42}$.
This is a cyclic group, so there is exactly one subgroup of order $d$ for each $d$ dividing 42. Since $42 = 2*3*7$, we have

- A subgroup of order 2, corresponding to a field extension of degree 21,
- A subgroup of order 3, corresponding to a field extension of degree 14,
- A subgroup of order 6, corresponding to a field extension of degree 7,
- A subgroup of order 7, corresponding to a field extension of degree 6,
- A subgroup of order 14, corresponding to a field extension of degree 3,
- A subgroup of order 21, corresponding to a field extension of degree 2.

## Problem 2
