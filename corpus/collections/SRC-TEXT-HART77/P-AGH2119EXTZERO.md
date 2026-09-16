---
schema: qual/card@1
id: P-AGH2119EXTZERO
kind: problem
title: Extending a sheaf by zero outside a closed or an open subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Extension By Zero
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Let $X$ be a topological space, let $Z$ be a closed subset with inclusion $i: Z \to X$, let $U = X \sm Z$ be the complementary open subset, and let $j: U \to X$ be its inclusion.

a. Let $\mcf$ be a sheaf on $Z$.
Show that the stalk $(i_* \mcf)_P$ of the direct image sheaf on $X$ is $\mcf_P$ if $P \in Z$ and $0$ if $P \notin Z$.
Hence $i_* \mcf$ is called the sheaf obtained by **extending $\mcf$ by zero outside $Z$**.

b. Now let $\mcf$ be a sheaf on $U$.
Let $j_!(\mcf)$ be the sheaf on $X$ associated to the presheaf $V \mapsto \mcf(V)$ if $V \subseteq U$ and $V \mapsto 0$ otherwise.
Show that the stalk $(j_!(\mcf))_P$ equals $\mcf_P$ if $P \in U$ and $0$ if $P \notin U$, and show that $j_! \mcf$ is the only sheaf on $X$ with this property whose restriction to $U$ is $\mcf$.
We call $j_! \mcf$ the sheaf obtained by **extending $\mcf$ by zero outside $U$**.

c. Now let $\mcf$ be a sheaf on $X$.
Show that there is an exact sequence of sheaves on $X$,
\[
0 \to j_!\qty{\ro{\mcf}{U}} \to \mcf \to i_*\qty{\ro{\mcf}{Z}} \to 0.
\]
:::
