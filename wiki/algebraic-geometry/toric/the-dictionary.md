---
title: The fan dictionary
order: 1
topics:
- Toric Varieties
- Fans
- Orbits
---

# The fan dictionary

Toric geometry earns a place on a revision list for one reason: it is the corner of the subject where every question above becomes a finite computation with lattice points, so it is the fastest source of an example when an examiner asks for one.

[[D-Q7Q2N]]

[[PR-O8V3I]]

[[PR-D2F15]]

## Orbit closures are toric too

[[D-FULSTAR]]

The orbit-cone correspondence lists the orbits; the star fan identifies each closure as a toric variety in its own right.
That is what makes induction on dimension available: a statement about $X_\Sigma$ can be tested on the boundary divisors $D_\rho = X_{\Star(\rho)}$, which are toric varieties one dimension down.

## What to reach for, and when

| Asked for | Fan that supplies it |
| --- | --- |
| a normal variety that is not smooth | cone on $(0,1)$, $(d,-1)$ for $d \geq 2$ |
| a Weil divisor that is not Cartier | the same, $d = 2$: the quadric cone $V(xy - z^2)$ |
| a class group with torsion | the same: $\Cl = \ZZ/d$ |
| a resolution, explicitly | subdivide by inserting the missing lattice rays |
| a proper variety that is not projective | a complete fan that admits no strictly convex support function |

Every entry is checked by a computation on a two-dimensional picture, which is why the answers arrive faster from here than from anywhere else in the tree.

The cost is that the dictionary only covers toric varieties, and an examiner who wants a general argument will not accept a fan.
Use it to *find* the example, then state the example in the language the question was asked in.
