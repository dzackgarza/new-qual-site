---
schema: qual/card@1
id: P-AGH384PROJBUNDLE
kind: problem
title: Cohomology of a projective bundle and geometrically ruled surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Projective Bundles
  - Relative Canonical Sheaf
  - Ruled Surfaces
relations: []
review: draft
---

::: problem
Let $Y$ be a noetherian scheme, and let $\mce$ be a locally free $\mco_Y\dash$module of rank $n+1$, with $n \geq 1$. Let $X = \PP(\mce)$ (II, §7), with the invertible sheaf $\mco_X(1)$ and the projection morphism $\pi: X \to Y$.

a. Show that:

    - $\pi_*(\mco(l)) \cong \operatorname{Sym}^l(\mce)$ for $l \geq 0$, and $\pi_*(\mco(l)) = 0$ for $l < 0$ (II, 7.11);
    - $R^i \pi_*(\mco(l)) = 0$ for $0 < i < n$ and all $l \in \ZZ$; and
    - $R^n \pi_*(\mco(l)) = 0$ for $l > -n-1$.

b. Show there is a natural exact sequence
\[
0 \to \Omega_{X/Y} \to (\pi^* \mce)(-1) \to \mco \to 0
,\]
cf. (II, 8.13), and conclude that the **relative canonical sheaf** $\omega_{X/Y} = \wedge^n \Omega_{X/Y}$ is isomorphic to $(\pi^* \wedge^{n+1} \mce)(-n-1)$. Show furthermore that there is a natural isomorphism $R^n \pi_*(\omega_{X/Y}) \cong \mco_Y$ (cf. (7.1.1)).

c. Now show, for any $l \in \ZZ$, that
\[
R^n \pi_*(\mco(l)) \cong \pi_*(\mco(-l-n-1))\dual \tensor (\wedge^{n+1} \mce)\dual
.\]

d. Show that $p_a(X) = (-1)^n p_a(Y)$ (use (Ex. 8.1)) and $p_g(X) = 0$ (use (II, 8.11)).

e. In particular, if $Y$ is a nonsingular projective curve of genus $g$, and $\mce$ a locally free sheaf of rank $2$, then $X$ is a projective surface with $p_a = -g$, $p_g = 0$, and irregularity $g$ (7.12.3). This kind of surface is called a **geometrically ruled surface** (V, §2).
:::
