---
schema: qual/card@1
id: E-T7PYZ
kind: exercise
title: "Show that $\\RR$ with the cofinite topology is compact."
classification:
  areas:
  - topology
  topics:
  - compactness
  - point-set
relations: []
review: draft
---

::: exercise
Show that $\RR$ with the cofinite topology is compact.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that $\RR$ with the cofinite topology is compact.

<1>1. Let $\mathcal{U} = \theset{U_\alpha}_{\alpha \in I}$ be an open cover of $\RR$ (cofinite topology).
    Proof: Arbitrary open cover.

<1>2. Pick a nonempty member $U_0$ of the cover.
    Proof: The cover is nonempty because $\RR \neq \emptyset$; and since the cover covers $\RR$, some $U_0$ contains a point, hence is nonempty. (If $U_0$ were empty it still exists; choose one that is nonempty since the union is all of $\RR$.)

<1>3. The complement $\RR \setminus U_0$ is finite: $\RR \setminus U_0 = \theset{x_1, \ldots, x_n}$.
    Proof: Definition of the cofinite topology: nonempty open sets have finite complement.

<1>4. For each $j = 1, \ldots, n$, choose $U_j \in \mathcal{U}$ with $x_j \in U_j$.
    Proof: $\mathcal{U}$ covers $\RR$.

<1>5. $\theset{U_0, U_1, \ldots, U_n}$ is a finite subcover of $\RR$.
    Proof: $U_0$ covers everything except $\theset{x_1, \ldots, x_n}$, and each $x_j$ is covered by $U_j$ (<1>4).

<1>6. Q.E.D.
    Proof: <1>1--<1>5 show every open cover of $\RR$ (cofinite) has a finite subcover.

:::
