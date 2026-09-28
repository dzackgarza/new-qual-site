---
title: Line bundles and linear systems
order: 2
topics:
- Invertible Sheaves
- Linear Systems
- Base Locus
---

# Line bundles and linear systems

[[D-DIVOD]]

[[PR-DIVLB]]

A Cartier divisor $D$ gives the invertible sheaf $\OO(D)$ with the rational section $1$, and an invertible sheaf $\mcl$ with a nonzero global section $s$ gives the effective divisor $\operatorname{div}(s)$, its zero locus.
Linear equivalence of divisors corresponds to isomorphism of invertible sheaves, because changing the section by a rational function $f$ changes the divisor by $\operatorname{div}f$.

## From sections to a map

[[D-DIVLINSYS]]

[[T-DIVMAPPN]]

For a basis $s_0,\ldots,s_n$ of a linear system $V\subseteq H^0(X,\mcl)$, the morphism sends $x$ to $[s_0(x):\cdots:s_n(x)]$, with the values taken in a trivialization of $\mcl$ near $x$.
It is defined exactly off the base locus of $V$; for $X$ projective over an algebraically closed field, it is a closed immersion exactly when $V$ separates points and tangent vectors.

On a smooth projective curve $C$ of genus $g$, $\abs{D}$ is base-point free exactly when $\ell(D-p)=\ell(D)-1$ for every point $p$, and very ample exactly when $\ell(D-p-q)=\ell(D)-2$ for all points $p,q$; Riemann--Roch gives $\ell(D-E)=\deg(D-E)+1-g$ whenever $\deg(D-E)>2g-2$.
