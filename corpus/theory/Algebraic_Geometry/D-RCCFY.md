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
A **presheaf** $\mathcal{F}$ of abelian groups on a space $X$ assigns a group $\mathcal{F}(U)$ to each open $U$ and a restriction $\res{U}{V}: \mathcal{F}(U) \to \mathcal{F}(V)$ to each inclusion $V \subseteq U$, functorially, with $\mathcal{F}(\emptyset) = 0$.
:::

::: {.definition title="Sheaf"}
A presheaf is a **sheaf** if for every open $U$ and every open cover $\ts{U_i}$ of $U$:

- *identity*: a section $s \in \mathcal{F}(U)$ with $\ro{s}{U_i} = 0$ for all $i$ is $0$;

- *gluing*: sections $s_i \in \mathcal{F}(U_i)$ agreeing on every overlap $U_i \intersect U_j$ come from a section of $\mathcal{F}(U)$.
:::

::: {.remark}
The two axioms say that a section is determined by local data and that compatible local data assembles.
Together they make $\mathcal{F}(U)$ the limit of the diagram of its restrictions, which is why a sheaf is exactly a presheaf satisfying descent for open covers.

Identity without gluing is a **separated presheaf**, and the distinction is worth keeping: sheafification of a separated presheaf only adds the missing glued sections, while in general it must also kill sections that are locally zero.
:::
