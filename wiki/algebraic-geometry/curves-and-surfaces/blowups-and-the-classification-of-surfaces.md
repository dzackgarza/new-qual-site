---
title: Blowups and the classification of surfaces
order: 7
topics:
- Blowups
- Minimal Models
- Classification of Surfaces
---

# Blowups and the classification of surfaces

Surfaces are classified up to birational equivalence rather than isomorphism, and the reason is a single theorem: every birational map of smooth projective surfaces is a sequence of blowups and blowdowns.
So the invariants that matter are the ones a blowup does not change.

[[FE-SRFBLOW]]

The table of formulas is what gets asked for, and $E^2 = -1$ is the fact the rest follows from.
Note which invariants move and which do not: $K^2$ drops by one and $\rho$ rises by one, while $\chi(\OO)$, $p_g$ and $q$ are untouched.

The strict transform formulas are the tool for resolving plane curve singularities, since blowing up an ordinary $m$-fold point removes $\binom{m}{2}$ from the arithmetic genus — exactly the delta invariant.

[[T-SRFCAST]]

Contractibility is the converse, and it turns a numerical condition into a morphism.
Contracting $(-1)$-curves until none remain produces a minimal surface, and the process terminates because $K^2$ rises each time.

A surface need not have finitely many $(-1)$-curves: $\Bl_n \PP^2$ for $n \geq 9$ has infinitely many.

[[T-SRFZMT]]

Zariski's theorem is the connectedness statement; the factorization of birational maps is what it is used for.

## The surfaces themselves

[[D-SRFRULED]]

Rational and ruled surfaces are the $\kappa = -\infty$ case.
The rationality criterion is worth stating exactly, because $p_g = q = 0$ is not enough — the Enriques surfaces satisfy it and are not rational, and $P_2$ is what separates them.

[[FE-SRFCUBIC]]

The cubic surface is the example that ties the chapter together: a blowup of $\PP^2$ at six points, anticanonically embedded, with its $27$ lines counted by solving $L^2 = L \cdot K = -1$ in $\Pic$.
Each line is a $(-1)$-curve, so each can be contracted, and the many ways of doing so are the symmetry in the configuration.

[[T-SRFKOD]]

The classification then reads as the two-dimensional version of the trichotomy $g = 0$, $g = 1$, $g \geq 2$ for curves.
The row worth rehearsing is $\kappa = 0$, separated by $(p_g, q)$: K3 at $(1,0)$, Enriques at $(0,0)$, abelian at $(1,2)$, bielliptic at $(0,1)$.
