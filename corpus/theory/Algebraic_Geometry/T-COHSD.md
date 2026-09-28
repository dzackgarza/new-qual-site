---
schema: qual/card@1
id: T-COHSD
kind: theorem
title: Serre duality in dimension $n$
slogan: 'Serre duality pairs complementary degrees perfectly: $H^i(\mcl)$ is dual to $H^{n-i}(\omega_X\tensor\dualof{\mcl})$ on a smooth proper $n$-fold.'
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
Let $X$ be a smooth proper variety of dimension $n$ over a field $k$, with canonical sheaf $\omega_X = \Omega^n_{X/k}$, and let $\mcl$ be locally free of finite rank.
Then the cup product pairing
$$
H^i(X, \mcl) \tensor H^{n-i}\qty{X, \omega_X \tensor \dualof{\mcl}}
\to H^n(X,\omega_X)\xrightarrow{t_X} k
$$
is perfect, so $H^i(X,\mcl) \cong H^{n-i}\dualof{\qty{X, \omega_X \tensor \dualof{\mcl}}}$, by [duality for proper schemes over fields](https://stacks.math.columbia.edu/tag/0FVU). The trace $t_X$ corresponds under $H^n(X,\omega_X)\cong H^0(X,\OO_X)^\vee$ to evaluation on the constant section $1$.
It is an isomorphism exactly when $H^0(X,\OO_X)=k$.
For example, for $X=\Spec K$ with $K/k$ a finite separable extension of degree greater than one, $H^0(X,\omega_X)=K$ has that greater dimension over $k$, so the trace cannot be an isomorphism.
:::

::: {.definition title="Dualizing sheaf"}
Let $X$ be a proper scheme of dimension $n$ over a field $k$.
A \dfn{dualizing sheaf} for $X$ is a coherent sheaf $\omega_X^\circ$ with a $k$-linear \dfn{trace map} $t \colon H^n(X, \omega_X^\circ) \to k$ such that for every coherent sheaf $\mcf$ the pairing $$\Hom(\mcf, \omega_X^\circ) \times H^n(X, \mcf) \to H^n(X, \omega_X^\circ) \xrightarrow{t} k$$ induces an isomorphism $\Hom(\mcf, \omega_X^\circ) \cong \dualof{H^n(X, \mcf)}$.
A dualizing sheaf is unique up to unique isomorphism compatible with the trace maps.
:::

::: {.theorem title="Serre duality for projective schemes"}
Let $X$ be a projective scheme of dimension $n$ over an algebraically closed field $k$.

1. $X$ has a dualizing sheaf $\omega_X^\circ$.

2. For every $i$ and every coherent $\mcf$ there are natural maps $\theta^i \colon \Ext^i(\mcf, \omega_X^\circ) \to \dualof{H^{n-i}(X, \mcf)}$, and $\theta^0$ is an isomorphism.

3. The maps $\theta^i$ are isomorphisms for all $i$ and all coherent $\mcf$ if and only if $X$ is Cohen--Macaulay and equidimensional.
   In that case, for $\mcf$ locally free, $H^i(X, \mcf) \cong \dualof{H^{n-i}(X, \omega_X^\circ \otimes \dualof{\mcf})}$.

4. If $X$ is smooth, $\omega_X^\circ \cong \omega_X = \Omega^n_{X/k}$.
:::

::: {.remark}
For $X = \PP^n$ this is the symmetry already visible in the twists, with $\omega = \OO(-n-1)$; that computation is what the general theorem is modelled on, and it is also the base case of its proof.

Properness cannot be dropped at all: on $\AA^n$ the top cohomology that would receive the pairing is zero.

Two consequences worth saying immediately: $h^i(\mcl) = h^{n-i}(\omega \tensor \dualof{\mcl})$ and $\chi(\mcl) = (-1)^n \chi(\omega \tensor \dualof{\mcl})$, and taking $\mcl = \OO$ gives $h^n(\OO_X) = h^0(\omega_X) = p_g$.
:::
