---
schema: qual/card@1
id: PR-UBJ6P
kind: proposition
title: Universal cover and deck groups
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.proposition}
Let $X$ be path-connected, locally path-connected and [[D-EPQ54|semilocally simply connected]].
Then $X$ has a [[D-BX3WD|universal cover]] $p\colon\hat X \to X$ [@Hat02, §1.3, p. 64].
If $q\colon C\to X$ is a covering map with $C$ path-connected, then there is a covering map $\tilde p\colon \hat{X} \to C$ with $q\circ\tilde p = p$ [@Hat02, Theorem 1.38, p. 67]:

\begin{tikzcd}
	{C} && {\hat X} \\
	\\
	{X}
	\arrow["{q}", from=1-1, to=3-1, two heads]
	\arrow["{p}", from=1-3, to=3-1, two heads]
	\arrow["{\tilde p}"', from=1-3, to=1-1, dashed, two heads]
\end{tikzcd}

In particular, $\hat X$ is unique up to isomorphism of covering spaces.
:::

::: {.remark}
The [[D-4VGAW|deck transformation group]] of the universal cover is isomorphic to $\pi_1(X)$; deck groups of general covers are described in [[T-F4PQY]] [@Hat02, Proposition 1.39, p. 71].
:::
