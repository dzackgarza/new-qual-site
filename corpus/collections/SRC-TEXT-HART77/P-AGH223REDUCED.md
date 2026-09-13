---
schema: qual/card@1
id: P-AGH223REDUCED
kind: problem
title: Reducedness is local, and every scheme has a reduction
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Reduced Schemes
  - Nilpotents
relations: []
review: draft
---

::: problem
A scheme $(X, \OO_X)$ is **reduced** if for every open set $U \subseteq X$ the ring $\OO_X(U)$ has no nilpotent elements.

a. Show that $(X, \OO_X)$ is reduced if and only if for every $P \in X$ the local ring $\OO_{X, P}$ has no nilpotent elements.

b. Let $(X, \OO_X)$ be a scheme.
Let $(\OO_X)_{\mathrm{red}}$ be the sheaf associated to the presheaf $U \mapsto \OO_X(U)_{\mathrm{red}}$, where for any ring $A$ we denote by $A_{\mathrm{red}}$ the quotient of $A$ by its ideal of nilpotent elements.
Show that $\qty{X, (\OO_X)_{\mathrm{red}}}$ is a scheme.
We call it the **reduced scheme** associated to $X$ and denote it by $X_{\mathrm{red}}$.
Show that there is a morphism of schemes $X_{\mathrm{red}} \to X$ which is a homeomorphism on the underlying topological spaces.

c. Let $f: X \to Y$ be a morphism of schemes and assume that $X$ is reduced.
Show that there is a unique morphism $g: X \to Y_{\mathrm{red}}$ such that $f$ is obtained by composing $g$ with the natural map $Y_{\mathrm{red}} \to Y$.
:::
