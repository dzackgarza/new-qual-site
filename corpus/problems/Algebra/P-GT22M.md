---
schema: qual/card@1
id: P-GT22M
kind: problem
title: If $K/F$ is cyclic and $E/F$ is normal then $E/F$ and $K/E$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}

Let $F \subseteq E \subseteq K$ be a tower of fields such that $K/F$ is a finite cyclic Galois extension.
Suppose $E/F$ is normal.
Prove that both $E/F$ and $K/E$ are cyclic Galois extensions.

:::

::: {.solution}

Let $G=\Gal(K/F)$ and $H=\Gal(K/E)$. Since $K/F$ is cyclic Galois, $G$ is cyclic.

::: pf

::: pf-step

$K/E$ is cyclic Galois.

::: pf-proof

Since $K/F$ is Galois, so is $K/E$, and by the Galois correspondence its group $H$ is a subgroup of $G$. Every subgroup of a cyclic group is cyclic.

:::

:::

::: pf-step

$E/F$ is cyclic Galois.

::: pf-proof

Every subgroup of the abelian group $G$ is normal, so $H\trianglelefteq G$. By the Galois correspondence $E/F$ is Galois and restriction gives $\Gal(E/F)\cong G/H$. A quotient of a cyclic group is cyclic.

:::

:::

:::

:::

::: {.remark}

The hypothesis that $E/F$ is normal is redundant: every intermediate field of a finite cyclic Galois extension is Galois over the base field.

:::
