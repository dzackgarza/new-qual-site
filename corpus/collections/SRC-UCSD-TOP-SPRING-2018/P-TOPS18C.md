---
schema: qual/card@1
id: P-TOPS18C
kind: problem
title: "H_1 of a mapping telescope built from degree-k gluing maps"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Direct Limits
  - Mapping Telescope
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $X_n$ be the space formed from the disjoint union of $n$ copies $C_1, \ldots, C_n$ of the cylinder $S^1 \times I$ by gluing, for each $k$, the $S^1 \times \{1\}$ of $C_k$ to the $S^1 \times \{0\}$ of $C_{k+1}$ using a map of degree $k$.
There is a natural sequence of inclusions $X_1 \subseteq X_2 \subseteq X_3 \subseteq \cdots$ and so we may define $X$ to be the direct limit of this family.
(This is called a mapping telescope.)
What is $H_1(X; \mathbb{Z})$?
:::

::: {.solution}
<1>1. $H_1(X_n) = \ZZ$ for each $n$.
Proof: $X_n$ is homotopy equivalent to $S^1$ (each cylinder $S^1 \times I$ deformation retracts onto $S^1$, and the gluing maps are homotopy equivalences on $S^1$), so $H_1(X_n) = H_1(S^1) = \ZZ$.

<1>2. The inclusion $X_n \hookrightarrow X_{n+1}$ induces on $H_1$ the map $\ZZ \to \ZZ$ given by multiplication by $n$.
Proof: the inclusion of $X_n$ into $X_{n+1}$ sends the generator of $H_1(X_n)$ (the core circle of $C_n$) to the core circle of $C_{n+1}$ via the gluing map of degree $n$, so the induced map is multiplication by $n$.

<1>3. $H_1(X) = \varinjlim H_1(X_n)$.
Proof: homology commutes with direct limits (filtered colimits) of spaces.

<1>4. The direct limit of the system $\ZZ \xrightarrow{1} \ZZ \xrightarrow{2} \ZZ \xrightarrow{3} \ZZ \xrightarrow{4} \cdots$ is $\QQ$.
Proof: the direct limit of $\ZZ \xrightarrow{\cdot n} \ZZ$ over all $n$ is the localization of $\ZZ$ at all nonzero integers, i.e. $\QQ$ (every element is a fraction $a/b$ with $b$ a product of the gluing degrees).

<1>5. Hence $H_1(X;\ZZ) = \QQ$.
Proof: <1>3 and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
