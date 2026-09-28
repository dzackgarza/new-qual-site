---
title: Cohomology in families
order: 5
topics:
- Higher Direct Images
- Base Change
- Formal Functions
---

# Cohomology in families

[[D-COHRIF]]

[[T-COHLERAY]]

If $f$ is affine and $\mcf$ is quasicoherent, then $R^qf_*\mcf=0$ for $q>0$, the Leray spectral sequence degenerates, and $H^i(X,\mcf)\cong H^i(Y,f_*\mcf)$.
For a closed immersion $\iota\colon X\hookrightarrow\PP^n$ and a coherent sheaf $\mcf$ on $X$, this gives $H^i(X,\mcf)\cong H^i(\PP^n,\iota_*\mcf)$.

## Formal functions and semicontinuity

[[T-COHFF]]

[[T-COHBC]]

Without flatness, $\chi$ need not be locally constant.
For distinct points $p,q\in\PP^1$, let $X=(\AA^1\times\{p\})\cup(\{0\}\times\{q\})\subset\AA^1\times\PP^1$ with the projection $f\colon X\to\AA^1$.
Then $f$ is projective, $\chi(\OO_{X_t})=1$ for $t\neq0$, and $\chi(\OO_{X_0})=2$; the sheaf $\OO_X$ is not flat over $\AA^1$.

Cohomology need not commute with base change when $h^i$ jumps.
For a smooth projective curve $C$ of genus $g\ge1$ and the Poincaré line bundle $\mathcal P$ on $C\times\Pic^0(C)$, $h^0(C,\mathcal P_t)$ is $1$ at the trivial bundle $t=0$ and $0$ elsewhere, while $\chi(\mathcal P_t)=1-g$ for every $t$.
The pushforward $\pi_*\mathcal P$ to $\Pic^0(C)$ is torsion-free of generic rank $0$, so $\pi_*\mathcal P=0$, and the base change map $\pi_*\mathcal P\otimes k(0)\to H^0(C,\OO_C)=k$ is not surjective.

## Base change theorems

[[T-BASECHANGE]]

## The projection formula

[[PR-SCHPROJFORM]]

## Deformations

[[D-COTCPLX]]

[[T-DEFEXT]]
