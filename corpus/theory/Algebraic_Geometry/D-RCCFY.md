---
schema: qual/card@1
id: D-RCCFY
kind: definition
title: Presheaves, sheaves, and the sheaf axioms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Presheaves
relations: []
review: draft
prompts:
- What is a presheaf, and what does a sheaf add?
- State the sheaf axioms.
---

::: {.definition title="Presheaf"}
A \dfn{presheaf} $\mcf$ of abelian groups on a space $X$ assigns a group $\mcf(U)$ to each open $U$ and a restriction $\res{U}{V}: \mcf(U) \to \mcf(V)$ to each inclusion $V \subseteq U$, functorially, with $\mcf(\emptyset) = 0$.
Equivalently, $\mcf$ is a contravariant functor from the category of open subsets of $X$, with inclusions as morphisms, to abelian groups.
More generally, a presheaf with values in a category $\mcc$ (sets, rings, modules) is a contravariant functor from open subsets of $X$ to $\mcc$, and sheaves with values in $\mcc$ are defined by the same two axioms.
Elements of $\mcf(U)$ are \dfn{sections} of $\mcf$ over $U$, and elements of $\mcf(X)$ are \dfn{global sections}.
:::

::: {.definition title="Sheaf"}
A presheaf is a \dfn{sheaf} if for every open $U$ and every open cover $\theset{U_i}$ of $U$:

- *identity*: a section $s \in \mcf(U)$ with $\restrictionof{s}{U_i} = 0$ for all $i$ is $0$;

- *gluing*: sections $s_i \in \mcf(U_i)$ agreeing on every overlap $U_i \intersect U_j$ come from a section of $\mcf(U)$.

A presheaf satisfying the identity axiom is a \dfn{separated presheaf}.
:::

::: {.remark}
For a separated presheaf $\mcf$, the map $\mcf\to\mcf^+$ to its sheafification is injective on sections; for an arbitrary presheaf, its kernel on $\mcf(U)$ consists of the sections whose restrictions to the members of some open cover of $U$ vanish.
:::

::: {.remark title="The equalizer form"}
Both axioms at once say that
$$
\mcf(U) \to \prod_i \mcf(U_i) \rightrightarrows \prod_{i,j} \mcf(U_i \intersect U_j)
$$
is an equalizer, the two maps being restriction from $U_i$ and from $U_j$ to the overlap.
Injectivity of the first map is identity; that its image is exactly the equalizer is gluing.
This equalizer condition, with fibre products $U_i\times_UU_j$ in place of intersections, is the definition of a sheaf on a site ([[D-GROTHTOP]]).
:::
