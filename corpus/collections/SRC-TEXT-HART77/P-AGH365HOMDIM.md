---
schema: qual/card@1
id: P-AGH365HOMDIM
kind: problem
title: Homological dimension of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Sheaves
  - Homological Dimension
  - Locally Free Sheaves
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian scheme, and assume that $\Coh(X)$ has enough locally frees (Ex. 6.4). Then for any coherent sheaf $\mcf$ we define the **homological dimension** of $\mcf$, denoted $\operatorname{hd}(\mcf)$, to be the least length of a locally free resolution of $\mcf$ (or $+\infty$ if there is no finite one). Show:

a. $\mcf$ is locally free $\iff \mathcal{E}xt^1(\mcf, \mcg)=0$ for all $\mcg \in \Mod(X)$;

b. $\operatorname{hd}(\mcf) \leq n \iff \mathcal{E}xt^i(\mcf, \mcg)=0$ for all $i>n$ and all $\mcg \in \Mod(X)$;

c. $\operatorname{hd}(\mcf)=\sup_x \operatorname{pd}_{\mco_x} \mcf_x$.
:::
