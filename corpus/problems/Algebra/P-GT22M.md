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

::: problem
Let $F \subseteq E \subseteq K$ be a tower of fields such that $K/F$ is a finite cyclic Galois extension.
Suppose $E/F$ is normal.
Prove that both $E/F$ and $K/E$ are cyclic Galois extensions.
:::

::: solution
Let
\[
G=\operatorname{Gal}(K/F),\qquad H=\operatorname{Gal}(K/E).
\]
Since $K/F$ is cyclic Galois, $G$ is cyclic. By the Galois correspondence,
\[
\operatorname{Gal}(K/E)=H\le G,
\]
so $H$ is cyclic because every subgroup of a cyclic group is cyclic. Hence $K/E$ is cyclic Galois.

Also every subgroup of a cyclic group is normal, so $H\trianglelefteq G$. Therefore $E/F$ is Galois and restriction gives
\[
\operatorname{Gal}(E/F)\cong G/H.
\]
A quotient of a cyclic group is cyclic, so $E/F$ is cyclic Galois.

Thus both $K/E$ and $E/F$ are cyclic. In fact, the stated assumption that $E/F$ is normal is redundant: every intermediate field of a finite cyclic Galois extension is Galois over the base field.
:::
