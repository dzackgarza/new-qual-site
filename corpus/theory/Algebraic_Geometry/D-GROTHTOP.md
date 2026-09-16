---
schema: qual/card@1
id: D-GROTHTOP
kind: definition
title: Sites, sheaves on a site, and topoi
classification:
  areas:
  - algebraic-geometry
  topics:
  - Grothendieck Topologies
  - Sites
  - Topoi
relations:
- kind: uses
  target: D-RCCFY
review: draft
prompts:
- What is a site?
- What is a topos?
- What is a sheaf on a site?
---

::: {.definition title="Site"}
Let $\mathcal{C}$ be a category with fibre products.
A \dfn{Grothendieck topology} on $\mathcal{C}$ assigns to each object $U$ a set $\operatorname{Cov}(U)$ of families of morphisms $\{U_i \to U\}_{i \in I}$, the \dfn{coverings} of $U$, such that:

1. every isomorphism $V \to U$, as a one-element family, is a covering of $U$;

2. if $\{U_i \to U\}_i$ is a covering and $V \to U$ is any morphism, then $\{U_i \times_U V \to V\}_i$ is a covering of $V$;

3. if $\{U_i \to U\}_i$ is a covering and $\{U_{ij} \to U_i\}_j$ is a covering of $U_i$ for each $i$, then the composites $\{U_{ij} \to U\}_{i,j}$ form a covering of $U$.

A \dfn{site} is a category with fibre products together with a Grothendieck topology.
:::

::: {.definition title="Sheaf on a site"}
A \dfn{presheaf} of sets on a site $\mathcal{C}$ is a functor $F \colon \mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$.
It is a \dfn{sheaf} if for every covering $\{U_i \to U\}_i$ the diagram
$$F(U) \to \prod_i F(U_i) \rightrightarrows \prod_{i, j} F(U_i \times_U U_j)$$
is an equalizer, where the two parallel maps are induced by the projections $U_i \times_U U_j \to U_i$ and $U_i \times_U U_j \to U_j$.
Sheaves of abelian groups, rings or modules are defined in the same way with values in those categories.
The sheaves of sets form a full subcategory $\Sh(\mathcal{C}) \subseteq \operatorname{Fun}(\mathcal{C}^{\mathrm{op}}, \mathsf{Set})$.
:::

::: {.definition title="Topos"}
A \dfn{topos} is a category equivalent to $\Sh(\mathcal{C})$ for some site $\mathcal{C}$.
:::

::: {.example}
For a topological space $X$, let $\operatorname{Op}(X)$ be the category of open subsets with inclusions, where $V \times_U W = V \cap W$, and let the coverings of $U$ be the families $\{U_i \subseteq U\}$ with $\bigcup_i U_i = U$.
The sheaves on this site are the sheaves on $X$ in the sense of [[D-RCCFY]], and $\Sh(X)$ is a topos.
The étale and fppf topologies on a category of schemes are the sites of [[D-ETFPPF]].
:::
