---
title: Special divisors and the canonical map
order: 3
topics:
- Special Divisors
- Hyperelliptic Curves
- Linear Systems
- Complete Intersections
---

# Special divisors and the canonical map

Riemann--Roch is an equation with an unknown in it.
The unknown is $\ell(K-D)$, and everything interesting about a curve is hidden there.

[[D-CRVSPEC]]

Once $\deg D > 2g-2$ the unknown vanishes and $\ell(D)$ is a formula.
Below that threshold Riemann--Roch gives only an inequality, and the divisors that make the inequality strict are the ones that carry geometry.

[[T-CRVCLIFF]]

Clifford supplies the missing upper bound, and its equality cases name the only curves with unusually large special systems.
That is the pattern to expect: a bound whose extremal case is hyperelliptic.

## Counting maps to $\PP^1$

[[D-CRVGON]]

The $g^r_d$ notation is how the question gets asked, so it is worth translating on sight: a $g^1_2$ is a degree-two map to $\PP^1$, a $g^1_3$ makes the curve trigonal, and the canonical system on a non-hyperelliptic curve is a $g^{g-1}_{2g-2}$.

[[D-CRVHYP]]

The hyperelliptic case is the exception in the statement of almost every theorem here, and it is always the same picture underneath: the canonical map is two-to-one onto a rational normal curve rather than an embedding.

## The curves one can actually name

[[FE-CRVLOWG]]

An examiner asking about genus $2$, $3$ or $4$ wants the model, not a general theorem.
Genus $3$ is the plane quartic, genus $4$ is the intersection of a quadric and a cubic in $\PP^3$, and genus $2$ has no canonical embedding at all because every such curve is hyperelliptic.

## What the canonical class rules out

[[PR-CRVHYPCI]]

Genus $4$ is the case to hold next to this one: the canonical curve there *is* a complete intersection, and the formula $\omega_C \cong \OO_C(\sum d_i - n - 1)$ is what makes both statements the same computation.
