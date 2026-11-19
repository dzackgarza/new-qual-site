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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into a Lamport proof, mathematics unchanged: (a) is now the filtered-colimit
    injectivity with its one-line argument and then the stalkwise criterion, and (b) is the
    presheaf image with the compatibility of the inclusions checked, followed by part (a) and
    the identification of the target with the sheaf. The citation of Kim's set (Chapter II §1,
    Exercise 1.4, PDF p. 3) is moved from the remark to the head of the solution. Not proved,
    as before: the filtered-colimit statement and the stalkwise criterion, which are named.
    The remark and the statement are unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into a Lamport proof, mathematics unchanged: (a) is now the filtered-colimit
    injectivity with its one-line argument and then the stalkwise criterion, and (b) is the
    presheaf image with the compatibility of the inclusions checked, followed by part (a) and
    the identification of the target with the sheaf. The citation of Kim's set (Chapter II §1,
    Exercise 1.4, PDF p. 3) is moved from the remark to the head of the solution. Not proved,
    as before: the filtered-colimit statement and the stalkwise criterion, which are named.
    The remark and the statement are unchanged.
---


::: {.problem}
(a) Let $\varphi: \mcf \to \mcg$ be a morphism of presheaves such that $\varphi(U): \mcf(U) \to \mcg(U)$ is injective for each $U$.
Show that the induced map $\varphi^{+}: \mcf^{+} \to \mcg^{+}$ of associated sheaves is injective.

(b) Use part (a) to show that if $\varphi: \mcf \to \mcg$ is a morphism of sheaves, then $\im \varphi$ can be naturally identified with a subsheaf of $\mcg$.
:::

::: {.solution}
The published solution is **Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II–III), Chapter II §1, Exercise 1.4, PDF p. 3** (`tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`, the revision the card's remark records): he passes to stalks, where the map is a filtered colimit of the injective section maps and hence injective, and then uses that sheafification preserves stalks; (b) is the injection of the presheaf image into $\mcg$ taken after sheafification. The proof below is that argument with the filtered-colimit statement named rather than used silently.

Throughout $\varphi:\mcf\to\mcg$ is a morphism of presheaves on a space $X$, $\mcf^{+}$ denotes the associated sheaf, and $\varphi_P$ is the induced map of stalks at $P$.

::: pf

::: {.pf-step #stalk-injective}
If $\varphi(U)$ is injective for every $U$, then $\varphi_P$ is injective for every $P$.

::: pf-proof
The stalk at $P$ is the filtered colimit $\varinjlim_{U\ni P}\mcf(U)$ over the open neighbourhoods of $P$, ordered by reverse inclusion, and $\varphi_P$ is the colimit of the maps $\varphi(U)$. A filtered colimit of injective maps of abelian groups is injective: if $\varphi_P(x)=0$ for a class $x$ represented by $s\in\mcf(U)$, then $\varphi(U)(s)$ is carried to $0$ in some smaller stage $\mcg(V)$, $V\subseteq U$, $V\ni P$, and injectivity of $\varphi(V)$ gives $\restrictionof{s}{V}=0$, so $x=0$ in the colimit.

:::

:::

::: {.pf-step #part-a}
$\varphi^{+}:\mcf^{+}\to\mcg^{+}$ is injective.

::: pf-proof
Sheafification preserves stalks, $(\varphi^{+})_P=\varphi_P$ under the canonical identifications, and that map is injective by step [](#stalk-injective){.pf-ref}. A morphism of sheaves is injective iff it is injective on every stalk — a nonzero section of the kernel presheaf has a nonzero germ at some point, and a presheaf whose stalks all vanish sheafifies to $0$ — so $\varphi^{+}$ is injective.

:::

:::

::: {.pf-step #presheaf-image}
For $\varphi:\mcf\to\mcg$ a morphism of sheaves, $U\mapsto\im\varphi(U)$ is a presheaf and the inclusions $\psi(U):\im\varphi(U)\hookrightarrow\mcg(U)$ form a morphism of presheaves, injective at every $U$.

::: pf-proof
$\im\varphi(U)$ is a subgroup of $\mcg(U)$. If $s=\varphi(U)(t)$ and $V\subseteq U$, then $\restrictionof{s}{V}=\varphi(V)(\restrictionof{t}{V})$ by compatibility of $\varphi$ with restriction, so $\restrictionof{s}{V}\in\im\varphi(V)$: the assignment is a presheaf, with the restrictions of $\mcg$. The $\psi(U)$ are the inclusions, they commute with restriction because restriction in the subpresheaf is the restriction in $\mcg$, and each is injective.

:::

:::

::: {.pf-step #part-b}
$\im\varphi$, the associated sheaf of the presheaf image, is naturally a subsheaf of $\mcg$.

::: pf-proof
Apply part (a) to $\psi$: since each $\psi(U)$ is injective by step [](#presheaf-image){.pf-ref}, the induced $\psi^{+}:\bigl(U\mapsto\im\varphi(U)\bigr)^{+}\to\mcg^{+}$ is injective. The target $\mcg^{+}$ is $\mcg$ itself because $\mcg$ is a sheaf. By definition $\im\varphi$ is the associated sheaf of the presheaf $U\mapsto\im\varphi(U)$, so $\psi^{+}$ is an injective morphism $\im\varphi\to\mcg$, i.e. an identification of $\im\varphi$ with a subsheaf of $\mcg$; its restriction maps are those induced from $\mcg$, so the identification is natural.

:::

:::

:::
:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 66 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$; the statement above is that page's text, both parts -- the criterion for a morphism of presheaves to be injective on every open set, and the description of the image presheaf and its sheafification.

Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.4, PDF p. 3, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he passes to stalks, where the map is a filtered colimit of the injective section maps and hence injective, and then uses that sheafification preserves stalks; (b) is the injection of the presheaf image into $\mcg$ taken after sheafification.
The proof above is that argument, with the filtered-colimit statement named rather than proved.
Agree.
:::
