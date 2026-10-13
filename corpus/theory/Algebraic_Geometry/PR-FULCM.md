---
schema: qual/card@1
id: PR-FULCM
kind: proposition
title: Rationality, Cohen--Macaulayness, and vector bundles on toric varieties
slogan: 'Every toric variety is rational and Cohen--Macaulay; every vector bundle on an affine toric variety is trivial.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cohen-Macaulay Rings
  - Vector Bundles
relations:
- kind: uses
  target: PR-TORSMAFF
review: draft
prompts:
- What general ring-theoretic and birational properties does every toric variety have?
- What are the vector bundles on an affine toric variety?
---

::: {.proposition}
Let $X_\Sigma$ be an $n$-dimensional toric variety over a field $k$.

1. $X_\Sigma$ is rational: the dense torus $T\cong\GG_m^n$ has function field
$$
k(T)=k(t_1,\ldots,t_n)=k(X_\Sigma).
$$

2. $X_\Sigma$ is Cohen--Macaulay: every local ring $\OO_{X_\Sigma,x}$ satisfies
$$
\depth\OO_{X_\Sigma,x}=\dim\OO_{X_\Sigma,x}.
$$

3. By Gubeladze's theorem on projective modules over normal monoid algebras, every vector bundle on an affine toric variety $U_\sigma$ is trivial. Equivalently, every finitely generated projective $k[S_\sigma]$-module is free.
:::

::: {.remark title="Consequences"}
The rationality statement follows directly from the dense torus and does not require smoothness or completeness.

Since toric varieties are normal and Cohen--Macaulay, their canonical module is represented by the torus-invariant canonical divisor
$$
K_{X_\Sigma}\sim-\sum_{\rho\in\Sigma(1)}D_\rho.
$$
The toric variety is Gorenstein exactly when this canonical divisor is Cartier.

The vector-bundle theorem implies $\Pic(U_\sigma)=0$ for every affine toric chart. Singular affine toric varieties can nevertheless have nonzero divisor class group; [[FE-TORCD]] gives $\Cl(U_\sigma)\cong\ZZ/d\ZZ$ for the cone over the rational normal curve of degree $d$.
:::
