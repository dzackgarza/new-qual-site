---
schema: qual/card@1
id: L-Q44MT
kind: lemma
title: Finite $p$-groups are solvable
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
relations: []
review: draft
---

::: {.lemma}
Let $p$ be a prime.
Every finite [[D-FIB7S|$p$-group]] is [[D-DFIDP|solvable]].
:::

::: {.proof}
Induct on $\abs G$; the trivial group is solvable.
A nontrivial finite $p$-group $G$ has nontrivial [[D-NK7G7|center]] $Z(G)$ by the class equation.
The quotient $G/Z(G)$ is a $p$-group of smaller order, hence solvable by induction, and $Z(G)$ is an abelian normal subgroup.
Pulling back a normal series of $G/Z(G)$ with abelian factors to $G$ and appending $Z(G)\trianglerighteq\theset{e}$ gives a normal series of $G$ with abelian factors.
:::
