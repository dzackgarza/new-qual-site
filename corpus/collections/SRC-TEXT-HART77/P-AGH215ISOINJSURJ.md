---
schema: qual/card@1
id: P-AGH215ISOINJSURJ
kind: problem
title: A morphism of sheaves is an isomorphism exactly when it is injective and surjective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Exact Sequences
  - Stalks
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.5, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "Show that a morphism of sheaves
    is an isomorphism if and only if it is both injective and surjective." The
    card states exactly this. The proof was checked: injective plus surjective
    is exactness of 0 -> F -> G -> 0, which by exercise 1.2 is exactness on
    stalks, hence every phi_P is an isomorphism; conversely an isomorphism on
    stalks gives injectivity on sections and local liftability of sections of
    G, and the lifts agree on overlaps by injectivity, so they glue and the
    sectionwise inverses are compatible with restriction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into a Lamport proof, mathematics unchanged and one gap filled: the previous
    prose said that surjectivity on stalks lets one lift locally "and then glue the lifts, which
    are unique by the injectivity just established", without separating the two directions. The
    card now proves injectivity on sections from injectivity on stalks through the
    germ-comparison map of a sheaf, then surjectivity on sections by lifting over a cover,
    gluing, and using the injectivity just proved on the overlaps; the inverse morphism is
    constructed from the sectionwise inverses with compatibility checked. The citation of Kim's
    set (Chapter II §1, Exercise 1.5, PDF p. 3) is moved from the remark to the head of the
    solution. Statement unchanged.
---


::: {.problem}
Show that a morphism of sheaves is an isomorphism if and only if it is both injective and surjective.
:::

::: {.solution}
The published solution is **Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II–III), Chapter II §1, Exercise 1.5, PDF p. 3** (`tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`): he identifies injective together with surjective with exactness of $0\to\mcf\to\mcg\to0$, which by Exercise 1.2 is exactness of every stalk sequence and hence bijectivity of every $\phi_P$; the converse builds the inverse on sections by lifting with Exercise 1.3 and gluing. The proof below adds the uniqueness of the lifts, which is what makes the local inverses glue.

Throughout $\phi:\mcf\to\mcg$ is a morphism of sheaves of abelian groups on a space $X$, and $\phi_P$ is the induced map of stalks at $P$.

::: pf

::: {.pf-step #exactness}
$\phi$ is injective and surjective iff $0\to\mcf\xrightarrow{\phi}\mcg\to0$ is exact as a sequence of sheaves.

::: pf-proof
A morphism of sheaves is injective when $\ker\phi=0$ as a sheaf and surjective when $\im\phi=\mcg$; $\ker\phi$ and $\im\phi$ are the sheaves associated to the presheaves $U\mapsto\ker\phi(U)$, $U\mapsto\im\phi(U)$ (Exercise 1.4). The sequence is exact at $\mcf$ iff the kernel is $0$ and exact at $\mcg$ iff the image is $\mcg$; combined with exactness at the middle term, that is the assertion.

:::

:::

::: {.pf-step #stalkwise}
$0\to\mcf\to\mcg\to0$ is exact iff $0\to\mcf_P\xrightarrow{\phi_P}\mcg_P\to0$ is exact for every $P\in X$.

::: pf-proof
This is Exercise 1.2: a sequence of sheaves is exact iff its stalk sequence is exact at every point, because the stalk functor is exact and a morphism of sheaves whose stalks all vanish is zero.

:::

:::

::: {.pf-step #forward}
If $\phi$ is injective and surjective then every $\phi_P$ is an isomorphism.

::: pf-proof
By steps [](#exactness){.pf-ref} and [](#stalkwise){.pf-ref}, every $\phi_P$ is injective and surjective as a map of abelian groups, hence an isomorphism.

:::

:::

::: {.pf-step #injectivity-criterion}
If every $\phi_P$ is injective then $\phi$ is injective.

::: pf-proof
Let $s\in\mcf(U)$ with $\phi(U)(s)=0$. Its germ $s_P$ satisfies $\phi_P(s_P)=0$, so $s_P=0$ for every $P\in U$ by injectivity of $\phi_P$. A section of a sheaf all of whose germs vanish is zero, because the map $\mcf(U)\to\prod_{P\in U}\mcf_P$, $s\mapsto(s_P)$, is injective: a cover of $U$ by open sets on which the representative of the zero germ vanishes exhibits $s$ as locally zero, and a sheaf has no nonzero locally zero sections. Hence $s=0$ and $\phi(U)$ is injective for every $U$.

:::

:::

::: {.pf-step #surjectivity-criterion}
If every $\phi_P$ is surjective then $\phi$ is surjective.

::: pf-proof
Let $t\in\mcg(U)$. For each $P\in U$ choose a neighbourhood $U_P\subseteq U$ of $P$ and $s_P\in\mcf(U_P)$ with $\phi(U_P)(s_P)=\restrictionof{t}{U_P}$; such a pair exists because the germ $t_P$ is $\phi_P(x)$ for some $x$, represented by such an $s_P$. On an overlap $U_P\cap U_Q$ the two sections $s_P,s_Q$ have equal images under $\phi$, hence are equal by step [](#injectivity-criterion){.pf-ref} applied to the sheaf $\mcf$ over the open set $U_P\cap U_Q$. The sheaf axiom for $\mcf$ then glues the $s_P$ to a single $s\in\mcf(U)$, and $\phi(U)(s)=t$ because the two agree on a neighbourhood of every point. So $\phi(U)$ is surjective for every $U$.

:::

:::

::: {.pf-step #conclusion}
A morphism of sheaves is an isomorphism iff it is injective and surjective.

::: pf-proof
If $\phi$ is injective and surjective, then $\phi(U)$ is a bijection for every $U$ by steps [](#injectivity-criterion){.pf-ref} and [](#surjectivity-criterion){.pf-ref}, and the inverse maps $\phi(U)^{-1}$ are compatible with restriction: for $V\subseteq U$ and $t\in\mcg(U)$, both $\restrictionof{\phi(U)^{-1}(t)}{V}$ and $\phi(V)^{-1}(\restrictionof{t}{V})$ map to $\restrictionof{t}{V}$ under $\phi(V)$ and $\phi(V)$ is injective, so they agree. Hence they define a morphism of sheaves $\mcg\to\mcf$ inverse to $\phi$, and $\phi$ is an isomorphism. The converse is immediate.

:::

:::

:::
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.5, PDF p. 3, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he identifies injective together with surjective with exactness of $0\to\mcf\to\mcg\to0$, which by Exercise 1.2 is exactness of every stalk sequence and hence bijectivity of every $\phi_P$; the converse builds the inverse on sections by lifting with Exercise 1.3 and gluing.
The proof above is that argument, with the uniqueness of the lifts used explicitly so that the local inverses glue.
Agree.
:::
