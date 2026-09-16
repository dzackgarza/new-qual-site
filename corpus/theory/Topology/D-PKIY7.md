---
schema: qual/card@1
id: D-PKIY7
kind: definition
title: Projective resolution
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring and $M$ an $R$-module.
A \dfn{projective resolution} of $M$ is an [[D-BJYH3|exact sequence]] of $R$-modules
$$
\cdots\to P_2\mapsvia{d_2}P_1\mapsvia{d_1}P_0\mapsvia{\varepsilon}M\to0
$$
in which every $P_i$ is a [[D-DEFPROJO|projective module]].
It is a \dfn{free resolution} if every $P_i$ is a [[D-LIEMF|free module]].
:::

::: {.proposition}
Let $R$ be a ring and $M$ an $R$-module.

(a) $M$ has a free resolution, and hence a projective resolution.

(b) If $P_\bullet\to M$ and $Q_\bullet\to M$ are projective resolutions, there is a chain map $P_\bullet\to Q_\bullet$ over $\id_M$, and any such chain map is a chain homotopy equivalence [@Hat02, pp. 193--195].
:::

::: {.remark}
Let $R$ be commutative and $N$ an $R$-module.
By (b), the cohomology of the cochain complex $\Hom_R(P_\bullet,N)$ and the homology of the chain complex $P_\bullet\otimes_RN$ do not depend on the projective resolution $P_\bullet$ of $M$, up to canonical isomorphism; they are $\Ext^n_R(M,N)$ and $\Tor_n^R(M,N)$.
:::
