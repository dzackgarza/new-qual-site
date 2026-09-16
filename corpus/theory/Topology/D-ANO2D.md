---
schema: qual/card@1
id: D-ANO2D
kind: definition
title: Covering Space
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
A \dfn{covering space} of $X$ is a topological space $\tilde X$ together with a [[D-AEAAD|continuous map]] $p\colon \tilde X\to X$ such that every $x\in X$ has an open [[D-JMRPA|neighborhood]] $U$ for which $p\inv(U)$ is a union of pairwise disjoint open sets $V_i\subseteq\tilde X$, each mapped [[D-9KQZT|homeomorphically]] onto $U$ by $p$.
The sets $V_i$ are the \dfn{sheets} of $\tilde X$ over $U$.
:::

::: {.definition}
Let $p_1\colon\tilde X_1\to X$ and $p_2\colon\tilde X_2\to X$ be covering spaces of $X$.
An \dfn{isomorphism of covering spaces} is a homeomorphism $f\colon\tilde X_1\to\tilde X_2$ with $p_2\circ f = p_1$:

\begin{tikzcd}
	{\tilde X_1} && {\tilde X_2} \\
	\\
	& {X}
	\arrow["{p_1}"', from=1-1, to=3-2]
	\arrow["{p_2}", from=1-3, to=3-2]
	\arrow["{f}", from=1-1, to=1-3]
\end{tikzcd}
:::

::: {.concept}
[@Hat02, §1.3].
:::
