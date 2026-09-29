---
schema: qual/card@1
id: E-T7PYZ
kind: problem
title: $\RR$ with the cofinite topology is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that $\RR$ with the cofinite topology is compact.
:::

::: {.solution}
**Goal:** Show that $\RR$ with the cofinite topology is compact.

::: pf

::: {.pf-step #s1}

Let $\mathcal{U} = \theset{U_\alpha}_{\alpha \in I}$ be an open cover of $\RR$ (cofinite topology).

::: pf-proof

Arbitrary open cover.

:::

:::

::: {.pf-step #s2}

Pick a nonempty member $U_0$ of the cover.

::: pf-proof

The cover is nonempty because $\RR \neq \emptyset$; and since the cover covers $\RR$, some $U_0$ contains a point, hence is nonempty.

(If $U_0$ were empty it still exists; choose one that is nonempty since the union is all of $\RR$.)

:::

:::

::: {.pf-step #s3}

The complement $\RR \setminus U_0$ is finite: $\RR \setminus U_0 = \theset{x_1, \ldots, x_n}$.

::: pf-proof

Definition of the cofinite topology: nonempty open sets have finite complement.

:::

:::

::: {.pf-step #s4}

For each $j = 1, \ldots, n$, choose $U_j \in \mathcal{U}$ with $x_j \in U_j$.

::: pf-proof

$\mathcal{U}$ covers $\RR$.

:::

:::

::: {.pf-step #s5}

$\theset{U_0, U_1, \ldots, U_n}$ is a finite subcover of $\RR$.

::: pf-proof

$U_0$ covers everything except $\theset{x_1, \ldots, x_n}$, and each $x_j$ is covered by $U_j$ (step [](#s4){.pf-ref}).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} show every open cover of $\RR$ (cofinite) has a finite subcover.

:::

:::

:::
