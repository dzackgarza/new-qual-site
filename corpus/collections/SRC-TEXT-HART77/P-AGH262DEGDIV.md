---
schema: qual/card@1
id: P-AGH262DEGDIV
kind: problem
title: Degrees of divisors on subvarieties of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisor Class Groups
  - Intersection Multiplicity
  - Bezout's Theorem
relations: []
review: draft
---

::: problem
Let $k$ be an algebraically closed field, and let $X$ be a closed subvariety of $\PP^n_k$ which is nonsingular in codimension one.
For any divisor $D = \sum n_i Y_i$ on $X$, define the **degree** of $D$ to be $\sum n_i \deg Y_i$, where $\deg Y_i$ is the degree of $Y_i$ considered as a projective variety itself.

a. Let $V$ be an irreducible hypersurface in $\PP^n$ which does not contain $X$, and let $Y_i$ be the irreducible components of $V \intersect X$; they all have codimension $1$.
   For each $i$, let $f_i$ be a local equation for $V$ on some open set $U_i$ of $\PP^n$ with $Y_i \intersect U_i \neq \emptyset$, and let $n_i = v_{Y_i}(\bar f_i)$, where $\bar f_i$ is the restriction of $f_i$ to $U_i \intersect X$.

   Define the divisor $V . X$ to be $\sum n_i Y_i$.
   Extend by linearity, and show that this gives a well-defined homomorphism from the subgroup of $\Div \PP^n$ consisting of divisors none of whose components contain $X$, to $\Div X$.

b. If $D$ is a principal divisor on $\PP^n$ for which $D . X$ is defined as in (a), show that $D . X$ is principal on $X$.
   Thus we get a homomorphism $\Cl \PP^n \to \Cl X$.

c. Show that the integer $n_i$ defined in (a) is the same as the intersection multiplicity $i(X, V; Y_i)$.
   Then use the generalized Bezout theorem to show that for any divisor $D$ on $\PP^n$ none of whose components contain $X$,
\[
\deg(D . X) = (\deg D)(\deg X)
.\]

d. If $D$ is a principal divisor on $X$, show that there is a rational function $f$ on $\PP^n$ such that $D = (f) . X$.
   Conclude that $\deg D = 0$, so the degree function defines a homomorphism $\deg: \Cl X \to \ZZ$.
   Finally, the square formed by $\Cl \PP^n \to \Cl X$, by the degree isomorphism $\Cl \PP^n \to \ZZ$, by $\deg: \Cl X \to \ZZ$, and by multiplication by $\deg X$ on $\ZZ$ commutes.
   In particular, the map $\Cl \PP^n \to \Cl X$ is injective.
:::
