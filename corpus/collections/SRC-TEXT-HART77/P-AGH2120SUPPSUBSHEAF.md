---
schema: qual/card@1
id: P-AGH2120SUPPSUBSHEAF
kind: problem
title: The subsheaf of sections supported in a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Flasque Sheaves
relations: []
review: draft
---

::: {.problem}
Let $Z$ be a closed subset of $X$ and let $\mcf$ be a sheaf on $X$.
Define $\Gamma_Z(X, \mcf)$ to be the subgroup of $\Gamma(X, \mcf)$ consisting of all sections whose support is contained in $Z$.

a. Show that the presheaf $V \mapsto \Gamma_{Z \intersect V}\qty{V, \ro{\mcf}{V}}$ is a sheaf.
It is called the **subsheaf of $\mcf$ with supports in $Z$** and is denoted $\mathcal{H}_Z^0(\mcf)$.

b. Let $U = X \sm Z$ and let $j: U \to X$ be the inclusion.
Show that there is an exact sequence of sheaves on $X$
\[
0 \to \mathcal{H}_Z^0(\mcf) \to \mcf \to j_*\qty{\ro{\mcf}{U}}.
\]
Furthermore, if $\mcf$ is flasque, show that the map $\mcf \to j_*\qty{\ro{\mcf}{U}}$ is surjective.
:::
