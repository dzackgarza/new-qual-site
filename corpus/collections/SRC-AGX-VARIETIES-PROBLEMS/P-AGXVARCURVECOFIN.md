---
schema: qual/card@1
id: P-AGXVARCURVECOFIN
kind: problem
title: The Zariski topology on a curve is the cofinite topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Curves
  - Cofinite Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the recorded Zaidenberg source and its standing convention that k is
    algebraically closed of characteristic zero. Cross-checked the curve
    topology argument against P-AGH48CARDINALITY and D-BIVAU.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing base-field hypothesis explicit so that the
    standalone statement includes the assumption under which points of a
    variety are closed k-points.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the Noetherian irreducible-component decomposition, the dimension
    drop for proper irreducible closed subsets of a curve, and the converse
    that finite unions of closed k-points are closed.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero, and let $C$
be a curve over $k$. Show that the Zariski topology on $C$ is the cofinite
topology.
:::

::: {.solution}

::: pf

::: {.pf-step #proper-closed-finite}
Every proper Zariski closed subset of $C$ is finite.

::: pf-proof
Let
$$
Z\subsetneq C
$$
be Zariski closed. A variety is Noetherian, so $Z$ has only finitely many
irreducible components:
$$
Z=Z_1\cup\cdots\cup Z_r.
$$

The curve $C$ is irreducible of dimension $1$. Each $Z_i$ is an irreducible
proper closed subset of $C$, so
$$
\dim Z_i<\dim C=1.
$$
Hence
$$
\dim Z_i=0.
$$
Choose $p\in Z_i$. Since $k$ is algebraically closed, $\{p\}$ is a closed
irreducible subset of $Z_i$. If
$$
\{p\}\subsetneq Z_i,
$$
this would be a strict chain of nonempty irreducible closed subsets of length
$1$, contradicting $\dim Z_i=0$. Thus $Z_i=\{p\}$. Therefore every $Z_i$ is
a point, and $Z$ is finite.
:::

:::

::: {.pf-step #finite-subsets-closed}
Every finite subset of $C$ is Zariski closed.

::: pf-proof
Since $k$ is algebraically closed, every point of a $k$-variety is a closed
point. Thus every singleton
$$
\{p\}\subseteq C
$$
is Zariski closed. A finite union of closed subsets is closed, so every finite
subset of $C$ is Zariski closed.
:::

:::

::: {.pf-step #closed-subsets-characterization}
The Zariski closed subsets of $C$ are exactly $C$ and its finite
subsets.

::: pf-proof
Step [](#proper-closed-finite){.pf-ref} shows that every proper closed subset is finite. Step [](#finite-subsets-closed){.pf-ref} shows
that every finite subset is closed. Together with $C$ itself, these are
precisely the closed subsets.
:::

:::

::: {.pf-step #cofinite-topology-conclusion}
Therefore the Zariski topology on $C$ is the cofinite topology.

::: pf-proof
By definition, the cofinite topology is the topology whose closed subsets are
the whole space and the finite subsets. Step [](#closed-subsets-characterization){.pf-ref} gives exactly this
description for the Zariski topology on $C$.
:::

:::

::: pf-qed
Step [](#cofinite-topology-conclusion){.pf-ref} is the required conclusion.
:::

:::

:::
