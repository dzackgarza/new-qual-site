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
- What is a dualizing sheaf, and when does duality hold in every degree?
---

::: {.theorem}
Let $X$ be a smooth proper variety of dimension $n$ over a field $k$, with canonical sheaf $\omega_X = \Omega^n_{X/k}$, and let $\mcl$ be locally free.
Then the cup product pairing
\[
H^i(X, \mcl) \tensor H^{n-i}\qty{X, \omega_X \tensor \mcl\dual} \to H^n(X,\omega_X) \cong k
\]
is perfect, so $H^i(X,\mcl) \cong H^{n-i}\qty{X, \omega_X \tensor \mcl\dual}\dual$.
:::

::: {.definition title="Dualizing sheaf"}
Let $X$ be a proper scheme of dimension $n$ over a field $k$.
A \dfn{dualizing sheaf} for $X$ is a coherent sheaf $\omega_X^\circ$ with a $k$-linear \dfn{trace map} $t \colon H^n(X, \omega_X^\circ) \to k$ such that for every coherent sheaf $\mcf$ the pairing
$$\Hom(\mcf, \omega_X^\circ) \times H^n(X, \mcf) \to H^n(X, \omega_X^\circ) \xrightarrow{t} k$$
induces an isomorphism $\Hom(\mcf, \omega_X^\circ) \cong H^n(X, \mcf)\dual$.
A dualizing sheaf is unique up to unique isomorphism compatible with the trace maps.
:::

::: {.theorem title="Serre duality for projective schemes"}
Let $X$ be a projective scheme of dimension $n$ over an algebraically closed field $k$.

1. $X$ has a dualizing sheaf $\omega_X^\circ$.

2. For every $i$ and every coherent $\mcf$ there are natural maps $\theta^i \colon \Ext^i(\mcf, \omega_X^\circ) \to H^{n-i}(X, \mcf)\dual$, and $\theta^0$ is an isomorphism.

3. The maps $\theta^i$ are isomorphisms for all $i$ and all coherent $\mcf$ if and only if $X$ is Cohen--Macaulay and equidimensional. In that case, for $\mcf$ locally free, $H^i(X, \mcf) \cong H^{n-i}(X, \omega_X^\circ \otimes \mcf\dual)\dual$.

4. If $X$ is smooth, $\omega_X^\circ \cong \omega_X = \Omega^n_{X/k}$.
:::

::: {.remark}
For $X = \PP^n$ this is the symmetry already visible in the twists, with $\omega = \OO(-n-1)$; that computation is what the general theorem is modelled on, and it is also the base case of its proof.

Properness cannot be dropped at all: on $\AA^n$ the top cohomology that would receive the pairing is zero.

Two consequences worth saying immediately: $h^i(\mcl) = h^{n-i}(\omega \tensor \mcl\dual)$ and $\chi(\mcl) = (-1)^n \chi(\omega \tensor \mcl\dual)$, and taking $\mcl = \OO$ gives $h^n(\OO_X) = h^0(\omega_X) = p_g$.
:::
