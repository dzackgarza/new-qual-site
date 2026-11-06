---
schema: qual/card@1
id: P-AGH214IMSUBSHEAF
kind: problem
title: Sheafification preserves injectivity, and the image is a subsheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Subsheaves
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.4, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "(a) Let phi: F -> G be a morphism
    of presheaves such that phi(U): F(U) -> G(U) is injective for each U. Show
    that the induced map phi^+: F^+ -> G^+ of associated sheaves is injective.
    (b) Use part (a) to show that if phi: F -> G is a morphism of sheaves, then
    im phi can be naturally identified with a subsheaf of G, as mentioned in
    the text." The card states exactly this. The proof was checked: (a) passes
    to stalks, where the map is a colimit of the injective section maps, and
    sheafification preserves stalks; (b) applies (a) to the presheaf image.
    That a filtered colimit of injective abelian-group maps is injective is
    used, not reproved.
---


::: {.problem}
(a) Let $\varphi: \mcf \to \mcg$ be a morphism of presheaves such that $\varphi(U): \mcf(U) \to \mcg(U)$ is injective for each $U$.
Show that the induced map $\varphi^{+}: \mcf^{+} \to \mcg^{+}$ of associated sheaves is injective.

(b) Use part (a) to show that if $\varphi: \mcf \to \mcg$ is a morphism of sheaves, then $\im \varphi$ can be naturally identified with a subsheaf of $\mcg$.
:::

::: {.solution}
**Part (a).** A stalk is a filtered colimit of the groups of sections, and a filtered colimit of injections of abelian groups is injective.
So if $\phi(U)$ is injective for every $U$, then $\phi_P$ is injective for every $P$.
Sheafification does not change stalks, so $(\phi^+)_P = \phi_P$ is injective for every $P$, and by the stalkwise criterion for injectivity of a morphism of sheaves, $\phi^+$ is injective.

**Part (b).** The presheaf image $U \mapsto \im\qty{\phi(U)}$ is a subgroup of $\mcg(U)$ for every $U$, and the inclusions
$$
\psi(U): \im\qty{\phi(U)} \injects \mcg(U)
$$
are compatible with restriction, so they assemble into a morphism of presheaves $\psi$ into the sheaf $\mcg$.
Each $\psi(U)$ is injective, so by part (a) the induced map on associated sheaves is injective.
Since $\mcg$ is already a sheaf, the target of the sheafified map is $\mcg$ itself, and the source is $\im \phi$ by definition.
The restriction maps of $\im \phi$ are those induced from $\mcg$, so $\im \phi$ is identified with a subsheaf of $\mcg$.
:::
