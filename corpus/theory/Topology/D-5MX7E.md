---
schema: qual/card@1
id: D-5MX7E
kind: definition
title: Colimit
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $\mathcal C$ be a category, $I$ a small category, and $F\colon I\to\mathcal C$ a functor.
A \dfn{cocone} on $F$ is an object $Y$ of $\mathcal C$ with morphisms $\psi_i\colon F(i)\to Y$ for $i\in I$ such that $\psi_j\circ F(u) = \psi_i$ for every morphism $u\colon i\to j$ in $I$.
A \dfn{colimit} of $F$ is a cocone $(X, (\iota_i)_{i\in I})$ such that for every cocone $(Y, (\psi_i)_{i\in I})$ there exists a unique morphism $\varphi\colon X\to Y$ with $\varphi\circ\iota_i = \psi_i$ for all $i\in I$.
:::

::: {.remark}
A colimit is unique up to unique isomorphism compatible with the maps $\iota_i$, and is written $\colim_I F$.
Reversing all arrows gives the dual notion, a [[D-QXER7|limit]].
:::

::: {.example}
The following constructions are colimits.

- A [[D-COC6C|coproduct]] $\Disjoint_{i\in I} X_i$ is the colimit of a functor on a category $I$ with no non-identity morphisms.

- The [[D-5S7PK|pushout]] of $X \leftarrow Z \to Y$ is the colimit of that diagram.

- The [[D-NODFN|direct limit]] of a directed system $(A_\alpha, f_{\alpha\beta})$ is its colimit.

- In abelian groups, $\ZZ[1/p] \cong \colim\qty{\ZZ \mapsvia{p} \ZZ \mapsvia{p} \ZZ \mapsvia{p} \cdots}$, with the $k$th copy of $\ZZ$, for $k\geq 0$, mapped to $\ZZ[1/p]$ by $1\mapsto p^{-k}$.
:::

::: {.concept}
[@Wei94].
:::
