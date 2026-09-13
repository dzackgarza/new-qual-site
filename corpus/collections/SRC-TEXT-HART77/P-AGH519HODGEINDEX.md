---
schema: qual/card@1
id: P-AGH519HODGEINDEX
kind: problem
title: Hodge index inequality and divisors of type $(a,b)$ on a product of curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
relations: []
review: draft
---

::: problem
a. If $H$ is an ample divisor on the surface $X$, and if $D$ is any divisor, show that
\[
\left(D^2\right)\left(H^2\right) \leqslant(D . H)^2 .
\]

b. Now let $X$ be a product of two curves $X=C \times C^{\prime}$.
Let $l=C \times \mathrm{pt}$, and $m=\mathrm{pt} \times C^{\prime}$.
For any divisor $D$ on $X$, let $a=D . l$, $b=D . m$.
Then we say $D$ has type $(a, b)$.
If $D$ has type $(a, b)$, with $a, b \in \ZZ$, show that
\[
D^2 \leqslant 2 a b ,
\]
and equality holds if and only if $D \equiv b l+a m$.

Hint: Show that $H=l+m$ is ample, let $E=l-m$, let $D^{\prime}=\left(H^2\right)\left(E^2\right) D-\left(E^2\right)(D \cdot H) H-\left(H^2\right)(D \cdot E) E$, and apply (1.9). This inequality is due to Castelnuovo and Severi.
See Grothendieck [2].
:::
