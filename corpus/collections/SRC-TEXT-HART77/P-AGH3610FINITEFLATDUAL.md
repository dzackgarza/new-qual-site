---
schema: qual/card@1
id: P-AGH3610FINITEFLATDUAL
kind: problem
title: Duality for a finite flat morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Duality
  - Finite Morphisms
  - Ext Sheaves
  - Flatness
relations: []
review: draft
---

::: problem
a. Let $f: X \to Y$ be a finite morphism of noetherian schemes.
For any quasi-coherent $\mco_Y$-module $\mcg$, $\sheafhom_Y(f_* \mco_X, \mcg)$ is a quasi-coherent $f_* \mco_X$-module, hence corresponds to a quasi-coherent $\mco_X$-module, which we call $f^{!} \mcg$ (II, Ex.
5.17e).

b. Show that for any coherent $\mcf$ on $X$ and any quasi-coherent $\mcg$ on $Y$, there is a natural isomorphism
\[
f_* \sheafhom_X(\mcf, f^{!} \mcg) \iso \sheafhom_Y(f_* \mcf, \mcg).
\]

c. For each $i \geq 0$, there is a natural map
\[
\varphi_i: \Ext_X^i(\mcf, f^{!} \mcg) \to \Ext_Y^i(f_* \mcf, \mcg).
\]
Hint: First construct a map $\Ext_X^i(\mcf, f^{!} \mcg) \to \Ext_Y^i(f_* \mcf, f_* f^{!} \mcg)$.
Then compose with a suitable map from $f_* f^{!} \mcg$ to $\mcg$.

d. Now assume that $X$ and $Y$ are separated, $\Coh(X)$ has enough locally frees, and assume that $f_* \mco_X$ is locally free on $Y$ (this is equivalent to saying $f$ is flat — see §9). Show that $\varphi_i$ is an isomorphism for all $i$, all $\mcf$ coherent on $X$, and all $\mcg$ quasi-coherent on $Y$.

Hints: First do $i=0$.
Then do $\mcf=\mco_X$, using (Ex.
4.1). Then do $\mcf$ locally free.
Do the general case by induction on $i$, writing $\mcf$ as a quotient of a locally free sheaf.
:::
