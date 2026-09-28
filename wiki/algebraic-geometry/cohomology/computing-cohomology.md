---
title: Computing cohomology
order: 1
topics:
- Cohomology
- Cech Cohomology
- Twisting Sheaves
---

# Computing cohomology

Sheaf cohomology $H^i(X,-)$ is the $i$th right derived functor of $\Gamma(X,-)$ on sheaves of abelian groups.
For a quasi-coherent sheaf on a noetherian separated scheme, the Čech complex of a finite affine open cover computes it.
The cover of $\PP^n_A$ by the $n+1$ opens $D_+(x_i)$ gives $H^*(\PP^n_A,\OO(d))$ for every $d$.

[[D-PTIW0]]

[[T-IJW1K]]

The shift $-n-1$ in the duality between $H^n(\PP^n,\OO(d))$ and $S_{-d-n-1}$, where $S=A[x_0,\ldots,x_n]$, is the degree of the canonical sheaf $\omega_{\PP^n}=\OO(-n-1)$ of [[../sheaves-of-modules/differentials|differentials]].
The perfect pairing $H^0(\PP^n,\OO(d))\times H^n(\PP^n,\OO(-d-n-1))\to H^n(\PP^n,\OO(-n-1))\cong A$ is [[T-COHSD|Serre duality]] on $\PP^n$.

## $H^1$: lifting sections and line bundles

[[PR-ET5PQ]]

For an exact sequence $0\to\mcf'\to\mcf\to\mcf''\to0$ of sheaves of abelian groups, a section $s\in\Gamma(X,\mcf'')$ lifts to $\Gamma(X,\mcf)$ if and only if $\delta(s)=0$ in $H^1(X,\mcf')$.
On a cover $\{U_i\}$ with local lifts $t_i\in\mcf(U_i)$ of $s$, the Čech cocycle $(t_j-t_i)|_{U_i\cap U_j}$ with values in $\mcf'$ represents $\delta(s)$.
Under $\Pic X\cong H^1(X,\OO_X^\times)$, the Čech cocycle of a line bundle is its family of transition functions $g_{ij}\in\OO_X^\times(U_i\cap U_j)$.

## Dévissage

[[D-COHDEVISSAGE]]
