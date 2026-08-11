---
schema: qual/card@1
id: P-7DZQQ
kind: problem
title: "By the Galois correspondence, all intermediate fields will correspond\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

By the Galois correspondence, all intermediate fields will correspond to subgroups of $\Gal(K/F)$.
Since this group is cyclic, we are reduced to analyzing the subgroup lattice of a generic cyclic group.

But if $G = \generators{x \mid x^n = e}$ where $\size G = n$, then there is one and *only* one subgroup of index $d$ and order $\frac{n}{d}$ for every $d$ dividing $n$, given by $H_d \definedas \generators{x^d}$.

So we have $[G: H_d] = d$, so $H_d$ corresponds to a field $E_d/ F$ of degree $d$ where $F \leq E_d \leq K$.
This can be done for every $d$ dividing $n$, and since $K/F$ is a Galois extension, $n = \abs{\Gal(K/F)} = [K: F]$, and this can be done for every divisor of $[K: F]$ as desired.
$\qed$
