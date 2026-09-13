---
schema: qual/card@1
id: PR-FULCM
kind: proposition
title: Toric varieties are rational and Cohen-Macaulay, and affine ones have no nontrivial vector bundles
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

::: {.proposition title="Three free properties"}
Let $X_\Sigma$ be a toric variety of dimension $n$.

1. $X_\Sigma$ is rational: it contains the torus $T \cong \GG_m^n$ as a dense open set, so $k(X_\Sigma) = k(t_1, \ldots, t_n)$.

2. $X_\Sigma$ is Cohen-Macaulay: every local ring $R$ has $\depth R = \dim R$.

3. Every vector bundle on an affine toric variety $U_\sigma$ is trivial, equivalently every finitely generated projective $k[S_\sigma]$-module is free.
:::

::: {.remark title="What each one is worth"}
Rationality is the one-line answer to "is this variety rational", and it is also the reason toric varieties supply no counterexamples about rationality: they are all rational, so a unirational-but-not-rational example must be found elsewhere.

Cohen-Macaulayness is the input that makes Serre duality and the vanishing theorems available without extra hypotheses, and it is why $\omega_{X_\Sigma} = \OO(-\sum_\rho D_\rho)$ behaves as a dualising sheaf even at singular points.
Note the contrast with Gorenstein, which is a genuine condition: $X_\Sigma$ is Gorenstein exactly when $K_X$ is Cartier, which for $X_P$ means $P$ reflexive.

The third statement is the toric case of a theorem on semigroup rings, and it says that $\Pic(U_\sigma) = 0$ for every cone, which is what makes the class group of the cone over the rational normal curve a clean example of $\Pic \subsetneq \Cl$.
:::
