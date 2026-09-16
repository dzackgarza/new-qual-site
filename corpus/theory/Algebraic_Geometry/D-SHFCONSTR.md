---
schema: qual/card@1
id: D-SHFCONSTR
kind: definition
title: Constructible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Constructible Sheaves
  - Local Systems
  - Stratifications
relations:
- kind: uses
  target: D-SHFLOCSYS
review: draft
prompts:
- What is a constructible sheaf?
---

::: {.definition title="Constructible sheaf"}
Let $X$ be a complex algebraic variety with its analytic topology.
A sheaf $\mathcal{F}$ of $k$-vector spaces on $X$ is \dfn{constructible} if there is a finite partition $X = \coprod_i X_i$ into Zariski locally closed subvarieties such that each restriction $\mathcal{F}|_{X_i}$ is a local system.
:::

::: {.remark}
The same definition with the Zariski or étale topology on a Noetherian scheme, and locally constant sheaves with finite stalks in place of local systems, gives constructible étale sheaves.
Constructible sheaves are preserved by $f^{-1}$, by $f_*$ and $f_!$ for morphisms of varieties, and by $\otimes$ and $\mathcal{H}om$, in the derived sense; this closure is what makes them the coefficients for the six operations on varieties.
:::

::: {.example}
Let $j \colon U = \AA^1 \setminus \{0\} \hookrightarrow \AA^1$ and $i \colon \{0\} \hookrightarrow \AA^1$ over $\CC$.
The sheaf $j_! \ul{\CC}_U$ has stalk $\CC$ on $U$ and $0$ at $0$, and $i_* \CC$ has stalk $\CC$ at $0$ and $0$ elsewhere.
Both are constructible with respect to the partition $\AA^1 = U \amalg \{0\}$, and neither is a local system on $\AA^1$.
:::
