---
title: Vanishing and duality
order: 2
topics:
- Serre Criterion
- Serre Duality
- Riemann-Roch
---

# Vanishing and duality

[[T-5IOUR]]

The criterion holds for quasicompact quasi-separated schemes, with $\mci$ ranging over quasicoherent ideal sheaves.
It fails without quasicompactness: $X=\coprod_{n\in\NN}\Spec k$ has $H^p(X,\mcf)=\prod_nH^p(\Spec k,\mcf|_{\Spec k})=0$ for every quasicoherent $\mcf$ on $X$ and every $p>0$, and $X$ is not quasicompact, hence not affine.

## Serre duality and Riemann--Roch for curves

[[T-COHSD]]

Properness is needed for the pairing: $\AA^1_k$ is smooth of dimension $1$, $H^1(\AA^1_k,\omega_{\AA^1_k})=0$ by affine vanishing, and $H^0(\AA^1_k,\OO)=k[x]$ is infinite-dimensional.

[[T-MWDVL]]

By Serre duality $h^1(\OO(D))=\ell(K-D)$, so $\chi(\OO(D))=\deg D+1-g$ is the identity $\ell(D)-\ell(K-D)=\deg D+1-g$.
For $\deg D>2g-2$, $\ell(K-D)=0$ and $\ell(D)=\deg D+1-g$.
At $D=0$, Riemann--Roch gives $\ell(K)=g$: the global regular differentials on a curve of genus $g$ form a $g$-dimensional space.
At $D=K$, it gives $\deg K=2g-2$, which enters Riemann--Hurwitz in [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

## Riemann--Roch for surfaces

[[T-COHRRS]]

By Serre duality $h^2(\OO_X(D))=h^0(\OO_X(K-D))$, so
$$
h^0(\OO_X(D))\ge\chi(\OO_X)+\tfrac12D\cdot(D-K)-h^0(\OO_X(K-D)).
$$
If $h^0(\OO_X(K-D))=0$ and $\chi(\OO_X)+\tfrac12D\cdot(D-K)>0$, then $h^0(\OO_X(D))>0$, and $D$ is linearly equivalent to an effective divisor.

## Finiteness and vanishing for ample twists

[[T-CARTSERRE]]

[[T-KODVAN]]

[[T-GAGA]]

## Topology of hyperplane sections

[[T-LEFHYP]]

[[T-HARDLEF]]
