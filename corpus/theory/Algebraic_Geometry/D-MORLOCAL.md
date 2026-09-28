---
schema: qual/card@1
id: D-MORLOCAL
kind: definition
title: Classes of morphisms stable under base change and local on the source or target
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Base Change
  - Grothendieck Topologies
relations:
- kind: uses
  target: D-SCHBC
- kind: related-to
  target: PR-MORBC
review: draft
prompts:
- What does it mean for a property of morphisms to be local on the target? Local on the source?
- What does it mean for a class of morphisms to be stable under base change and composition?
- What is an affine-local property?
---

::: {.definition title="Stability"}
Let $P$ be a class of morphisms of schemes.

- $P$ is \dfn{stable under base change} if for every $f \colon X \to Y$ in $P$ and every morphism $g \colon Y' \to Y$, the base change $X \times_Y Y' \to Y'$ is in $P$.

- $P$ is \dfn{stable under composition} if $f \colon X \to Y$ and $g \colon Y \to Z$ in $P$ imply $g \circ f \in P$.
:::

::: {.remark}
If $P$ contains every isomorphism and is stable under composition, the schemes together with the morphisms in $P$ form a subcategory $\Sch_P \subseteq \Sch$ with the same objects.
:::

::: {.definition title="Locality for the Zariski topology"}
Let $P$ be a class of morphisms of schemes.

- $P$ is \dfn{local on the target} if for every morphism $f \colon X \to Y$ and every open cover $Y = \bigcup_i V_i$: $f \in P$ if and only if every restriction $f^{-1}(V_i) \to V_i$ is in $P$.

- $P$ is \dfn{local on the source} if for every morphism $f \colon X \to Y$ and every open cover $X = \bigcup_i U_i$: $f \in P$ if and only if every restriction $f|_{U_i} \colon U_i \to Y$ is in $P$.

- $P$ is \dfn{affine-local on the target} if for every morphism $f \colon X \to Y$ and every cover of $Y$ by affine opens $V_i$: $f \in P$ if and only if every $f^{-1}(V_i) \to V_i$ is in $P$; so a single affine cover of $Y$ decides membership. \dfn{Affine-local on the source} is defined in the same way with affine covers of $X$.
:::

::: {.definition title="Locality for a Grothendieck topology"}
Let $\tau$ be the Zariski, étale, smooth or fppf topology.
A class $P$ of morphisms is \dfn{$\tau$-local on the target} if for every $f \colon X \to Y$ and every $\tau$-covering $\{Y_i \to Y\}$, $f \in P$ if and only if every base change $X \times_Y Y_i \to Y_i$ is in $P$.
It is \dfn{$\tau$-local on the source} if for every $f \colon X \to Y$ and every $\tau$-covering $\{X_i \to X\}$, $f \in P$ if and only if every composite $X_i \to X \to Y$ is in $P$.
For the Zariski topology these are the notions above.
:::

::: {.example}
Affine morphisms are stable under base change and composition and local on the target ([[D-MORAFF]]), but not local on the source: for a field $k$, $X = \AA^2_k \setminus \{0\}$ is covered by the affine opens $D(x)$ and $D(y)$, each affine over $\Spec k$, while $X \to \Spec k$ is not affine because $X$ is not an affine scheme.
:::

::: {.example}
Closed immersions are local on the target but not on the source: $\Spec k \sqcup \Spec k \to \Spec k$ restricts to an isomorphism on each of the two open components, but it is not injective, so it is not a closed immersion.
:::

::: {.example}
Flat morphisms and morphisms locally of finite presentation are local on the source and on the target for the fppf topology; smooth and étale morphisms are local on the source for the étale topology and local on the target for the fppf topology.
Proper and separated morphisms are local on the target for the fppf topology and are not local on the source: $\PP^1_k$ is covered by two copies of $\AA^1_k$, and $\AA^1_k \to \Spec k$ is not proper.
:::
