---
schema: qual/card@1
id: P-27BNG
kind: problem
title: "Suppose $K/F$ is a finite, normal, Galois extension."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Suppose $K/F$ is a finite, normal, Galois extension.

## Part 1

We have $F \leq E \leq K$. Suppose that

- $K / F$ is cyclic, so $\Gal(K / F)$ is a cyclic group,
- $E / F$ is normal


We then want to show that

1.  $E/F$ is cyclic, i.e. $\Gal(E/F)$ is cyclic, and
2.  $K/E$ is cyclic, i.e. $\Gal(K/E)$ is cyclic.

By the fundamental theorem of Galois theory, $E/F$ is normal if and only if

a. $\Gal(K/E) \normal \Gal(K/F)$, and
b. $\Gal(E/F) \cong \Gal(K/F) / \Gal(K/E)$.

Since $\Gal(K/F)$ is a cyclic group and every subgroup of a cyclic group is itself cyclic, (a) lets us conclude that (1) holds.

Similarly, since $\Gal(K/F)$ is a cyclic group and every *quotient* of a cyclic group is cyclic, (b) lets us conclude (2). 

## Part 2

By the Galois correspondence, all intermediate fields will correspond to subgroups of $\Gal(K/F)$.
Since this group is cyclic, we are reduced to analyzing the subgroup lattice of a generic cyclic group.

But if $G = \generators{x \mid x^n = e}$ where $\size G = n$, then there is one and *only* one subgroup of index $d$ and order $\frac{n}{d}$ for every $d$ dividing $n$, given by $H_d \definedas \generators{x^d}$.

So we have $[G: H_d] = d$, so $H_d$ corresponds to a field $E_d/ F$ of degree $d$ where $F \leq E_d \leq K$. 
This can be done for every $d$ dividing $n$, and since $K/F$ is a Galois extension, $n = \abs{\Gal(K/F)} = [K: F]$, and this can be done for every divisor of $[K: F]$ as desired. $\qed$

