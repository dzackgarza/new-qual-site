---
schema: qual/card@1
id: P-TOPS24D
kind: problem
title: Homology of the cube with opposite faces glued by 180° rotations
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $X$ be the space obtained by gluing opposite pairs of faces of a standard cube $I^3$ via 180 degree rotations, as shown.
Compute the homology $H_*(X; \mathbb{Z})$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$X$ has one $0$-cell, three $1$-cells, three $2$-cells, one $3$-cell.

::: pf-proof

the cube has 8 vertices identified to one, 12 edges identified into 3 classes of 4 parallel edges, 6 faces identified into 3 pairs.

:::

:::

::: {.pf-step #s2}

Cellular chain complex: $0 \to \mathbb{Z} \xrightarrow{\partial_3} \mathbb{Z}^3 \xrightarrow{\partial_2} \mathbb{Z}^3 \xrightarrow{\partial_1} \mathbb{Z} \to 0$.

::: pf-proof

Step [](#s1){.pf-ref}.

:::

:::

::: pf-step

$\partial_1 =0$ (single $0$-cell).

::: pf-proof

each $1$-cell is a loop.

:::

:::

::: {.pf-step #s4}

Each $2$-cell is attached with degree $2$ (the $180^\circ$ rotation identifies opposite edges with a twist, giving boundary $2\cdot$generator).

::: pf-proof

the gluing map has degree $2$ on the $1$-skeleton.

:::

:::

::: {.pf-step #s5}

Hence $\partial_2$ is multiplication by $2$ on each $2$-cell.

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

$\partial_3 =0$ (the $3$-cell is attached by a map of degree $0$ for this orientable gluing).

::: pf-proof

orientability.

:::

:::

::: {.pf-step #s7}

Therefore $H_0(X)=\mathbb{Z}$, $H_1(X)=\mathbb{Z}^3/2\mathbb{Z}^3 \cong (\mathbb{Z}/2)^3$, $H_2(X)=0$, $H_3(X)=\mathbb{Z}$.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}; $H_1 = \ker\partial_1/\operatorname{im}\partial_2 = \mathbb{Z}^3/2\mathbb{Z}^3$, $H_2 = \ker\partial_2/\operatorname{im}\partial_3 =0$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
