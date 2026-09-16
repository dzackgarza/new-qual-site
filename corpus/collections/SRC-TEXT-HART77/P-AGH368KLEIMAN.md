---
schema: qual/card@1
id: P-AGH368KLEIMAN
kind: problem
title: Kleiman's theorem on enough locally free sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Invertible Sheaves
  - Locally Factorial Schemes
relations: []
review: draft
---

::: {.problem}
Prove the following theorem of Kleiman: if $X$ is a noetherian, integral, separated, locally factorial scheme, then every coherent sheaf on $X$ is a quotient of a locally free sheaf (of finite rank).

a. First show that open sets of the form $X_s$, for various $s \in \Gamma(X, \mcl)$, and various invertible sheaves $\mcl$ on $X$, form a base for the topology of $X$.

Hint: Given a closed point $x \in X$ and an open neighborhood $U$ of $x$, to show there is an $\mcl, s$ such that $x \in X_s \subseteq U$, first reduce to the case that $Z=X-U$ is irreducible.
Then let $\zeta$ be the generic point of $Z$.
Let $f \in K(X)$ be a rational function with $f \in \mco_x$, $f \notin \mco_\zeta$.
Let $D=(f)_{\infty}$, and let $\mcl=\mcl(D)$, $s \in \Gamma(X, \mcl(D))$ correspond to $D$ (II, §6).

b. Now use (II, 5.14) to show that any coherent sheaf is a quotient of a direct sum $\bigoplus_i \mcl_i^{n_i}$ for various invertible sheaves $\mcl_i$ and various integers $n_i$.
:::
