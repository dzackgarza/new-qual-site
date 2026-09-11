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
---

::: problem
Let $A$ be an abelian group and let $X$ be a topological space.
Define the **constant presheaf** associated to $A$ on $X$ to be the presheaf $U \mapsto A$ for all $U \neq \varnothing$, with all restriction maps the identity.
Show that the constant sheaf $\mca$ defined in the text is the sheaf associated to this presheaf.

Recall that the constant sheaf $\mca$ of the text is defined by giving $A$ the discrete topology and setting $\mca(U)$ to be the group of continuous maps $U \to A$.
:::

::: solution
Write $\tilde\mca$ for the constant presheaf of the question and $\mca$ for the sheaf of the text.

Define a morphism of presheaves $F: \tilde\mca \to \mca$ by giving, for each open $U$, the map
\[
F_U: \tilde\mca(U) = A \to \mca(U) = C^0(U, A)
\]
which sends $a \in A$ to the constant function with value $a$.
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
