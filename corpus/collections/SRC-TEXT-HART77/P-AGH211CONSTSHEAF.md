---
schema: qual/card@1
id: P-AGH211CONSTSHEAF
kind: problem
title: The constant sheaf is the sheafification of the constant presheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Stalks
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.1, printed page 65 (PDF page 80 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "Let A be an abelian group, and
    define the constant presheaf associated to A on the topological space X to
    be the presheaf U -> A for all U nonempty, with restriction maps the
    identity. Show that the constant sheaf A defined in the text is the sheaf
    associated to this presheaf." The card states exactly this; its added
    "Recall that ..." sentence restates the text's definition of the constant
    sheaf and adds no hypothesis. The proof was read and checked: the presheaf
    map a -> constant function is well defined because A is discrete, compatible
    with restriction, and its stalk map is the identity since a continuous map
    into a discrete group is locally constant. Not checked: the universal
    property of sheafification is used as the text states it, not re-proved.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into a Lamport proof, mathematics unchanged: the four paragraphs are now five
    numbered steps — the presheaf morphism with continuity of constant maps, the computation of
    both stalks with the bijection from A to the stalk of the constant sheaf and its inverse,
    the passage to sheafification with the stalkwise criterion for an isomorphism of sheaves,
    and the conclusion — with the citation to Kim's set (Chapter II §1, Exercise 1.1, PDF p. 2)
    moved to the head of the solution so that the proof it supports is attributed where it is
    read. The remark after the solution, which records the same attribution and the two
    implicit points, is unchanged. Nothing was re-derived; the statement is unchanged.
---


::: {.problem}
Let $A$ be an abelian group and let $X$ be a topological space.
Define the \dfn{constant presheaf} associated to $A$ on $X$ to be the presheaf $U \mapsto A$ for all $U \neq \varnothing$, with all restriction maps the identity.
Show that the constant sheaf $\mca$ defined in the text is the sheaf associated to this presheaf.

Recall that the constant sheaf $\mca$ of the text is defined by giving $A$ the discrete topology and setting $\mca(U)$ to be the group of continuous maps $U \to A$.
:::

::: {.solution}
The published solution is **Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II–III), Chapter II §1, Exercise 1.1, PDF p. 2** (`tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`): he maps the constant presheaf into the constant sheaf of the text by sending $a$ to the constant function with value $a$, notes that the induced map is an isomorphism on every stalk, and concludes from the universal property of sheafification that $(\tilde\mca)^{+}\to\mca$ is an isomorphism. The two points he leaves implicit are supplied here: constant maps into the discrete group $A$ are continuous, and a continuous map from a neighbourhood of a point into a discrete group is constant near that point.

Throughout $X$ is a topological space, $A$ an abelian group with the discrete topology, $\tilde\mca$ the constant presheaf $U\mapsto A$ for $U\ne\varnothing$ with identity restrictions, set to $\tilde\mca(\varnothing)=0$, and $\mca$ the sheaf $U\mapsto C^0(U,A)$ of the text.

::: pf

::: {.pf-step #presheaf-map}
There is a morphism of presheaves $F:\tilde\mca\to\mca$ with $F_U(a)$ the constant function of value $a$.

::: pf-proof
For nonempty open $U$ let $F_U:A\to C^0(U,A)$, $a\mapsto(u\mapsto a)$. Because $A$ is discrete, the preimage of a point is either $U$ or $\varnothing$, so every constant map is continuous and $F_U$ is well defined; it is a homomorphism of groups. For open $V\subseteq U$ and $a\in A$, restricting the constant function $a$ on $U$ to $V$ gives the constant function $a$ on $V$, which is $F_V(a)$; so the $F_U$ commute with restriction. On $\varnothing$ the source is $0$ and there is a unique map to $\mca(\varnothing)=C^0(\varnothing,A)$.

:::

:::

::: {.pf-step #stalks}
$\tilde\mca_P\cong A\cong\mca_P$ for every $P\in X$, and $F_P$ is an isomorphism.

::: pf-proof
All restriction maps of $\tilde\mca$ are identities and the groups are all $A$, so the filtered colimit over the open neighbourhoods of $P$ is $A$ and $F_P$ is induced by identity maps. For $\mca$: a germ at $P$ is represented by a continuous $s:U\to A$; since $A$ is discrete, $s^{-1}(s(P))$ is open and nonempty, so on the neighbourhood $s^{-1}(s(P))$ the section $s$ is the constant map of value $s(P)$, which is the germ of an element of $A$ under $F$. Two continuous maps agreeing at $P$ have the same value there, so the map $a\mapsto$ germ of the constant function $a$ is a bijection $A\to\mca_P$, and it is inverse to the map induced by $F$. Hence $\mca_P\cong A$ and $F_P$ is an isomorphism.

:::

:::

::: {.pf-step #sheafification}
The map $F^{+}:\tilde\mca^{+}\to\mca^{+}=\mca$ induced by $F$ is an isomorphism.

::: pf-proof
Sheafification is left adjoint to the inclusion of sheaves in presheaves, so $F$ induces $F^{+}:\tilde\mca^{+}\to\mca^{+}$, and $\mca^{+}\cong\mca$ since $\mca$ is a sheaf. Sheafification preserves stalks, so $(F^{+})_P=F_P$ by step [](#stalks){.pf-ref}, which is an isomorphism. A morphism of sheaves that is an isomorphism on every stalk is an isomorphism: it is injective and surjective on sections (a nonzero section of the kernel or a class in the cokernel would give a nonzero element of some stalk). Hence $F^{+}$ is an isomorphism.

:::

:::

::: {.pf-step #conclusion}
$\mca$ is the sheaf associated to the constant presheaf $\tilde\mca$.

::: pf-proof
The sheaf associated to a presheaf is unique up to unique isomorphism, and step [](#sheafification){.pf-ref} exhibits an isomorphism $\tilde\mca^{+}\cong\mca$; that is the assertion.

:::

:::

:::
:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 65 of Hartshorne, the first exercise of §II.1, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$; the statement above is that page's text, the constant presheaf associated to an abelian group $A$ and its sheafification included.

Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.1, PDF p. 2, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he maps the constant presheaf into the constant sheaf of the text by sending $a$ to the constant function with value $a$, notes that the induced map is an isomorphism on every stalk, and concludes from the universal property of sheafification that $(\tilde\mca)^{+}\to\mca$ is an isomorphism.
The proof above is the same argument with the two points Kim leaves implicit supplied: constant maps into the discrete group $A$ are continuous, so the presheaf map lands in $\mca(U)$, and a continuous map from a neighbourhood of a point into a discrete group is constant near that point, which is what gives $\tilde\mca_P=\mca_P=A$.
Agree.
:::
