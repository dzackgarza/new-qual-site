---
schema: qual/card@1
id: D-VJFAP
kind: definition
title: The espace étalé, and sheafification as continuous sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Stalks
relations:
- kind: uses
  target: D-0QSI0
- kind: related-to
  target: T-3VX80
review: draft
prompts:
- What is the espace étalé of a presheaf, and what topology does it carry?
- Describe sheafification as a space of sections.
- Why is a continuous section of $\Et(\mcf)$ the same thing as a section of $\mcf^+$?
---

::: {.definition title="Espace étalé"}
Let $\mcf$ be a presheaf on $X$.
Set
$$
\Et(\mcf) \da \disjoint_{p \in X} \mcf_p ,
\qquad
\pi : \Et(\mcf) \to X ,
$$
where $\pi$ sends every germ in $\mcf_p$ to $p$.

Each $s \in \mcf(U)$ gives a set-theoretic section $\bar s : U \to \Et(\mcf)$, $p \mapsto s_p$, with $\pi \circ \bar s = \id_U$.
Give $\Et(\mcf)$ the finest topology making every such $\bar s$ continuous.
:::

::: {.proposition}
For that topology,
$$
\mcf^+(U) = \ts{ \text{continuous } t : U \to \Et(\mcf) \st \pi \circ t = \id_U } .
$$
:::

::: {.remark}
The sets $\bar s(U)$, for $U$ open and $s \in \mcf(U)$, form a basis of the topology, and each $\bar s$ is a homeomorphism of $U$ onto the open set $\bar s(U)$, with inverse $\pi|_{\bar s(U)}$.
Hence $\pi$ is a local homeomorphism.
:::

::: {.remark title="Sheaves as spaces over $X$"}
In [[T-3VX80]], $\mcf^+(U)$ is the set of compatible families of germs; the proposition identifies these with the continuous sections of $\pi$.
The functor $\mcf\mapsto(\Et(\mcf)\to X)$ restricts to an equivalence between sheaves on $X$ and spaces over $X$ whose projection is a local homeomorphism; the inverse sends such a space to its sheaf of continuous sections.

Since $\Et(\mcf)$ is built from the stalks, $(\mcf^+)_p = \mcf_p$ for every $p$.
The map $\mcf \to \mcf^+$ is an isomorphism if and only if $\mcf$ is a sheaf.

For an abelian group $A$, the constant presheaf $U\mapsto A$ and the constant sheaf $\ul{A}$ have the same espace étalé, $X \times A$ with $A$ discrete; its continuous sections over $U$ are the locally constant functions $U\to A$, which are the sections of $\ul{A}$.
:::
