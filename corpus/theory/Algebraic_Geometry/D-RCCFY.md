---
schema: qual/card@1
id: D-RCCFY
kind: definition
title: Presheaves, sheaves, and the two axioms
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
:::

::: {.definition title="Sheaf"}
A presheaf is a \dfn{sheaf} if for every open $U$ and every open cover $\ts{U_i}$ of $U$:

- *identity*: a section $s \in \mcf(U)$ with $\ro{s}{U_i} = 0$ for all $i$ is $0$;

- *gluing*: sections $s_i \in \mcf(U_i)$ agreeing on every overlap $U_i \intersect U_j$ come from a section of $\mcf(U)$.
:::

::: {.remark}
The two axioms say that a section is determined by local data and that compatible local data assembles.
Together they make $\mcf(U)$ the limit of the diagram of its restrictions, which is why a sheaf is exactly a presheaf satisfying descent for open covers.

Identity without gluing is a **separated presheaf**, and the distinction is worth keeping: sheafification of a separated presheaf only adds the missing glued sections, while in general it must also kill sections that are locally zero.
:::

::: {.remark title="The equalizer form"}
Both axioms at once say that
\[
\mcf(U) \to \prod_i \mcf(U_i) \rightrightarrows \prod_{i,j} \mcf(U_i \intersect U_j)
\]
is an equalizer, the two maps being restriction from $U_i$ and from $U_j$ to the overlap.
Injectivity of the first map is identity; that its image is exactly the equalizer is gluing.
This is the formulation to quote when the question moves to sites and descent, where there are no points to test on.
:::
