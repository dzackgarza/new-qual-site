---
title: Cohomology of projective schemes
order: 4
topics:
- Coherent Sheaves
- Vanishing Theorems
- Euler Characteristic
---

# Cohomology of projective schemes

[[T-COHFIN]]

[[T-COHSVAN]]

For $X$ projective over a field $k$ and $\mcf$ coherent, the two theorems give finite numbers $h^i(X,\mcf(n))=\dim_kH^i(X,\mcf(n))$ and $\chi(X,\mcf(n))=h^0(X,\mcf(n))$ for $n\ge n_0$.
The threshold $n_0$ depends on $\mcf$: $H^1(\PP^1_k,\OO(-m)(m-2))\cong H^1(\PP^1_k,\OO(-2))\cong k$ for every $m\ge0$, so no single $n_0$ serves all the sheaves $\OO_{\PP^1_k}(-m)$.

## Euler characteristic and Hilbert polynomial

[[D-COHEULER]]

[[T-COHFLATCHI]]

For $f\colon X\to T$ projective with $T$ noetherian and $\mcf$ coherent on $X$ and flat over $T$, each $h^i(X_t,\mcf_t)$ is upper semicontinuous in $t$ and $\chi(X_t,\mcf_t)$ is locally constant ([[T-COHBC]]).
For a finitely generated graded $k$-algebra $S$ generated in degree one and a finite graded $S$-module $M$, the sheaf $\mcf=\widetilde M$ on $\Proj S$ has $\chi(\mcf(n))$ equal to the Hilbert polynomial of $M$ ([[algebraic-geometry/varieties/dimension-and-degree|dimension and degree]]) at every integer $n$.
Over an integral noetherian base, [[T-COHFLATCHI]] gives the converse to local constancy: a coherent sheaf on $\PP^n_T$ whose fibres all have the same Hilbert polynomial is [[algebraic-geometry/morphisms/finite-and-flat|flat]] over $T$.
