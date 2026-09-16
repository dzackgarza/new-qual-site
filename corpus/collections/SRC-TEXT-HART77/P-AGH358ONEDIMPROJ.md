---
schema: qual/card@1
id: P-AGH358ONEDIMPROJ
kind: problem
title: Every one-dimensional proper scheme is projective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Schemes
  - Projectivity
  - Curves
  - Picard Group
relations: []
review: draft
---

::: {.problem}
Prove that every one-dimensional proper scheme $X$ over an algebraically closed field $k$ is projective.

a. If $X$ is irreducible and nonsingular, then $X$ is projective by (II, 6.7).

b. If $X$ is integral, let $\tilde{X}$ be its normalization (II, Ex. 3.8). Show that $\tilde{X}$ is complete and nonsingular, hence projective by (a).

    Let $f: \tilde{X} \to X$ be the projection. Let $\mcl$ be a very ample invertible sheaf on $\tilde{X}$. Show there is an effective divisor $D=\sum P_i$ on $\tilde{X}$ with $\mcl(D) \cong \mcl$, and such that $f(P_i)$ is a nonsingular point of $X$, for each $i$.

    Conclude that there is an invertible sheaf $\mcl_0$ on $X$ with $f^* \mcl_0 \cong \mcl$. Then use (Ex. 5.7d), (II, 7.6) and (II, 5.16.1) to show that $X$ is projective.

c. If $X$ is reduced, but not necessarily irreducible, let $X_1, \ldots, X_r$ be the irreducible components of $X$. Use (Ex. 4.5) to show $\Pic X \to \bigoplus_i \Pic X_i$ is surjective. Then use (Ex. 5.7c) to show $X$ is projective.

d. Finally, if $X$ is any one-dimensional proper scheme over $k$, use (2.7) and (Ex. 4.6) to show that $\Pic X \to \Pic X_{\mathrm{red}}$ is surjective. Then use (Ex. 5.7b) to show $X$ is projective.
:::
