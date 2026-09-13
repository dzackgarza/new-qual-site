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
Let $X$ be smooth projective of dimension $n$ over $k = \bar k$, with canonical sheaf $\omega_X = \Omega^n_{X/k}$, and let $\mcl$ be locally free.
Then the cup product pairing
\[
H^i(X, \mcl) \tensor H^{n-i}\qty{X, \omega_X \tensor \mcl\dual} \to H^n(X,\omega_X) \cong k
\]
is perfect, so $H^i(X,\mcl) \cong H^{n-i}\qty{X, \omega_X \tensor \mcl\dual}\dual$.
:::

::: {.remark}
For $X = \PP^n$ this is the symmetry already visible in the twists, with $\omega = \OO(-n-1)$; that computation is what the general theorem is modelled on, and it is also the base case of its proof.

Smoothness is what makes $\omega_X$ the sheaf of top forms.
Without it duality still holds with a *dualizing sheaf* $\omega_X^\circ$ characterised by the pairing, for any projective scheme, and the general statement uses $\Ext$ groups:
\[
H^i(X,\mcf) \cong \Ext^{n-i}\qty{\mcf, \omega_X^\circ}\dual .
\]
That $\omega_X^\circ$ agrees with $\Omega^n$ is exactly what smoothness buys.
Properness cannot be dropped at all: on $\AA^n$ the top cohomology that would receive the pairing is zero.

Two consequences worth saying immediately: $h^i(\mcl) = h^{n-i}(\omega \tensor \mcl\dual)$ and $\chi(\mcl) = (-1)^n \chi(\omega \tensor \mcl\dual)$, and taking $\mcl = \OO$ gives $h^n(\OO_X) = h^0(\omega_X) = p_g$.
:::
