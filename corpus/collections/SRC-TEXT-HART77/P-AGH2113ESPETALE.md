---
schema: qual/card@1
id: P-AGH2113ESPETALE
kind: problem
title: Sheafification as the sheaf of continuous sections of the espace étalé
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Espace Etale
relations: []
review: draft
---

::: problem
Given a presheaf $\mcf$ on $X$, define a topological space $\operatorname{Spe}(\mcf)$, called the **espace étalé** of $\mcf$, as follows.
As a set, $\operatorname{Spe}(\mcf) = \Union_{P \in X} \mcf_P$.
Define a projection map $\pi: \operatorname{Spe}(\mcf) \to X$ by sending $s \in \mcf_P$ to $P$.
For each open set $U \subseteq X$ and each section $s \in \mcf(U)$ we obtain a map $\bar{s}: U \to \operatorname{Spe}(\mcf)$ sending $P \mapsto s_P$, the germ of $s$ at $P$.
This map satisfies $\pi \circ \bar{s} = \id$, so it is a section of $\pi$ over $U$.
Give $\operatorname{Spe}(\mcf)$ the strongest topology such that all the maps $\bar{s}$, for all $U$ and all $s \in \mcf(U)$, are continuous.

Show that the sheaf $\mcf^{+}$ associated to $\mcf$ can be described as follows: for any open $U \subseteq X$, the group $\mcf^{+}(U)$ is the set of continuous sections of $\operatorname{Spe}(\mcf)$ over $U$.

In particular, the original presheaf $\mcf$ was a sheaf if and only if for each $U$ the group $\mcf(U)$ equals the set of all continuous sections of $\operatorname{Spe}(\mcf)$ over $U$.
:::

::: remark
This exercise connects Hartshorne's definition of a sheaf with the espace étalé definition used elsewhere in the literature, for example in Godement.
:::
