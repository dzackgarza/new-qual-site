---
schema: qual/card@1
id: E-HAT-3.3-20
kind: problem
title: Compactly supported $H^0$ of noncompact spaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 20; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: for compact $K$ the complement is nonempty, so restriction of locally
    constant functions from a path-connected $X$ to $X-K$ is injective and the relative group
    vanishes; the compactly supported group is the limit of these.
---

::: {.problem}
Show that $H_c^0(X; G) = 0$ if $X$ is path-connected and noncompact.
:::

::: {.solution}
For every compact subset $K\subset X$, the complement $X\setminus K$ is nonempty because $X$ is noncompact. The long exact cohomology sequence of the pair $(X,X\setminus K)$ begins
$$
0\longrightarrow H^0(X,X\setminus K;G)
\longrightarrow H^0(X;G)
\longrightarrow H^0(X\setminus K;G).
$$
Since $X$ is path-connected, $H^0(X;G)\cong G$, and restriction to the nonempty subspace $X\setminus K$ is injective: a constant function that vanishes there vanishes everywhere. Thus $H^0(X,X\setminus K;G)=0$ for every compact $K$. Taking the direct limit over compact subsets gives $H_c^0(X;G)=0$.
:::
