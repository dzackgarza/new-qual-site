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
---


::: {.problem}
Let $A$ be an abelian group and let $X$ be a topological space.
Define the \dfn{constant presheaf} associated to $A$ on $X$ to be the presheaf $U \mapsto A$ for all $U \neq \varnothing$, with all restriction maps the identity.
Show that the constant sheaf $\mca$ defined in the text is the sheaf associated to this presheaf.

Recall that the constant sheaf $\mca$ of the text is defined by giving $A$ the discrete topology and setting $\mca(U)$ to be the group of continuous maps $U \to A$.
:::

::: {.solution}
Write $\tilde\mca$ for the constant presheaf of the question and $\mca$ for the sheaf of the text.

Set $\tilde\mca(\varnothing)=0$. Define a morphism of presheaves $F: \tilde\mca \to \mca$ by giving, for each nonempty open $U$, the map
$$
F_U: \tilde\mca(U) = A \to \mca(U) = C^0(U, A)
$$
which sends $a \in A$ to the constant function with value $a$.
On the empty open set, $F_\varnothing$ is the unique map between zero groups.
Since $A$ carries the discrete topology, every constant function is continuous, so $F_U$ lands in $\mca(U)$.
The maps $F_U$ are compatible with restriction, because restricting a constant function gives the constant function with the same value, so $F$ is a morphism of presheaves.

Now compare stalks.
For every $p \in X$ we have $\tilde\mca_p = A$, since every restriction map of $\tilde\mca$ is the identity.
On the other side, a continuous map from a small enough neighbourhood of $p$ into the discrete group $A$ is constant near $p$, so $\mca_p = A$ as well, and $F_p: A \to A$ is the identity.
Thus $F_p$ is an isomorphism for every $p$.

A morphism of presheaves which is an isomorphism on all stalks induces an isomorphism on the associated sheaves.
By the universal property of sheafification, $F$ factors through $(\tilde\mca)^+$, and the induced map $(\tilde\mca)^+ \to \mca$ is an isomorphism on stalks between two sheaves, hence an isomorphism.
So $\mca$ is the sheafification of the constant presheaf.
:::
