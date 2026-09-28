---
schema: qual/card@1
id: D-OPENSUBFUNCTOR
kind: definition
title: Zariski sheaves, open subfunctors, and representability by gluing
classification:
  areas:
  - algebraic-geometry
  topics:
  - Functor Of Points
  - Representable Functors
  - Gluing
relations:
- kind: uses
  target: PR-SCHFOP
- kind: related-to
  target: FE-SCHREPFUNCTORS
review: draft
prompts:
- What is a Zariski sheaf?
- What is an open subfunctor?
- When is a functor on schemes representable?
---

For a scheme $X$, write $h_X = \Hom(-, X) \colon \Sch^{\mathrm{op}} \to \mathsf{Set}$ for its functor of points ([[PR-SCHFOP]]).

::: {.definition title="Zariski sheaf"}
A functor $F \colon \Sch^{\mathrm{op}} \to \mathsf{Set}$ is a \dfn{Zariski sheaf} if for every scheme $Y$ the presheaf $U \mapsto F(U)$ on the open subsets $U \subseteq Y$, with restriction maps $F(U) \to F(U')$ induced by the inclusions $U' \subseteq U$, is a sheaf of sets on $Y$.
:::

::: {.definition title="Open subfunctor"}
Let $F, G \colon \Sch^{\mathrm{op}} \to \mathsf{Set}$ be functors.
A natural transformation $\iota \colon G \to F$ exhibits $G$ as an \dfn{open subfunctor} of $F$ if for every scheme $X$ and every natural transformation $h_X \to F$, the fibre product $h_X \times_F G$ is represented by a scheme $U$ and the induced morphism $U \to X$ is an open immersion.
A family of open subfunctors $\{G_i \to F\}$ is an \dfn{open cover} of $F$ if for every $h_X \to F$ the open subschemes $U_i \subseteq X$ representing $h_X \times_F G_i$ cover $X$.
:::

::: {.theorem title="Representability by gluing"}
Let $F$ be a Zariski sheaf with an open cover by open subfunctors $\{G_i \to F\}_{i \in I}$ such that each $G_i$ is represented by a scheme $X_i$.
Then $F$ is represented by a scheme $X$ covered by open subschemes isomorphic to the $X_i$.
:::

::: {.example}
The functor $\PP^n$ of [[FE-SCHREPFUNCTORS]] is a Zariski sheaf because line bundles and their sections glue.
For $0 \leq i \leq n$ the subfunctor $G_i$ of pairs $(\mathcal{L}, s_0, \ldots, s_n)$ in which $s_i$ generates $\mathcal{L}$ is open, its fibre product with $h_X$ being represented by the open set $X_{s_i} = \{x \in X : s_i(x) \neq 0\}$.
Each $G_i$ is represented by $\AA^n_\ZZ$, via $(\mathcal{L}, s) \mapsto (s_j/s_i)_{j \neq i}$, and the $G_i$ cover because generating sections have no common zero, so the theorem constructs $\PP^n_\ZZ$ by gluing $n+1$ copies of $\AA^n_\ZZ$.
:::
