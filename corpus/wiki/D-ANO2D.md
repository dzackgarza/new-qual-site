---
schema: qual/card@1
id: D-ANO2D
kind: definition
title: "Covering Space"
classification:
  areas:
  - topology
  topics:
  - covering-spaces
relations: []
review: draft
---

::: {.definition title="Covering Space"}
A **covering space** of $X$ is the data $p: \tilde X \to X$ such that

1. Each $x\in X$ admits a neighborhood $U$ such that $p ^{-1} (U)$ is a union of disjoint open sets in $\tilde V_i \subseteq X$ (the **sheets** of $\tilde X$ over $U$),

2. $\ro{p}{V_i}: V_i \to U$ is a homeomorphism for each sheet.

An **isomorphism** of covering spaces $\tilde X_1 \cong \tilde X_2$ is a commutative diagram

\begin{tikzcd}
	{\tilde X_1} && {\tilde X_2} \\
	\\
	& {X}
	\arrow["{p_1}"', from=1-1, to=3-2]
	\arrow["{p_2}", from=1-3, to=3-2]
	\arrow["{f}", from=1-1, to=1-3]
\end{tikzcd}
> [Link to diagram](https://q.uiver.app/?q=WzAsMyxbMCwwLCJcXHRpbGRlIFhfMSJdLFsxLDIsIlgiXSxbMiwwLCJcXHRpbGRlIFhfMiJdLFswLDEsInBfMSIsMl0sWzIsMSwicF8yIl0sWzAsMiwiZiJdXQ==)
:::
