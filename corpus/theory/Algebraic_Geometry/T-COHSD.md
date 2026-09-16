---
schema: qual/card@1
id: T-COHSD
kind: theorem
title: Serre duality in dimension $n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Canonical Sheaf
  - Cohomology
relations:
- kind: uses
  target: T-IJW1K
- kind: related-to
  target: T-MWDVL
review: draft
prompts:
- State Serre duality in arbitrary dimension.
- What is the dualizing sheaf of $\PP^n$?
- What does duality say about Hodge numbers?
---

::: {.theorem}
Let $X$ be a smooth proper variety of dimension $n$ over a field $k$, with canonical sheaf $\omega_X = \Omega^n_{X/k}$, and let $\mcl$ be locally free.
Then the cup product pairing
\[
H^i(X, \mcl) \tensor H^{n-i}\qty{X, \omega_X \tensor \mcl\dual} \to H^n(X,\omega_X) \cong k
\]
is perfect, so $H^i(X,\mcl) \cong H^{n-i}\qty{X, \omega_X \tensor \mcl\dual}\dual$.
:::

::: {.remark}
For $X = \PP^n$ this is the symmetry already visible in the twists, with $\omega = \OO(-n-1)$; that computation is what the general theorem is modelled on, and it is also the base case of its proof.

Smoothness is what makes $\omega_X$ the sheaf of top forms.
Without it, a projective scheme $X$ of dimension $n$ over $k$ still has a \dfn{dualizing sheaf} $\omega_X^\circ$ with a trace map $t \colon H^n(X, \omega_X^\circ) \to k$, such that for every coherent $\mcf$ the pairing
\[
\Hom(\mcf, \omega_X^\circ) \times H^n(X, \mcf) \to H^n(X, \omega_X^\circ) \xrightarrow{t} k
\]
is perfect.
Duality in the other degrees,
\[
H^i(X,\mcf) \cong \Ext^{n-i}\qty{\mcf, \omega_X^\circ}\dual \quad \text{for all } i ,
\]
holds exactly when $X$ is Cohen--Macaulay and equidimensional.
That $\omega_X^\circ$ agrees with $\Omega^n$ is what smoothness buys.
Properness cannot be dropped at all: on $\AA^n$ the top cohomology that would receive the pairing is zero.

Two consequences worth saying immediately: $h^i(\mcl) = h^{n-i}(\omega \tensor \mcl\dual)$ and $\chi(\mcl) = (-1)^n \chi(\omega \tensor \mcl\dual)$, and taking $\mcl = \OO$ gives $h^n(\OO_X) = h^0(\omega_X) = p_g$.
:::
