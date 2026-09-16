---
schema: qual/card@1
id: P-AGH361EXTONE
kind: problem
title: Extensions of sheaves of modules are classified by $\Ext^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Groups
  - Extensions
  - Sheaves of Modules
relations: []
review: draft
---

::: {.problem}
Let $(X, \mco_X)$ be a ringed space, and let $\mcf', \mcf'' \in \Mod(X)$.
An **extension** of $\mcf''$ by $\mcf'$ is a short exact sequence
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
in $\Mod(X)$.
Two extensions are isomorphic if there is an isomorphism of the short exact sequences, inducing the identity maps on $\mcf'$ and $\mcf''$.
Given an extension as above, consider the long exact sequence arising from $\Hom(\mcf'', \wait)$, in particular the map
\[
\delta: \Hom(\mcf'', \mcf'') \to \Ext^1(\mcf'', \mcf'),
\]
and let $\xi \in \Ext^1(\mcf'', \mcf')$ be $\delta(1_{\mcf''})$.
Show that this process gives a one-to-one correspondence between isomorphism classes of extensions of $\mcf''$ by $\mcf'$, and elements of the group $\Ext^1(\mcf'', \mcf')$.
:::
