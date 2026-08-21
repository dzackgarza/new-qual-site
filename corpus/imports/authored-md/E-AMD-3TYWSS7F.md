---
schema: qual/card@1
id: E-AMD-3TYWSS7F
kind: exercise
title: Nilpotent groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that $G$ nilpotent $\implies G$ solvable.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a nilpotent group.
By definition, $G$ possesses a finite central series terminating at the identity:
$$
1 = Z_0 \normal Z_1 \normal Z_2 \normal \cdots \normal Z_c = G,
$$
where each subgroup $Z_{i+1}$ satisfies:
$$
Z_{i+1} / Z_i \subseteq Z(G / Z_i).
$$
In particular, since $Z_{i+1}/Z_i$ is a subgroup of the center $Z(G/Z_i)$, every element of $Z_{i+1}/Z_i$ commutes with every element of $G/Z_i$.
Therefore, the quotient group $Z_{i+1} / Z_i$ is **abelian** for each $i \in \{0, 1, \ldots, c-1\}$.

Recall the definition of a solvable group: A group $G$ is **solvable** if it has a finite subnormal series (an abelian series):
$$
1 = G_0 \normal G_1 \normal G_2 \normal \cdots \normal G_k = G
$$
such that each successive quotient $G_{i+1}/G_i$ is abelian.

The central series $1 = Z_0 \normal Z_1 \normal \cdots \normal Z_c = G$ is precisely such a series with abelian quotients $Z_{i+1}/Z_i$.
Thus, every nilpotent group is solvable.

*(Note: The converse is false in general; for example, the symmetric group $S_3$ is solvable with derived series $1 \normal A_3 \normal S_3$, but not nilpotent because $Z(S_3) = 1$.)*
:::
