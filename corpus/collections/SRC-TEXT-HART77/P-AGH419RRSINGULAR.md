---
schema: qual/card@1
id: P-AGH419RRSINGULAR
kind: problem
title: Riemann-Roch for singular curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Canonical Divisor
  - Very Ample Divisors
  - Genus
relations: []
review: draft
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$.
Let $X_{\reg}$ be the set of regular points of $X$.

a. Let $D=\sum n_i P_i$ be a divisor with support in $X_{\reg}$, i.e., all $P_i \in X_{\reg}$.
Then define $\deg D=\sum n_i$.
Let $\mcl(D)$ be the associated invertible sheaf on $X$, and show that
$$
\chi(\mcl(D))=\deg D+1-p_a .
$$

b. Show that any Cartier divisor on $X$ is the difference of two very ample Cartier divisors.
Use (II, Ex.
7.5).

c. Conclude that every invertible sheaf $\mcl$ on $X$ is isomorphic to $\mcl(D)$ for some divisor $D$ with support in $X_{\reg}$.

d. Assume furthermore that $X$ is a locally complete intersection in some projective space.
Then by (III, 7.11) the dualizing sheaf $\omega_X$ is an invertible sheaf on $X$, so we can define the canonical divisor $K$ to be a divisor with support in $X_{\reg}$ corresponding to $\omega_X$.
Then the formula of a. becomes
$$
l(D)-l(K-D)=\deg D+1-p_a
$$
:::
